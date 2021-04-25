from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$',views.PostListView.as_view(),name='post_list'),
    url(r'^about',views.AboutView.as_view(),name='about'),
    url(r'^post/(?P<pk>\d+)/$',views.PostDetailView.as_view(),name='post_detail'),
    url(r'^post/(?P<pk>\d+)/edit',views.PostUpdateView.as_view(),name='post_update'),
    url(r'^post/(?P<pk>\d+)/delete',views.PostDeleteView.as_view(),name='post_delete'),
    url(r'^post/create/$',views.PostCreateView.as_view(),name='post_create'),
    url(r'^draft',views.DraftView.as_view(),name='draft'),
    url(r'^post/(?P<pk>\d+)/comment',views.add_comment,name='comment'),
    url(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$',views.publish,name='post_publish')
]