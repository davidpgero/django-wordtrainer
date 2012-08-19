# Make sure this code is called after $ is initialized.
# A tutorial suggested this was optional, but it isn't, since the "el"
# attributes are computed at class creation, not at instantiation.
$ ->
  class JQMPage extends Backbone.View
    go: =>
      $.mobile.changePage @$el


  class HomePage extends JQMPage
    el: $ 'homepage'
    initialize: ->
      _.bindAll @
    
  home_page = new HomePage

  class ListChoicePage extends JQMPage
    el: $ 'div#list-choice-page'
    update: =>
      list = @$el.find("ul#word-list-list")
      html = ""
      word_lists.each (word_list) =>
                name = word_list.get "name"
                id = word_list.get "id"
                html+= "<li><a href='' data-id='#{id}'>#{name}</a></li>"

      list.html(html)
      # JQM needs this to update a listview correctly
      try
        list.listview "refresh"
      catch error
        
        #list.listview()
      list.find("li a").each (i, a) => $(a).click((event) =>
        @choose($(event.target).attr "data-id" ))
    choose: (id) =>
      training_page.activate(id)

  class TrainingPage extends JQMPage
    el: $ 'div#training-page'
    prompt: $ 'div#prompt'
    response: $ 'input#response'
    initialize: =>
    activate: (id) =>
      @word_pairs = new WordPairs
      # Download Pairs of this word list
      @word_pairs_downloaded = false
      # Note to fellow coffeescript newbies:
      # make sure you get the indentation in .fetch right!
      @word_pairs.fetch(
                          data:
                            'word_list': id
                          success: =>
                            @word_pairs_downloaded = true
                            @update()
      )
      # Now get all TrainingItems for this list and for the logged in user
      @training_items = new TrainingItems
      @training_items_downloaded = false
      @training_items.fetch(
        data:
          'word_list': id
        success: =>
          @training_items_downloaded = true
          @update()
      )
      @prompt.text("Hello World")
      @go()

    update: =>
      if @training_items_downloaded and @word_pairs_downloaded
        @pair_ids = {}
        @word_pairs.each (pair, i) =>
          id = pair.get "id"
          @pair_ids[id] = pair
        @training_ids.each (item, i) =>
          id = item.get word_pair_id
        new_ids = []
        new_ids.push(id) if @training_ids[id]== undefined for id, pair of @pair_ids
        console.log("hello", new_ids)

    enqueue: =>
      # if @training_items.length < @word_pairs.length
      
    next: (id) =>
      if @training_items.length == 0 then @enqueue()
    

  class WordList extends Backbone.Model
    defaults:
      name:""
      description:""


  class WordLists extends Backbone.Collection
    model: WordList
    url: '/api/v1/word_list/'

  
  class WordPair extends Backbone.Model
    defaults:
      prompt: ""
      answer: ""

  class WordPairs extends Backbone.Collection
    model: WordPair
    url: '/api/v1/word_pair/'


  class TrainingItem extends Backbone.Model
    defaults:
      correct: 0
      mistakes: 0


  class TrainingItems extends Backbone.Collection
    model: TrainingItem
    url: '/api/v1/training_items/'

  
  window.word_lists = new WordLists
  window.list_choice_page = new ListChoicePage
  window.training_page = new TrainingPage
  word_lists.fetch(success:=> list_choice_page.update())
