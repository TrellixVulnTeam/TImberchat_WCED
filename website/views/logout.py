from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, user_logged_in, logout
from django.urls import reverse
from ..views import HomePage

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('website_login'))

    def post(self, request):
        logout(request)
        return redirect(reverse('website_login'))
