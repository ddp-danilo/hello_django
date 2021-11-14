"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as viewscore
from senha import views as viewsenha
from django.views.generic import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url="/calc")),
    path('hello/', viewscore.hello),
    path('hello/<nome>', viewscore.hello),
    path('hello/<nome>/<int:idade>', viewscore.hello),
    path('calc/soma/<int:d1>/<int:d2>', viewscore.soma),
    path('calc/soma/<int:d1>', viewscore.soma),
    path('calc/multi/<int:d1>/<int:d2>', viewscore.multi),
    path('calc/multi/<int:d1>/', viewscore.multi),
    path('calc/divi/<int:d1>/<int:d2>', viewscore.divi),
    path('calc/divi/<int:d1>', viewscore.divi),
    path('calc/sub/<int:d1>/<int:d2>', viewscore.sub),
    path('calc/sub/<int:d1>', viewscore.sub),
    path('calc', viewscore.calc),
    path('cal_submit', viewscore.calc_submit),
    path('senha/', viewsenha.senha),
    path('senha/submit', viewsenha.senha_submit),
]
