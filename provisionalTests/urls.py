from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('notes/',views.notes, name='notes'),
    path('test/',views.test, name='test'),
    path('marks/', views.marks, name='marks'),   
] 


 