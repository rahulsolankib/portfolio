from django.shortcuts import render,redirect  
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required 


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print(form)

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

