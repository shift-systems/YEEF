from django.urls import path
from .views import RegisterView
urlpatterns = [
    path('register', RegisterView.as_view()),
    # path('users/create/', views.user_list),
    # path('users/<int:pk>/', views.user_detail),

]
