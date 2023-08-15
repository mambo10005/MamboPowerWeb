from django.urls import path

from .views import HomePageView, AboutPageView, TransformerPageView, LinePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("powersystemanalysis/transformer/", TransformerPageView.as_view(), name="transformer"),
    path("powersystemanalysis/line/", LinePageView.as_view(), name="line"),
]