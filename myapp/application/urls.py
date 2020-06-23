from django.urls import path
from application import views
from application.views import chartView

app_name='application'

urlpatterns = [
    # [...]
    path('conccurent_list.html', views.home, name='home'),
    ##path('conccurent_config.html', views.conccurent_config(), name='conccurent_config')
   	path('config.html',views.config,name='config'),
   	path('config_list.html', views.ConfigList.as_view(), name='config_list'),
   	path('charts.html',chartView.as_view(), name='charts'),

]
