from django.views.generic.base import TemplateView

class MainpageView(TemplateView):
    template_name = 'theme/main.html'