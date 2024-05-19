from django.urls import path
from .views import PostTemplate,PostDetail,PostForm
app_name='myapp'
urlpatterns = [
    path('',PostTemplate.as_view(),name='index'),
    path('detail/<int:pk>/',PostDetail.as_view(),name='detail'),
    path('post/',PostForm.as_view(),name='post')
]