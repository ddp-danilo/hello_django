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
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('hello/<nome>', views.hello),
    path('hello/<nome>/<int:idade>', views.hello),
    path('soma/<int:d1>/<int:d2>', views.soma),
    path('soma/<int:d1>', views.soma),
    path('multi/<int:d1>/<int:d2>', views.multi),
    path('multi/<int:d1>/', views.multi),
    path('divi/<int:d1>/<int:d2>', views.divi),
    path('divi/<int:d1>', views.divi),
    path('sub/<int:d1>/<int:d2>', views.sub),
    path('sub/<int:d1>', views.sub)
]
