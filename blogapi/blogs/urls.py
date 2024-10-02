from django.urls import path,include
from  .views import *


urlpatterns=[ path("blog/",BlogView.as_view()),
               path("",PublicBlogView.as_view()),
              
]