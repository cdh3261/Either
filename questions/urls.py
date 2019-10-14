from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    path('',views.index, name='index'),
    path('create/',views.create, name='create'),

    path('<int:id>/',views.detail, name='detail'),
    path('<int:id>/update/',views.update, name='update'),

    path('<int:id>/delete/',views.delete, name='delete'),

    path('<int:id>/answer_create/',views.answer_create, name='answer_create'),
    path('<int:question_id>/answer/<int:answer_id>/update',views.answer_update, name='answer_update'),
    path('<int:question_id>/answer/<int:answer_id>/delete',views.answer_delete, name='answer_delete'),

    path('search/',views.search, name='search')
]
