from django.urls import path
from django.views.generic import RedirectView


from . import views

#app_name = 'frontpage'

urlpatterns = [
    path('frontpage/', views.frontPage, name='frontpage-home'),
    path('', RedirectView.as_view(pattern_name='frontpage-home')),
]
