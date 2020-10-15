from django.urls import path
from . import views
from . import forms

urlpatterns = [
    
    #path('',views.HomeView.as_view(),name="home"),
    path('',views.index,name="index"),
    path('home/',views.index,name="home"),
    #path('ac/',views.ac,name=""),
    path('general/',views.ac_post,name=""),
    path('freezer/',views.general_post,name=""),
    path('icu/',views.icu_post),
    path('terms/',views.terms),
    path('blog/',views.blog,name='blog'),
    path('single_blog/<int:id>',views.single_blog,name='single_blog'),
    path('comment_delete/<int:id>',views.comment_delete,name="comment_delete"),
    #path('blog/<int:id>',views.blog_update),
    path('post',views.post,name='post'),
    path('post_update/<int:id>',views.post_update,name="post_update"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('rent_show',views.rent_show,name="rent_show"),
    path('rent_post',views.rent_post,name="rent_post"),
    path('rent/',views.rent,name="rent"),
    path('rent_update/<int:id>',views.rent_update,name="rent_update"),
    path('rent_delete/<int:id>',views.rent_delete,name="rent_delete"),
    path('contact',views.contact),
]