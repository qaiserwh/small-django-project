from django.urls import  path
from .import views

urlpatterns = [
     path('',views.admin_login, name='login' ),
     path('index',views.index, name='index' ),
     path('cardacc',views.cardacc, name='cardacc' ),
     path('emplist',views.emplist, name='emplist' ),
     path('admin/',views.admin,name='admin/'),
     path('front',views.front,name='front'),
     path('cardemp',views.cardemp, name='cardemp' )
    
]
