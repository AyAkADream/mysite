from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(),name='indexHome'),
    path('index/<int:pk>', views.SkillView.as_view(),name='skill'),
    path('detail/<int:pk>', views.DetailView.as_view(),name='detail'),
    path('about/', views.AboutView.as_view(),name='about'),
    path('dream/', views.DreamView.as_view(),name='dream'),
    path('contact/', views.ContactView.as_view(),name='contact'),
    path('thanks/', views.ThanksView.as_view(),name='thanks')
]
