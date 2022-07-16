from multiprocessing.spawn import import_main_path
from django.urls import path
from .views import SignUpView

urlpatterns = [
  
  path('signup/', SignUpView.as_view(), name='signup'),
    
]
