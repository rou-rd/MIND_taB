from django.urls import path
from product import views


app_name='product'

urlpatterns = [
    # [...]
    path('product.html', views.home, name='home'),

]
