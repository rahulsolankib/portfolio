from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm  
# Create your views here.

def register(request):
    form = UserCreationForm()
    return 
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request,'user/register.html',{'form':form,'title':'Register Here!'})