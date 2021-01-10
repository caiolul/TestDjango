from django.urls import path
from myProject.core import views as v

urlpatterns = [
    path('', v.index, name='index'),
    path('post/<int:pk>', v.post_pg, name='post_pg'),
    path('post/new', v.post_new, name='post_new'),
    path('post/<int:pk>/edit', v.post_edit, name='post_edit'),
    path('register/', v.register_form, name='register_form'),
    path('login/', v.login_form, name='login_form'),
    path('logout/', v.LogoutRedirectViews.as_view(), name='logout_form'),
    path('api/', v.PostApi.as_view(), name='api_view'),
]

#curl -X POST http://127.0.0.1:8000/api/ -H 'content-type: application/json' -d '{"title": "Test api route", "text": "esse texto foi enviado pelo terminal", "description": "teste api via terminal"}'