from django.urls import path

from . import views


# categories/<id>
urlpatterns = [
    # path('', views.home_view, name='home'),
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.about_view, name='about'),
    path('contacts/', views.contacts_view, name='contacts'),

    path('categories/<int:category_id>', views.get_articles_by_category, name='category_articles'),
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),

    path('login/', views.login_view, name='login'),
    path('registration/', views.registration_view, name='registration'),
    path('logout/', views.user_logout, name='logout'),

    path('article/create/', views.create_views, name='create'),
    path('article/myarticles/', views.myarticles, name='myarticles'),
    path('article/<int:pk>/update/', views.ArticleUpdateView.as_view(), name='update'),
    path('article/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='delete'),

    path('<str:obj_type>/<int:obj_id>/<str:action>/', views.add_vote, name='add_vote'),
    path('author/<str:username>', views.author_articles, name='author_articles'),
    path('search/', views.SearchResults.as_view(), name='search')


]