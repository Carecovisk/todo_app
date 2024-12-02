from django.views.generic import View
from django.shortcuts import redirect, resolve_url, render
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout


class Login(View):

    def get(self, request : HttpRequest):

        if request.user.is_authenticated:
            return redirect(resolve_url('listar-tarefas'))
        else:
            return render(request, 'login.html')
    
    def post(self, request : HttpRequest):

        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(resolve_url('listar-tarefas'))
            
            return render(request, 'login.html', {'mensagem': 'Usuario inativo.' })
        
        return render(request, 'login.html', {'mensagem': 'Usuario ou senha invalidos'})


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect(resolve_url('login'))