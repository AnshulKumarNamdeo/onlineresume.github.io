from django.urls import path
from . import views
urlpatterns = [
    path('education/', views.eduview, name='education')
]