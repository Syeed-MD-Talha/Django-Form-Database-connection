from django.shortcuts import render, redirect
from .forms import AddUser

# Create your views here.
def SignUp(request):
    if request.method == "POST":
        frm = AddUser(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect('login')  # Redirect to a login page or another view after successful signup
    else:
        frm = AddUser()
    return render(request, 'SignUp.html', {'form': frm})
