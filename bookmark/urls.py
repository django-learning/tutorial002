from django.urls import path
from .views import bookmark_list_view
app_name = "bookmark"

urlpatterns = [
    path("", bookmark_list_view, name="index")
]
