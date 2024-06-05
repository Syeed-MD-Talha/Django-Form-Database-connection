from django.shortcuts import render
from django.http import HttpResponse
from Problems.models import online_judge

# Create your views here.

def problemSet(request):
    return render(request,'problems/twoSum.html')

def show_table(request):
    data=online_judge.objects.all()
    return render(request,'problems/problemSolvingSites.html',{'data':data})