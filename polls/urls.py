# from django.conf.urls import url

# from . import views

# app_name = 'polls'
# urlpatterns = [
#     # e.g. /polls/
#     url(r'^$', views.index, name='index'),
#     # e.g. /polls/5/
#     # i.e. If the received URL matches this regex, call the views.detail function (view)
#     # Using parentheses around a pattern “captures” the text matched by that pattern and sends it as an argument to the view function
#     # ?P<question_id> defines the name that will be used to identify the matched pattern
#     url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#     # e.g. /polls/5/results/
#     url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#     # e.g. /polls/5/vote/
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
# ]


from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    # /polls/	(it will convert /poll to /polls/)
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /polls/31/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /polls/31/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # /polls/31/results/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
