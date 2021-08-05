from django.contrib import admin
from django.urls import path
from intro.views import home_page,index,my_bio
from register.views import contact_us, delete_subject, get_subject, see_video, signup,login,logout_request,add_subject, upload_video


urlpatterns = [
    path('home', get_subject,name="index"),
    path('admin/', admin.site.urls),
    
    path("introduction",my_bio,name='bio_page'),
    path("",signup,name='signup_page'),
    path("login",login,name='login_page'),
    path("logout",logout_request,name='logout_page'),
    path("contact",contact_us,name='contact_page'),
    path("add_subject",add_subject,name='add_subject'),
    path("delete/<id>",delete_subject,name='delete_subject'),
    path("upload-video",upload_video,name='upload_video'),
    path("watch-video",see_video,name='see_video'),
    
]
