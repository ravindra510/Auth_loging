from django.urls import path
from account import views
urlpatterns = [
    path('registration/',views.UserRsgistertionView.as_view(),name="registration"),
]