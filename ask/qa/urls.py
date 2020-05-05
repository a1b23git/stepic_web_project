from django.urls import path
#from orders.views import test
from . import views

urlpatterns = [
    url(r'.*', views.test),
    ]
