from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class LinePageView(TemplateView):
    template_name = "line.html"

class TransformerPageView(TemplateView):
    template_name = "transformer.html"
