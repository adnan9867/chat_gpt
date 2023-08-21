"""ChatGPT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from ChatGPT.routing import websocket_urlpatterns
from .views import PrivacyPolicyView, DeployDjangoView, TestViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('talk_bot_privacy_policy/', PrivacyPolicyView.as_view(), name='privacy_policy'),
    path('deploy_django_using_pm2/', DeployDjangoView.as_view(), name='privacy_policy'),
    path('test-api/', TestViewSet.as_view({"get": "list"}), name='privacy_policy'),
]

urlpatterns += websocket_urlpatterns
