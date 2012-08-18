from django.contrib import admin
from wordtrainer.vocabulary.models import WordList, WordPair


class WordPairInlineAdmin(admin.TabularInline):
    model = WordPair
    extra = 20


class WordListAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_editable = ["name"]
    inlines = [WordPairInlineAdmin]


class WordPairAdmin(admin.ModelAdmin):
    list_display = ["id", "prompt", "answer"]
    list_editable = ["prompt", "answer"]


admin.site.register(WordList, WordListAdmin)
admin.site.register(WordPair, WordPairAdmin)
