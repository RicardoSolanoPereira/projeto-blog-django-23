from django.urls import path
from blog.views import CategoryListViews, CreatedByListView, PageDetailView, PostDetailView, TagListViews, SearchListView, PostListView  # noqa

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post'),
    path('page/<slug:slug>', PageDetailView.as_view(), name='page'),
    path('created_by/<int:author_pk>',
         CreatedByListView.as_view(), name='created_by'),
    path('category/<slug:slug>', CategoryListViews.as_view(), name='category'),
    path('tag/<slug:slug>', TagListViews.as_view(), name='tag'),
    path('search/', SearchListView.as_view(), name='search'),
]
