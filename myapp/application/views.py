from django.shortcuts import render,redirect
from application.models import conccurent
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView,TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import conccurent,config
from django.shortcuts import render

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserChangeForm

from application.forms import ConfigForm
import requests




    
    
"""
class conccurent(ListView):
    model = conccurent
"""
class ConfigList(ListView):
    model = config
class ConfigDetail(DetailView):
    model = config

def config(request):
	form=ConfigForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('index')
	return render(request,'application/config.html',{'form':form})






def home(request):
    response = requests.get('http://localhost:5000/conccurentList')
    datas = response.json()
    return render(request, 'concurrent_api/concurrent_api.html',{
        'datas':datas
    
    })

    
def ticket_class_view(request):
    dataset = conccurent.objects \
        .values('name') \
        .annotate(survived_count=Count('conccurent', filter=Q(survived=True)),
                  not_survived_count=Count('ticket_class', filter=Q(survived=False))) \
        .order_by('ticket_class')
    return render(request, 'ticket_class.html', {'dataset': dataset})


class chartView(TemplateView):
    template_name='application/charts.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["qs"]=conccurent.objects.all()
        return context

"""
def conccurent_config(request):
	args={'conccurent_config':request.user}
	return render(request,'application/conccurent_config.html',args)
"""