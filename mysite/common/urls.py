from django.urls import path
from django.contrib.auth import views as auth_views
from .views import common_views, profile_views

app_name = 'common'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', common_views.signup, name='signup'),

    # profile
    path('profile/base/<int:user_id>/', profile_views.base, name='profile_base'),
    path('profile/question/<int:user_id>/', profile_views.question, name='profile_question'),
    path('profile/answer/<int:user_id>/', profile_views.answer, name='profile_answer'),
    path('profile/comment/<int:user_id>/', profile_views.comment, name='profile_comment'),
]