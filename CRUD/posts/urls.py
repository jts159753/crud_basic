from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', view=views.post_list, name='list'),
    path('<int:post_id>/', view=views.post_detail, name='detail'),
    path('create/', view=views.create_post, name='create'),
    path('<int:pk>/update', view=views.update_post, name='update'),
]
