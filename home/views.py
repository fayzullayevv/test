from django.shortcuts import render
from .models import RegisterModell
import requests as r
# Create your views here.



def HomePage(request):
  if request.method == 'POST':
    name = request.POST.get('first')
    surname = request.POST.get('last')
    school = request.POST.get('school')
    clas = request.POST.get('class')
    age = request.POST.get('age')
    course = request.POST.get('course')
    obj = RegisterModell.objects.create(name=name,surname=surname,school=school,clas=clas,age=age,course=course)
    obj.save()

    token = "6129236243:AAEfiaGL4q5esogOfv6CPPqJa9KM-HmhuI8"
    text = f"Sizga xabar yuborishdi: \nFirst Name: {request.POST.get('first')} \nLast Name: {request.POST.get('last')} \nSchool: {request.POST.get('school')} \nClass: {request.POST.get('class')} \nAge: {request.POST.get('age')} \nCourse: {request.POST.get('course')}"
    url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id='
    r.get(url + str(5469101117) + '&text=' + text)
  return render(request,'index.html')
