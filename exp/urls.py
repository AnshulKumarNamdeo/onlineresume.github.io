from django.urls import path
from . import views
urlpatterns = [
    path('experience/', views.WorkExp, name='experience')
]