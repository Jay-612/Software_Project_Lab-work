from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return render(request, 'hello.html', {'name': 'User'})

def calc(request):
    c = ''
    if request.method == "POST":
        n1 = int(request.POST['num1'])
        n2 = int(request.POST['num2'])
        c = n1 + n2

    return render(request, 'calc.html', {'result': c})