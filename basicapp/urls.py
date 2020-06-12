from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("create/", views.create_new_record, name="create"),
    path("details/", views.get_all_the_records, name="details"),
    path("update/<pk>", views.update_the_record, name="update"),
    path("delete/<pk>", views.delete_the_record, name="delete"),
    path("key/", views.update_the_key, name="key"),
    path("get_value/", views.get_by_id, name="value"),
]
