from django.conf.urls import url
from template_app_vs import views

# TEMPLATE TAGGING
app_name = 'template_app_vs'

urlpatterns= [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
    ]