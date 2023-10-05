from django.shortcuts import render

# Create your views here.
def publicaciones(request):
    context = {}
    return render(request, 'inicio.html',context)
