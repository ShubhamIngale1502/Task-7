from django.urls import  path
from .views import CreateFakeView, CreateAPI

urlpatterns = [
    path('add/',CreateFakeView.as_view()),
    path('show/',CreateAPI.as_view())
    
]
