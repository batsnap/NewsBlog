from django.urls import path
from . import views

urlpatterns = [
    # post views
    path('',views.main),
    path('sport/'                       ,views.category_post_list,{'slug':'sport'}),
    path('culture/'                     ,views.category_post_list,{'slug':'culture'}),
    path('finance/'                     ,views.category_post_list,{'slug':'finance'}),
    path('politics/'                    ,views.category_post_list,{'slug':'politics'}),
    path('technologies/'                ,views.category_post_list,{'slug':'technologies'}),
    
    path('sport/<slug:slug>/'           ,views.category_one_post),
    path('culture/<slug:slug>/'         ,views.category_one_post),
    path('finance/<slug:slug>/'         ,views.category_one_post),
    path('politics/<slug:slug>/'        ,views.category_one_post),
    path('technologies/<slug:slug>/'    ,views.category_one_post),
]