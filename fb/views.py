from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse('hrllo')
    return render(request,'index.html')

def signup(request):
    return render(request,'signup.html')
from django.contrib import messages
def login(request):
    if request.method == 'POST':
        print('post')
        username = request.POST['email']
        password = request.POST['password']
        if username == "111arpit1@gmail.com" and password == "123":
            # messages.success(request,'Successfullt logged in')
            context = { "data" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14],} 
            return redirect('/arpit',context)
        else:
            messages.error(request,'Wrong email or password!!.')

    else:
        print('not post')
        # messages.error(request,'Error occured!!.')
    return render(request,'login.html')

def arpit(request):
    return render(request,'arpit.html')
def messenger(request):
    return render(request,'messenger.html')
def lite(request):
    return render(request,'lite.html')