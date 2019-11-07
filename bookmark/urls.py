from django.urls import path
from .views import bookmark_list_view, bookmark_create_view, bookmark_detail_view
app_name = "bookmark"

urlpatterns = [
    path("", bookmark_list_view, name="index"),
    path("create/", bookmark_create_view, name="create"),
    path("<int:pk>/bookmark/", bookmark_detail_view, name="detail"),
]
