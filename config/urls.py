"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import redirect_to_swagger
from django.conf.urls.static import static
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path("admin/", admin.site.urls),
    
    path('', redirect_to_swagger, name='redirect-to-swagger'),
    
    path('api/base/', SpectacularAPIView.as_view(), name='base'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='base'), name='swagger-doc'),
    
    path('', include('authentication.urls')),
    path('', include('article.urls')),
    path('', include('contactus.urls')),
    path('', include('event.urls')),
    path('', include('gallery.urls')),
    path('', include('job_opportunity.urls')),
    path('', include('personnel.urls')),
    path('', include('questions.urls')),
    path('', include('sample_question.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)