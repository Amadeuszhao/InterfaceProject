from django.urls import re_path as url
from tutorials import views 
 
urlpatterns = [ 
    url(r'^api/tutorials$', views.tutorial_list),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^api/tutorials/published$', views.tutorial_list_published),
    url(r'^api/adversarial_attack$', views.adversarial_attack_generate),
    url(r'^api/adversarial_attack/(?P<pk>[0-9]+)$', views.adversarial_detail),
    url(r'^api/backdoor_attack$', views.backdoor_attack_generate),
    url(r'^api/backdoor_attack/(?P<pk>[0-9]+)$', views.backdoor_detail),
    url(r'^api/text_attack$', views.text_attack_generate),
    url(r'^api/text_attack/(?P<pk>[0-9]+)$', views.text_detail),
]