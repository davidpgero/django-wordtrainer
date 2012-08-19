from tastypie.resources import ModelResource
from wordtrainer.vocabulary.models import WordList


class WordListResource(ModelResource):
    class Meta:
        queryset = WordList.objects.all()
        resource_name = 'word_list'
