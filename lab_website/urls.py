"""
URL configuration for lab_website project.

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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('home.urls')), # connect to chat app URLs
    # path('chat/', include('chat_model.urls')),  # Chat model page
    # path('synde-batch/', include('synde_batch.urls')), # SynDe Batch page
    # path("accounts/", include('accounts.urls')),  # User accounts management
    # path('circuit/', include('synde_cb.urls')),
] 

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# --- ✅ Serve plasmid design outputs during development ---
if settings.DEBUG:
    urlpatterns += static(
        '/synde_outputs/',
        document_root='/home/wenjun/lab_website_Agent/synde_outputs'
    )
    # --- ✅ Also serve MEDIA files (like IDT exports) ---
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
