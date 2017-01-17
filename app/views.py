import django.views.generic

class Home(django.views.generic.TemplateView):
    template_name = "index.html"
home = Home.as_view()