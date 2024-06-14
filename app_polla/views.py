from django.shortcuts import render, redirect,  get_object_or_404
from .models import Partido, Marcador, ViewPosiciones, ViewPartido, AuthUser, ViewCalculo, ViewCuadroHonor, ViewMarcador, ViewPosicionesPlayOff
from django.contrib.auth import authenticate, login
from django.db.models import Q
from .forms import MarcadorForm
from django.contrib.auth.models import User
from django.utils import timezone

def posiciones(request):
    posiciones = ViewPosiciones.objects.all()
    return render(request,'posiciones.html',{'posiciones': posiciones})

def posiciones_playoff(request):
    posiciones_playoff = ViewPosicionesPlayOff.objects.all()
    return render(request,'posiciones_playoff.html',{'posiciones_playoff': posiciones_playoff})

def marcadores(request):
    marcadores = ViewPartido.objects.all()
    return render(request,'marcadores.html',{'marcadores': marcadores})

def marcadores_usuario(request, pk):
    usuario = AuthUser.objects.get(id=pk)
    marcadores_usuario = ViewCalculo.objects.all().filter(usuario=pk).order_by('nro_partido')
    return render(request,'marcadores_usuario.html',{'marcadores_usuario': marcadores_usuario, 'usuario' : usuario})

def marcadores_partido(request, pk):
    marcadores_partido = ViewCalculo.objects.all().filter(nro_partido=pk).order_by('marcador1','marcador2')
    return render(request,'marcadores_partido.html',{'marcadores_partido': marcadores_partido})    

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