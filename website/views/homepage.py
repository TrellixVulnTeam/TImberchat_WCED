from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

class HomePage(View):
    def get(self, request):
        return render(request, 'homepage.html')

    def post(self, request):
        return HttpResponse("HomePage Post")
