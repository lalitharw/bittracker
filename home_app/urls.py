from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path('addhabit/',views.add_habit,name='addhabit'),
    path("create_profile/", views.create_profile, name="create_profile"),
    path("home/habit_info/<int:habitpk>/", views.habit_info, name="habit_info"),
    path("home/<int:habitpk>/edit/", views.edit_habit, name="edit_habit"),
    path("home/<int:habitpk>/delete/", views.delete_habit, name="delete_habit"),
    path("home/habit_info/<int:habitpk>/add_log/", views.add_log, name="add_log"),
    path('report/<int:id>/',views.see_report,name='report'),
    path('show_log/<int:id>/',views.show_log,name='show_log'),
    path('del_log/<int:id>/',views.del_log,name='del_log'), # type: ignore
    path('update_log/<int:id>/',views.update_log,name='update_user_log'),
    path('calendar/<int:id>/',views.display_calendar,name='calendar'),
    path('test/',views.test,name='tets'),
    path('all/<int:id>/',views.all_func,name='func'),
    path('con/',views.congraluations,name='cong')
]