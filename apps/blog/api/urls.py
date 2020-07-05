from django.urls import path

from apps.blog.api.views import(
    api_detail_blog_view
)

app_name = 'blog'

urlpatterns = [
    path('<slug>/', api_detail_blog_view, name="detail"),
]