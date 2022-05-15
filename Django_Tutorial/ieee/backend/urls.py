from django.urls import path
from .views import societies, event

urlpatterns = [
    path('societies/', societies, name="societies"),
    path('events/', event, name="events"),
]
