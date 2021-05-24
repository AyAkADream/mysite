from django.urls import path
from study import views

urlpatterns = [
    path('', views.StudyIndexView.as_view(), name='study_index'),
    path('post/<int:pk>', views.StudyPostDetailView.as_view(), name='study_post_detail'),
    path('post/new/', views.StudyCreatePostView.as_view(), name='study_post_new'),
    path('post/<int:pk>/edit/', views.StudyPostEditView.as_view(), name='study_post_edit'),
    path('post/<int:pk>/delete/', views.StudyPostDeleteView.as_view(), name='study_post_delete'),
]