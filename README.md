django-wordtrainer
==================

A vocabulary training site implemented in Django, using some novel ideas. Also usable as a plugabble app.

Built for the django-dash competition at http://djangodash.com

(Planned) Features:
* The admin staff manages the vocabulary
* Students can register and login
* "Continuous repetition"
* Nice support for mobile devices through JQuery Mobile


Continuous Repetition
====================

Conventional vocabulary sites/applications use spaced repetition. SR was originally invented as the Leitner Register Card system, where register cards would be sorted into buckets. Known cards are advanced one level, missed cards put down. Higher levels are reviewed less often.

More modern systems would try to guess the best time/day to review a word. This can get quite sophisticated but is completely besides the point. If you want to learn 100 words in one day, these systems just don't work.

Also, for more than a very few hundred words, the practicality of the system degrades rapidly.

This application be different. At any point in time it can query you with a word. The words are chosen at random, but with a random distribution reflecting how well the app thinks you know that card. This distribution is chosen to minimize short-time memory effects to the extent possible. The goal is to be able to learn a lot of words quickly, and repeat them whenever you feel like it. No fixed schedules!

Django Dash
====================

This project was originally started during the Django Dash 2012 competition.
The goal was to deliver a Djangoproject in 48 hours and make it all open source.

For me, the competition was quite a good excuse to explore coffeescript,
backbone.js and tastypie. The integration of all of these, however, took the
most time, and I wasn't able to produce a workable prototype in time. 

- JQuery mobile pages rendered into a single html file via a TemplateTag
- Pages can use template inheritance without requiring ajax requests for
  (relatively) static content
- API served via tastypie
- Integration with backbone
- Compiling and compressing all js and coffeescript dependencies into one big
  file


