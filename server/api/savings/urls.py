from django.urls import path
from .views import SavingsView, AllSavingsView
urlpatterns = [
    path('savings', SavingsView.as_view()),
    path('all_savings', AllSavingsView.as_view()),

]
