from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

def home(request):
    return render(request,'home.html')

#REGISTRATION
def registro(request):

    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()

            # autenticar al usuario recien registrado...
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            #hay que poner 2 veces la password para registrarse (a modo de confirmacion), por eso en el diccionario de datos existiran 2, 
            # y en este caso para autenticar al usuario,llamamos a password1
            
            #en este caso el login siempre sera correcto, pq el usuario acaba de crearse
            login(request,user)

            #redirigir al index
            return redirect(to="home")
        data["form"] = formulario #se reescribre el formulario, si hay problemas al guardarse


    return render(request,'registration/registro.html',data)