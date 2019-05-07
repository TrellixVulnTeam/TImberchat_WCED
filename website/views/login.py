from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        return HttpResponse("Login Post")
