from django.urls import path

from . import views

def trigger_error(request):
    division_by_zero = 1 / 0
    
app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('sentry-debug/', trigger_error),
] 
