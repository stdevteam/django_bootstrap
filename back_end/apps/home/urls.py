from django.conf.urls import url
from django.views.generic import TemplateView


app_name = 'Users'

urlpatterns = [
    url(r'', TemplateView.as_view(template_name='home/home.html'), name='home'),
]

