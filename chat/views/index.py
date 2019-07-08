from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate
from ..models import Chat as ChatModel

class Chat(View):
    def get(self, request):
        return render(request, 'chat.html')

    def post(self, request):
        chat = ChatModel()
        chat.name = request.user.first_name
        chat.text = request.POST.get('chat_text')
        chat.save()
        response = {}
        response['type'] = 'success'
        # return JsonResponse(response);

        return render(request, 'chat.html');
