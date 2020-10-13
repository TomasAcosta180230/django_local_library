from django.shortcuts import render, HttpResponse


def Home(request):

    return render(request, "ProyectoTeoriaweb/home.html")



def Tienda(request):

    return render(request,"ProyectoTeoriaweb/tienda.html")


def Blog(request):

    return render(request,"ProyectoTeoriaweb/blog.html")

def Contacto(request):

    return render(request,"ProyectoTeoriaweb/contacto.html")

# Create your views here.
