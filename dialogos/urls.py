from django.conf.urls.defaults import url, patterns, include, handler404, handler500


urlpatterns = patterns("dialogos.views",
    url(r"^comment/(?P<comment_id>.+?)/edit/$", "edit_comment",
        name="edit_comment"),
    url(r"^comment/(?P<comment_id>.+?)/delete/$", "delete_comment",
        name="delete_comment"),
    url(r"^comment/(?P<content_type_id>.+?)/(?P<object_id>.+?)/$", "post_comment",
        name="post_comment"),
)
