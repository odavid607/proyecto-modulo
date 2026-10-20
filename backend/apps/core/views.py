from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def home(request):
    return render(request, "core/home.html")

def is_gestor(user):
    return user.is_authenticated and (user.role == "GESTOR" or user.is_superuser)

@login_required
@user_passes_test(is_gestor)
def gestor_panel(request):
    return render(request, "core/gestor.html")