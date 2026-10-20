from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = user.Role.USUARIO
            user.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})

def login_manual(request):
    """Login real con validación de contraseña."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Aquí Django verifica la contraseña de verdad
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_superuser or user.role == 'GESTOR':
                return redirect('gestor_panel')
            return redirect('dashboard')
        else:
            # Si falla, lo devolvemos al login
            from django.contrib import messages
            messages.error(request, 'Usuario o contraseña incorrectos.')
            return redirect('login')
            
    # Mostrar el formulario vacío
    from django.contrib.auth.forms import AuthenticationForm
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def dashboard(request):
    u = request.user
    if u.is_superuser or u.role == u.Role.ADMIN:
        return redirect("/admin/")
    if u.role == u.Role.GESTOR:
        return redirect("gestor_panel")
    return render(request, "accounts/dashboard.html")