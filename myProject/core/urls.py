from django.urls import path
from myProject.core import views as v

urlpatterns = [
    path('', v.index, name='index'),
    path('post/<int:pk>', v.post_pg, name='post_pg'),
    path('post/new', v.post_new, name='post_new'),
    path('post/<int:pk>/edit', v.post_edit, name='post_edit'),
    path('register/', v.register_form, name='register_form'),
    path('login/', v.login_form, name='login_form'),
    path('logout/', v.logout_form, name='logout_form'),
]
