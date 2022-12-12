
from django.urls import path
from . import views

app_name = 'Pizzas'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('comments/<int:pizza_id>/',views.comments,name='comments'),
    path('pizzas',views.pizzas,name='pizzas'),
    path('pizzas/<int:pizza_id>/',views.pizza,name='pizza'),
    ]
    