from django.urls import path
from . import views 

urlpatterns = [ 
    path('',views.home,name='home'),
    path('cadastrar/', views.cadastrar_medico, name='cadastrar'),
    path('listar/', views.listar, name='listar'),
    path('editar/<int:id/', views.editar, name='editar'),
    path('excluir/<int:id>/', views.excluir_medico, name='excluir'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
]