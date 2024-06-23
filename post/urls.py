from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register("posts", views.PostViewSet)
router.register("comments", views.CommentViewSet)
router.register("votes", views.VoteViewSet)

urlpatterns = router.urls
urlpatterns += [
    path("popular/", views.PopularPostsListView.as_view()),
]
