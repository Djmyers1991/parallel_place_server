"""
URL configuration for parallel_place project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from parallel_place_api.views import register_user, login_user
from rest_framework import routers
from parallel_place_api.views import Student_View, Teacher_View, Token_View, Vocab_Word_View, Discussion_Comment_View, Discussion_Topic_View, Assignment_Submission_View, Assignment_View, Inspiration_List_View, Character_List_View, UserView, About_The_Author_View

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'students', Student_View, 'student')
router.register(r'teachers', Teacher_View, 'teacher')
router.register(r'tokens', Token_View, 'token')
router.register(r'vocabwords', Vocab_Word_View, 'vocab')
router.register(r'discussioncomments', Discussion_Comment_View, 'discussioncomments')
router.register(r'discussiontopics', Discussion_Topic_View, 'discussiontopics')
router.register(r'submissions', Assignment_Submission_View, 'assignmentsubmissions')
router.register(r'assignments', Assignment_View, 'assignments')
router.register(r'inspirations', Inspiration_List_View, 'inspirationlist')
router.register(r'characters', Character_List_View, 'characterlist')
router.register(r'users', UserView, 'users')
router.register(r'abouttheauthors', About_The_Author_View, 'about_the_authors')






urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
