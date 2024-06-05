from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def solution(request):
    return render(request,'solution.html')