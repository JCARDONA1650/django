from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .views import HomeView  # Importación de la vista HomeView
from blog.views import BlogListView  # Vista de la lista de blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),  # Página principal con HomeView
    # Incluye las URLs del blog
    path('blog/', include('blog.urls', namespace='blog')),
]
# Agregar django-browser-reload solo en modo desarrollo
if settings.DEBUG:
    urlpatterns += [path("__reload__/", include("django_browser_reload.urls"))]
