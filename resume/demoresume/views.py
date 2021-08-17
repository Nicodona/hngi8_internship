from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'home.html')
