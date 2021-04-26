from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
from myapp.models import Contect
from django.contrib import messages
from django.contrib.auth.models import User ,auth


# Create your views here.

def index(request):

    # context = {
    #     "variable1":"this is manually added in the text",
    #     "variable2":"this is second variable formate"
    # }
    return render(request, 'index.html')
    # return HttpResponse("this is home page")

def register(request):

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        confirm_password = request.POST['password2']

        if password1 == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username alrady taken')
                return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email alredy register')
                return render(request,'register.html')
            
            else:
                user = User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,
                        last_name=last_name)
                user.save()
                messages.success(request,'Register Successfully goto Login !')
                return render(request,'register.html')
        
        else:
            messages.info(request,'password not  matching ...')
            return render(request,'register.html')
    else:
        return render(request,'register.html')


def loginuser(request):

    if request.method =="POST":
        username = request.POST['username']
        password1 = request.POST['password1']


        user = auth.authenticate(username=username,password=password1)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'login Successfully!')

            return render(request,'index.html')
        else:
            messages.info(request,'Invailid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
   
    return render(request, 'login.html')


def logoutuser(request):
    auth.logout(request)
    messages.success(request,'logout Successfully!')

    return render(request, 'index.html')
    
def about(request):
     return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')

def contect(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')
        contect = Contect(name=name, email=email, phone =phone, msg=msg,
        date= datetime.today())
        contect.save()
        messages.success(request, 'Your massage has been sent !')
    return render(request, 'contect.html')


