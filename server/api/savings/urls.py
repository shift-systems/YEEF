from django.urls import path
from .views import SavingsView
urlpatterns = [
    path('requestpay', SavingsView.as_view()),

]
