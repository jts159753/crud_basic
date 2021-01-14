from django.urls import path
from . import views
urlpatterns = [
    path('', view=views.post_list, name='list'),
    path('<int:post_id>/', view=views.post_detail, name='detail')
]
