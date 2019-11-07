from django.urls import path
from .views import bookmark_list_view, bookmark_create_view, bookmark_detail_view,bookmark_update_view, bookmark_delete_view
app_name = "bookmark"

urlpatterns = [
    path("", bookmark_list_view, name="index"),
    path("create/", bookmark_create_view, name="create"),
    path("<int:pk>/bookmark/", bookmark_detail_view, name="detail"),
    path("<int:pk>/update/", bookmark_update_view, name="update"),
    path("<int:pk>/delete/", bookmark_delete_view, name="delete"),
]
