from django.urls import path
from .views import demo_plot_view


urlpatterns = [
    path('demo-plot/', demo_plot_view),
]
