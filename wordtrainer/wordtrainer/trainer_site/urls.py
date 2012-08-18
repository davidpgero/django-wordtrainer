from django.conf.urls import url, include
from wordtrainer.trainer_site.views import AppView
from wordtrainer.vocabulary.api import WordListResource

word_list_resource = WordListResource()

urlpatterns = (
    url(r'^api/', include(word_list_resource.urls)),
    url(r'^$', AppView.as_view(), name='wordtrainer-app'),
)
