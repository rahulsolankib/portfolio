from django.shortcuts import render,redirect  
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import sys
import pickle
import io
import urllib,base64

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hurray!! Your Account Has been Created, You Can Login Now...')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'user/register.html',{'form':form,'title':'Register Here!'})

@login_required
def profile(request):
    return render(request,'user/profile.html')

def invest(request):    
    data = pd.read_csv("user/forex_inr.csv")
    data.Price = 1/data.Price
    random.seed(1234)
    stock_counter = 1
    mean_daily_returns = []
    cov_input = []

    while stock_counter <= 33:
        indv_stock = data[data.Stock_No == stock_counter]
        avg_return = indv_stock.Price.mean()
        mean_daily_returns.append(avg_return)
        cov_input.append(indv_stock.Price.tolist())
        stock_counter += 1

    mean_daily_returns = np.matrix(mean_daily_returns)
    cov_input = np.matrix(cov_input)
    cov_matrix = np.cov(cov_input)

    avg_sharpe_list, portfolio_return, portfolio_vol, portfolio_sharpe, portfolio_weights = bso_optimize(mean_daily_returns, cov_matrix)

    portfolios = {'Returns': portfolio_return,
                'Volatility': portfolio_vol,
                'Sharpe Ratio': portfolio_sharpe,
                'Weights': portfolio_weights}
    portfolios_df = pd.DataFrame(portfolios)

    averages = {'Average Sharpe Ratio': avg_sharpe_list}
    averages_df = pd.DataFrame(averages)

    max_sharpe = portfolios_df['Sharpe Ratio'].max()
    optimal_portfolio = portfolios_df.loc[portfolios_df['Sharpe Ratio'] == max_sharpe]
    clu = pd.DataFrame()
    q = data['To'].unique()
    c = optimal_portfolio.Weights.keys()
    clu['weight']=optimal_portfolio.Weights[c[0]]
    clu['Currency']=q
    clu = clu.dropna()
    df = clu.sort_values(by=['weight'], ascending=False)
    top = df[:5]
    fig, axes = plt.subplots(figsize=(7,5), dpi=100)
    plt.bar(top.Currency, height=top.weight)
    plt.title('Barplot of Investing in Currency');
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    url = urllib.parse.quote(string)
    return render(request,'user/invest.html',{'data':url})

