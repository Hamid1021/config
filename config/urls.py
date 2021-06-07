"""config URL Configuration

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
from django.urls import path, include

urlpatterns = [
    path('account/admin/', admin.site.urls),
    path('account/', include("account.urls", namespace="account")),
    path('', include("sitemap.urls", namespace="sitemap")),
]


from config import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.shortcuts import render
def View_404(request,exception):
    return render(request,"404.html",{})

def home(request):
    return render(request,"home.html",{})
urlpatterns += [
    path('', home),
]
def View_504(request,exception):
    return render(request,"504.html",{})

handler404 = "config.urls.View_404"
handler504 = "config.urls.View_504"
