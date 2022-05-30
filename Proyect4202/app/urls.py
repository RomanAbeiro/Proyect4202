from django.urls import path
from .views import index, contacts, photos

urlpatterns = [
    path('', index, name="index"),
    path('contacts/', contacts, name="contacts"),
    path('photos/', photos, name="photos"),
]
