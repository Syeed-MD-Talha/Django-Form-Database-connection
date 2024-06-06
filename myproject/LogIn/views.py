from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def LogIn(request):
    if request.method == "POST":
        frm = AuthenticationForm(request=request, data=request.POST)
        if frm.is_valid():
            username = frm.cleaned_data['username']
            password = frm.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse("<h1>Successfully Logged In</h1>")
            else:
                return HttpResponse("<h1>Invalid login credentials</h1>")
        else:
            print("!!!!!!!!!! ERROR !!!!!!!!!!!!!!")
    else:
        print("========= GET request =========")
        frm = AuthenticationForm()
        
    return render(request, 'login.html', {'form': frm})





def LogOut(request):
    logout(request)
    return HttpResponseRedirect('../signup')