def bso_optimize(mean_daily_returns, cov_matrix):
    """
    Function for Particle Swarm Optimization
    """
    dimensions = 33
    iterations = 25
    swarm_size = 50

    swarm_position = []
    for particle in range(swarm_size):
        position = [0]*dimensions
        for dimension in range(dimensions):
            position[dimension] = random.random()
        swarm_position.append(position)

    swarm_velocity = []
    for particle in range(swarm_size):
        velocity = [0]*dimensions
        for dimension in range(dimensions):
            velocity[dimension] = random.random()
        swarm_velocity.append(velocity)

    swarm_position = np.array([np.array(p) for p in swarm_position])
    swarm_velocity = np.array([np.array(v) for v in swarm_velocity])
    particles_pbest = swarm_position 
    swarm_gbest = particles_pbest[0] 

    vmax = 0
    vmin = -sys.maxsize - 1
    delta = 0.5
    delta0 = delta
    sharpe_pbest_all = []
    for particle in range(swarm_size):
        sharpe_pbest = sharpe(particles_pbest[particle], mean_daily_returns, cov_matrix) 
        sharpe_pbest_all.append(sharpe_pbest)
        #sharpe(particles_pbest[particle], mean_daily_returns, cov_matrix) 
    #print(sharpe_pbest_all)

    avg_sharpe_list = []
    portfolio_return = []
    portfolio_vol = []
    portfolio_sharpe = []
    portfolio_weights = []
    #velocity = [0 for i in range(dimensions)]
    omegamin = 0.4
    omegamax = 0.9
    c1 = 2.5
    c2 = 0.5
    lam = 0.5
    print("reached")
    for iteration in range(iterations):
        sharpe_pbest_all = []
        w = omegamax - (((omegamax - omegamin)/iterations) * iteration)
        d = delta/c2
        for particle in range(swarm_size):
            ls = swarm_position[particle] - swarm_velocity[particle] * d/2
            rs = swarm_position[particle] + swarm_velocity[particle] * d/2
            #swarm_position[particle][dimension] = swarm_position[particle][dimension] + swarm_velocity[particle][dimension] 
            fls = sharpe(ls, mean_daily_returns, cov_matrix) 
            frs = sharpe(rs, mean_daily_returns, cov_matrix) 
            for dimension in range(dimensions):
                r1 = random.random()
                r2 = random.random()
                #swarm_velocity[particle][dimension] = w * swarm_velocity[particle][dimension] + c1 * r1 * np.linalg.norm(particles_pbest[particle][dimension] - swarm_position[particle][dimension]) + c2 * r2 * np.linalg.norm(swarm_gbest[dimension] - swarm_position[particle][dimension]) # Update velocity in every dimension
                incremental = delta * swarm_velocity[particle][dimension] * abs(frs - fls)
                
                swarm_velocity[particle][dimension] = w * swarm_velocity[particle][dimension] + c1*r1*(particles_pbest[particle][dimension] - swarm_position[particle][dimension]) +c2*r2*(swarm_gbest[dimension] - swarm_position[particle][dimension])
                swarm_position[particle][dimension] = swarm_position[particle][dimension] + lam*swarm_velocity[particle][dimension] + (1 - lam)*incremental
                #print(particle, dimension)
            sharpe_pbest = sharpe(particles_pbest[particle], mean_daily_returns, cov_matrix)
            if sharpe(swarm_position[particle], mean_daily_returns, cov_matrix) > sharpe_pbest: 
                particles_pbest[particle] = swarm_position[particle] 
                sharpe_pbest = sharpe(particles_pbest[particle], mean_daily_returns, cov_matrix) 
            sharpe_pbest_all.append(sharpe_pbest) 
        if max(sharpe_pbest_all) > sharpe(swarm_gbest, mean_daily_returns, cov_matrix):
            max_index = sharpe_pbest_all.index(max(sharpe_pbest_all))
            swarm_gbest = particles_pbest[max_index] 
        delta = delta * c1 + delta0
        avg_sharpe = sum(sharpe_pbest_all)/len(sharpe_pbest_all) 
        avg_sharpe_list.append(avg_sharpe) 
        # print(iteration)
        portfolio_return, portfolio_vol, portfolio_sharpe, portfolio_weights = optimized_solution(iteration, swarm_gbest, mean_daily_returns, cov_matrix, portfolio_return, portfolio_vol, portfolio_sharpe, portfolio_weights)

    return avg_sharpe_list, portfolio_return, portfolio_vol, portfolio_sharpe, portfolio_weights

def sharpe(weights, mean_daily_returns, cov_matrix,i=0):
    """
    Function to calculate Sharpe ratio
    """
    weights = [w/sum(weights) for w in weights] 
    weights = np.matrix(weights)
    port_return = np.round(np.sum(weights * mean_daily_returns.T) * 1259, 2)/5
    port_std_dev = np.round(np.sqrt(weights * cov_matrix * weights.T) * np.sqrt(1259), 2)/np.sqrt(5)
    port_std_dev = float(port_std_dev)
    sharpe_ratio = (port_return - 2.57)/ port_std_dev 
    risk = 25
    returns = 15
    lam = 1
    if (port_return < returns) and (port_std_dev > risk):
        h = 2
    elif (port_return < returns) or (port_std_dev > risk):
        h = 1
    else:
        h = 0
    sharpe_ratio -= h * lam
    if i == 1:
        return sharpe_ratio, port_return, port_std_dev
    return sharpe_ratio

def optimized_solution(i, weights, mean_daily_returns, cov_matrix, portfolio_return, portfolio_vol, portfolio_sharpe, portfolio_weights):
    sharpe_ratio, port_return, port_std_dev = sharpe(weights, mean_daily_returns, cov_matrix, i = 1)
    portfolio_return.append(port_return) 
    portfolio_vol.append(port_std_dev) 
    portfolio_sharpe.append(sharpe_ratio)
    portfolio_weights.append(weights)

    return portfolio_return, portfolio_vol, portfolio_sharpe, portfolio_weights
