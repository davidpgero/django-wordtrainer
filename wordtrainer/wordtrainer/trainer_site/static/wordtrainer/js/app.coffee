class HomePage extends Backbone.View
  el: $ 'homepage'
  initialize: ->
    _.bindAll @

    
home_page = new HomePage

class ListChoicePage extends Backbone.View
  el: $ '#list-choice-page'
  initialize: ->
    word_lists.bind('fetch', @update)
  update: =>
    list = @el.find("div#word-list-list")
    list.html()


class WordList extends Backbone.Model
  defaults:
    name:""
    description:""

class WordLists extends Backbone.Collection
  model: WordList
  url: '/api/word_list/'

window.word_lists = new WordLists
word_lists.fetch(success:=> list_choice_page.update())
window.list_choice_page = new ListChoicePage
