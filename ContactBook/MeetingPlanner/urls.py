from django.urls import path

from . import views


urlpatterns = [
    path("", views.get_planners, name="planners"),
    path("get_add_form/", views.get_add_form, name="get_add_form"),
    path("add_planner/", views.add_planner, name="add_planner"),
    path("list_view/", views.PlannerView.as_view(), name="list_view"),
    path("get_me_planners/", views.get_me_planners, name="get_me_planners"),
    path("meet_accept/<int:meet_id>/", views.accept_meet, name="accept"),
    path("reject_meet/<int:meet_id>/", views.reject_meet, name="reject"),
]