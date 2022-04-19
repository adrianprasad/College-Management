from unicodedata import name
from django import views
from django.urls import path
from.import views
urlpatterns =[
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('signup',views.signup,name='signup'),
    path('createuser',views.createuser,name='createuser'),
    path('about',views.about,name='about'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('addcour',views.addcour,name='addcour'),
    path('addteacher',views.addteacher,name='addteacher'),
    path('addtea',views.addtea,name='addtea'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('addstud',views.addstud,name='addstud'),
    path('show',views.show,name='show'),
    path('profile/<int:pk>/',views.profile,name='profile'),
    path('logout',views.logout,name='logout'),
    path('edit/<int:pk>/',views.edit,name='edit'),
    path('edit_stud/<int:pk>/',views.edit_stud,name='edit_stud'),
    path('delete_stud/<int:pk>/',views.delete_stud,name='delete_stud'),
]