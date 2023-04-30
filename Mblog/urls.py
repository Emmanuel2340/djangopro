from django.urls import path
from .views import BlogPost,Create,DeletePost,EditPost,PostDetail,MakeCategory,CategoryPage,Category_list




urlpatterns =[
    path('',BlogPost.as_view(), name='Post' ),
    path('blog',Create.as_view(), name='blog' ),
    path('delete/<int:pk>',DeletePost.as_view(), name='delete' ),
    path('post/<int:pk>',EditPost.as_view(), name='edit' ),
    path('detail/<int:pk>',PostDetail.as_view(), name='details' ),
    path('makecategory/',MakeCategory.as_view(), name='category' ),
    path('category/<str:cats>',CategoryPage, name='categorypage' ),
    path('category_list/',Category_list, name='cate' ),
 
]