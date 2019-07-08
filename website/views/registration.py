from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User


class Registration(View):
    def get(self, request):
        return render(request, 'registration.html')

    def post(self, request):

        user = User.objects.create_user(username=request.POST.get('username'), first_name=request.POST.get('first_name'), last_name=request.POST.get('last_name'), email=request.POST.get('email'), password=request.POST.get('password'))
        user.save()

        response = {}
        response['email'] = request.POST.get("email")
        return JsonResponse(response)