from django.urls import path

from .api.category.CategoryLC.views import CategoryLCView
from .api.category.CategoryRUD.views import CategoryRUDView

from .api.tag.TagLC.views import TagLCView
from .api.tag.TagRUD.views import TagRUDView

from .api.article.ArticleCreate.views import ArticleCreateView
from .api.article.ArticleDelete.views import ArticleDeleteView
from .api.article.ArticleDetail.views import ArticleDetailView
from .api.article.ArticleList.views import ArticleListView
from .api.article.ArticleUpdate.views import ArticleUpdateView

from .api.comment.CommentCreate.views import CommentCreateView
from .api.comment.CommentDestroy.view import CommentDestroyView
from .api.comment.CommentList.views import CommentListView
from .api.comment.CommentRetrieve.views import CommentRetrieveView


app_name = 'article'

urlpatterns = [
    path('categorylc/', CategoryLCView.as_view(), name='categorylc'),
    path('categoryrud/<slug:slug>', CategoryRUDView.as_view(), name='categoryrud'),

    path('taglc/', TagLCView.as_view(), name='taglc'),
    path('tagrud/<slug:slug>', TagRUDView.as_view(), name='tagrud'),
    
    path('articlecreate/', ArticleCreateView.as_view(), name='articlecreate'),
    path('articledelete/<slug:slug>', ArticleDeleteView.as_view(), name='articledelete'),
    path('articledetail/<slug:slug>', ArticleDetailView.as_view(), name='articledetail'),
    path('articlelist/', ArticleListView.as_view(), name='articlelist'),
    path('articleupdate/<slug:slug>', ArticleUpdateView.as_view(), name='articleupdate'),

    path('commentcreate/', CommentCreateView.as_view(), name='comment_create'),
    path('commentdestroy/<int:pk>', CommentDestroyView.as_view(), name='comment_destroy'),
    path('commentlist/', CommentListView.as_view(), name='comment_list'),
    path('commentretrieve/<int:pk>', CommentRetrieveView.as_view(), name='comment_retrieve'),
]
