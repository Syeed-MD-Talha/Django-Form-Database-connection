from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactUsForm
from .models import ContactUs

# Create your views here.
def contact(request):
    data=ContactUsForm()
    if request.method=='POST':
        print("============= POST METHOD =============")
        info=ContactUsForm(request.POST)
        if info.is_valid():
            # print(info.cleaned_data)
            name=info.cleaned_data['name']
            email=info.cleaned_data['email']
            message=info.cleaned_data['txt']
            Insert_data_to_database=ContactUs(name=name,email=email,message=message)
            Insert_data_to_database.save()
            return HttpResponse("form has submitted successfully")

    else:
        print("============= GET METHOD =============")

    return render(request,'contact.html',{'form':data})