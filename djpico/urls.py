from django.conf.urls import url

urlpatterns = [
    url(r'pico.js|client.js', 'djpico.views.picojs', name='picojs'),
    url(r'^.*$', 'djpico.views.index', name='index'),
]
