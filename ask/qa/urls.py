from django.urls import path
from orders.views import test

urlpatterns = [
    path('/', test),
    path('/login/', test),
    path('/signup/', test),
    path('/question/<123>/', test),
    path('/ask/', test),
    path('/popular/', test),
    path('/new/', test)
    ]
