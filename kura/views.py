from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request, '')

def register_view(request):
    if request.method=='POST':
        username= request.POST['username']
        passdword= request.POST['PASSWORD']
        
        
        if User.objects.filter(Username=Username).exist():
           messages.error(request, "Username already exist")
    
    
    