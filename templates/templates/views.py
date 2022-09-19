from django.http import HttpResponse
from django.shortcuts import render

# def about(request):
#     return HttpResponse('This is about page')
# def home(request):
#     return HttpResponse('My home')
# def homee(request):
#     return render(request,'home.html')
def homeee(request):
    return render(request,'home.html')