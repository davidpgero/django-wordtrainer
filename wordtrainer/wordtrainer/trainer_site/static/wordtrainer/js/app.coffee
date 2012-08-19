# Make sure this code is called after $ is initialized.
# A tutorial suggested this was optional, but it isn't, since the "el"
# attributes are computed at class creation, not at instantiation.
$ ->
  class HomePage extends Backbone.View
    el: $ 'homepage'
    initialize: ->
      _.bindAll @
    
  home_page = new HomePage

  class ListChoicePage extends Backbone.View
    el: $ 'div#list-choice-page'
    initialize: =>
      1
    update: =>
      list = @$el.find("ul#word-list-list")
      html = ""
      word_lists.each (word_list) =>
                name = word_list.get "name"
                id = word_list.get "id"
                html+= "<li><a href='' data-id='#{id}'> #{name}</a></li>"

      list.html(html)
      # JQM needs this to update a listview correctly
      list.listview "refresh"


  class WordList extends Backbone.Model
    defaults:
      name:""
      description:""


  class WordLists extends Backbone.Collection
    model: WordList
    url: '/api/word_list/'

  window.word_lists = new WordLists
  window.list_choice_page = new ListChoicePage
  word_lists.fetch(success:=> list_choice_page.update())
