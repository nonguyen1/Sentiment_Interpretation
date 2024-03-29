from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("devs/", hello.views.devs, name="devs"),
    path("admin/", admin.site.urls),
    path("ajax/handle_sentiment/", hello.views.handle_sentiment, name="handle_sentiment"),
    path("ajax/handle_emotion/", hello.views.handle_emotion, name="handle_emotion"),
    path("sent_data/", hello.views.sent_data, name="sent_data"),
    path("ajax/handle_phrase/", hello.views.handle_phrase, name="handle_phrase"),
    path("ajax/handle_phrase_emotion/", hello.views.handle_phrase_emotion, name="handle_phrase_emotion"),
]
