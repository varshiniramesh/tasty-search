from django.conf.urls import include, url

urlpatterns = [
    url(r'^tastysearch/', include('search.urls')),
]
