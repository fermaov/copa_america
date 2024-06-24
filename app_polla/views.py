from django.shortcuts import render, redirect,  get_object_or_404
from .models import Partido, Marcador, ViewPosiciones, ViewPartido, AuthUser, ViewCalculo, ViewCuadroHonor, ViewMarcador, ViewPosicionesPlayOff
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q
from .forms import MarcadorForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.messages import success
import os
from django.conf import settings
from django.http import FileResponse

def posiciones(request):
    queryset = ViewPartido.objects.all().filter(nom_estado='En juego')
    en_juego = queryset.count()
    posiciones = ViewPosiciones.objects.all()
    return render(request,'posiciones.html',{'posiciones': posiciones, 'en_juego':en_juego})

def posiciones_playoff(request):
    queryset = ViewPartido.objects.all().filter(nom_estado='En juego')
    en_juego = queryset.count()
    posiciones_playoff = ViewPosicionesPlayOff.objects.all()
    return render(request,'posiciones_playoff.html',{'posiciones_playoff': posiciones_playoff, 'en_juego':en_juego})

def marcadores(request):
    marcadores = ViewPartido.objects.all()
    return render(request,'marcadores.html',{'marcadores': marcadores})

def marcadores_chequeo(request):
    marcadores = ViewPartido.objects.all()
    return render(request,'marcadores_chequeo.html',{'marcadores': marcadores})

def marcadores_usuario(request, pk):
    usuario = AuthUser.objects.get(id=pk)
    marcadores_usuario = ViewCalculo.objects.all().filter(usuario=pk).order_by('nro_partido')
    return render(request,'marcadores_usuario.html',{'marcadores_usuario': marcadores_usuario, 'usuario' : usuario})

def marcadores_partido(request, pk):
    partido =  ViewPartido.objects.get(nro_partido=pk)    
    marcadores_partido = ViewCalculo.objects.all().filter(nro_partido=pk).order_by('marcador1','marcador2')
    return render(request,'marcadores_partido.html',{'marcadores_partido': marcadores_partido, 'partido': partido}) 

def marcadores_partido_chequeo(request, pk):
    partido =  ViewPartido.objects.get(nro_partido=pk)    
    marcadores_partido = ViewCalculo.objects.all().filter(nro_partido=pk).order_by('marcador1','marcador2')
    return render(request,'marcadores_partido_chequeo.html',{'marcadores_partido': marcadores_partido, 'partido': partido})    

def cuadro_honor(request):
    cuadro_honor = ViewCuadroHonor.objects.all().order_by('nom_campeon','nom_subcampeon','nom_tercero','nom_cuarto')
    return render(request,'cuadro_honor.html',{'cuadro_honor': cuadro_honor})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirigir al usuario a una página después de iniciar sesión
            return redirect('posiciones')
        else:
            # Mensaje de error si las credenciales son incorrectas
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    else:
        return render(request, 'login.html')

def mis_marcadores(request):
    usuario = request.user.id
    mis_marcadores = ViewMarcador.objects.filter(Q(usuario=usuario) | Q(usuario=None)).order_by('nro_partido')
    return render(request,'mis_marcadores.html',{'mis_marcadores': mis_marcadores})    

def marcador_new(request, nro_partido):
    usuario = User.objects.get(username=request.user.username)
    usuario = AuthUser.objects.get(id=usuario.id)
    partido = Partido.objects.get(nro_partido=nro_partido)
    
    if partido.fecha > timezone.now():
        if request.method == 'POST':
            try:
                marcador_existe = Marcador.objects.get(usuario=request.user.id, nro_partido=nro_partido)
                return redirect('mis_marcadores')
            except Marcador.DoesNotExist:
                form = MarcadorForm(request.POST)
                if form.is_valid():
                    marcador = form.save(commit=False)
                    marcador.usuario = usuario
                    marcador.nro_partido = partido
                    marcador.fecha_mod = timezone.now()
                    marcador.save()
                    # Redirige a una página de éxito o a donde desees después de guardar los datos
                    return redirect('mis_marcadores')
            
        else:
            form = MarcadorForm(instance=partido)
    else:
        return redirect('mis_marcadores')
    return render(request, 'marcador_edit.html', {'form': form})    
        
def marcador_edit(request, pk):
    #marcador = get_object_or_404(Marcador, pk=pk)
    marcador = Marcador.objects.get(pk=pk)
    partido = Partido.objects.get(nro_partido=marcador.nro_partido.nro_partido)
    if partido.fecha > timezone.now():
        if request.method == "POST":
            form = MarcadorForm(request.POST, instance=marcador)
            if form.is_valid():
                marcador = form.save(commit=False)
                marcador.fecha_mod = timezone.now()
                marcador.save()
                return redirect('mis_marcadores')
        else:
            form = MarcadorForm(instance=marcador)
    else:
        return redirect('mis_marcadores')
    return render(request, 'marcador_edit.html', {'form': form})

def cambio_contrasena(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)  # Pass user and POST data
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            message = 'Contraseña cambiada con éxito.'
            success(request, 'Contraseña cambiada con éxito.')
            #return redirect('posiciones')
            return render(request, 'mensaje.html', {})
    else:
        form = PasswordChangeForm(request.user)  # Pass user for initial form
    return render(request, 'cambio_contrasena.html', {'form': form})

def logout_view(request):
    logout(request)  # Logout the user
    return redirect('login')  # Redirect to the login page

def puntos_detalle(request, usuario, nro_partido):
    calculo =  ViewCalculo.objects.get(usuario=usuario, nro_partido=nro_partido)    
    return render(request,'puntos_detalle.html',{'calculo': calculo}) 
