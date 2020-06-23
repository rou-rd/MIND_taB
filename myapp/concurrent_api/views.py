from django.shortcuts import render
import requests

def home(request):
    response = requests.get('http://localhost:5000/todo/api/v1.0/datas?keywords=usa')
    datas = response.json()
    return render(request, 'concurrent_api/concurrent_api.html',{
        'datas':datas
    })
