from django.shortcucuts import render,redirect

def inicio(request):
    return render(request,"index.html")
    