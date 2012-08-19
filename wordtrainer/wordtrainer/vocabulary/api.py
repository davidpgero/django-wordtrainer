from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from wordtrainer.vocabulary.models import WordList, WordPair, TrainingItem
from django.conf import settings


class WordListResource(ModelResource):
    class Meta:
        limit = settings.WORDS_LIMIT
        max_limit = settings.WORDS_LIMIT
        queryset = WordList.objects.all()
        resource_name = 'word_list'
        authorization = DjangoAuthorization()


class WordPairResource(ModelResource):
    class Meta:
        limit = settings.WORDS_LIMIT
        max_limit = settings.WORDS_LIMIT
        limit = settings.WORDS_LIMIT
        queryset = WordPair.objects.all()
        resource_name = 'word_pair'
        authorization = DjangoAuthorization()

    def obj_create(self, bundle, request=None, **kwargs):
        return super(WordPairResource, self).obj_create(bundle, request, **kwargs)

    def dispatch(self, request_type, request, **kwargs):
        return super(WordPairResource, self).dispatch(request_type, request, **kwargs)

    def apply_authorization_limits(self, request, object_list):
        word_list = request.GET.get("word_list")
        return object_list.filter(word_list__id=word_list)


class TrainingItemResource(ModelResource):
    class Meta:
        limit = settings.WORDS_LIMIT
        max_limit = settings.WORDS_LIMIT
        limit = settings.WORDS_LIMIT
        queryset = TrainingItem.objects.all()
        resource_name = 'training_items'
        authorization = DjangoAuthorization()

    def obj_create(self, bundle, request=None, **kwargs):
        return super(TrainingItemResource, self).obj_create(bundle, request, **kwargs)

    def dispatch(self, request_type, request, **kwargs):
        return super(TrainingItemResource, self).dispatch(request_type, request, **kwargs)

    def apply_authorization_limits(self, request, object_list):
        word_list = request.GET.get("word_list")
        return object_list.filter(word_pair__word_list__id=word_list, user=request.user)
