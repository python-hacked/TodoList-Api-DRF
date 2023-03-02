from django.urls import path
from core import views
urlpatterns = [
    path('', views.Homeview, name='home'),
    path('detail/<str:pk>', views.DetailView, name='detail'),
    path('update/<str:pk>', views.UpdateView, name='update'),
    path('create/', views.CreateView, name='create'),
    path('delete/<str:pk>', views.DeleteView, name='delete'),
]