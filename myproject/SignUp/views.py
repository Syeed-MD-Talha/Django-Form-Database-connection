from django.shortcuts import render
from .forms import AddUser

# Create your views here.
def SignUp(request):
    if request.method=="POST":
        frm=AddUser(request.POST)
        if frm.is_valid():
            frm.save()
            

            
    frm=AddUser()
    return render(request,'SignUp.html',{'form':frm})