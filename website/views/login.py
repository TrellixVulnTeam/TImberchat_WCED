from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, user_logged_in, checks
from django.urls import reverse
from ..views import HomePage

class Login(View):
    def get(self, request):
        if(request.user.is_authenticated):
            return redirect(reverse('website_homepage'))
        else:
            return render(request, 'login.html')

    def post(self, request):
        uname = request.POST.get('username')
        pasd = request.POST.get('password')

        user = authenticate(request, username=uname, password=pasd)
        if(user):
            login(request, user)
            return JsonResponse({'type': 'success'})
        else:
            return JsonResponse({'type': 'Failure', 'data': "Credentials are wrong please try with another"})

