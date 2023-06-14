from django.shortcuts import render
from .models import HomeModel
import requests as r
# Create your views here.

def HomePage(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    email = request.POST.get('email')
    obj = HomeModel.objects.create(name=name,surname=surname,email=email)
    obj.save()

    token = "6129236243:AAEfiaGL4q5esogOfv6CPPqJa9KM-HmhuI8"
    text = f"Sizga xabar yuborishdi: \nIsm: {request.POST.get('name')} \nFamilya: {request.POST.get('surname')} \nEmail: {request.POST.get('email')}"
    url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id='
    r.get(url + str(5469101117) + '&text=' + text)
  return render(request,'index.html')