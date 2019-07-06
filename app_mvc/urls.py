from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^add-form/$', views.add_form, name='add-form'),
    url(r'^edit-form/$', views.edit_form, name='edit-form'),
    url(r'^delete-form/$', views.delete_form, name='delete-form'),

]