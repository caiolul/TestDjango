from django.urls import path
from myProject.core import views as v

urlpatterns = [
    path('', v.index, name='index'),
    path('post/<int:pk>', v.post_pg, name='post_pg'),

]
