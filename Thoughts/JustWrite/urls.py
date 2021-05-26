from django.urls import path
from .import views

urlpatterns = [
    path('home/',views.home, name="home"),
    path('login/', views.login, name="login"),
    path('logout/', views.Logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('blog/', views.blog, name="blog"),
    path('about/', views.about, name="about"),
    path('profile/', views.profile, name="profile"),
    path('editprofile/',views.edit, name="edit"),
    path('poem/', views.poem, name="poem"),
    path('fblog/', views.fblog, name="fblog")
    
    
    
    
]
