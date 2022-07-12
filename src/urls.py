from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name ="src"

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    
    path('login/', views.Login.as_view() ,name="login"),
    path('logout/', views.Logout.as_view() ,name="logout"),


    #Para los libros
    path('Libro_borrar/<int:pk>/', views.LibroEliminar.as_view() ,name="Libro_eliminar"),


    #Para pruebas
    path('pruebas/', views.pruebas ,name="pruebas"),
    path('registrar/', views.UsuariosCrear.as_view(), name ="registrar"),  

    #Para las apis
    #path('probando/', views.Probando ,name="probando"),
    path('api_login/', views.api_login ,name="api_login"),

    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

