from django.conf.urls import url
from wordtrainer.trainer_site.views import AppView


urlpatterns = (
        url(r'^$', AppView.as_view(), name='wordtrainer-app'),
        )
