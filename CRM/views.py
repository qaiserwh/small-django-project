from CRM.models import Accused, Employe, FrontManager
from django.shortcuts import render ,redirect
from . forms import AdminLoginForm
from django.contrib.auth import authenticate, login

# Create your views here.
def admin(request):
    return render
def admin_login(request):
    forms = AdminLoginForm()
    if request.method == 'POST':
        forms = AdminLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request,user)
                return redirect('front')
    context = {'forms': forms}
    return render(request, 'page/login.html', context)



def front(request):
    context={
        'front':FrontManager.objects.all()
    }
    return render (request,'page/front.html',context)
    
def index(request):
    context={
        'acce':Accused.objects.all()
    }

    return render(request,'page/index.html',context)

def cardacc(request):
    context={
        'rar':Accused.objects.all()
    }
    
    return render(request,'page/cardacc.html',context)
def emplist(request):
    context={
        'emplist':Employe.objects.all()
    }

    return render(request,'page/emplist.html',context)

def cardemp(request):
    context={
        'cardemp':Employe.objects.all()
    }
    
    return render(request,'page/cardemp.html',context)
