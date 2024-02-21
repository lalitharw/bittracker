from django.urls import path
from . import views
urlpatterns = [
    path('',views.forum_home,name='forum_home'),
    path('forum_info/<int:id>/',views.forumGroupInfo,name='group_info'),
    path("update_forum_log/<int:id>/",views.update_forum_log,name='update_forum_log'),
    path("previous_winner/",views.previous_winner,name='previous_winner')
]