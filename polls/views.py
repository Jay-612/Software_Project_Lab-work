from django.shortcuts import render
# You can remove HttpResponse if you aren't using it anymore

def home(request):
    # This renders the html file you just created
    return render(request, 'hello.html')