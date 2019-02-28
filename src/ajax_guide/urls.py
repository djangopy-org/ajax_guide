
from django.contrib import admin
from django.urls import path
from app_1 import views as app1
from app_2 import views as app2


urlpatterns = [
    path('admin/', admin.site.urls),

    # app_1
    #FBV
    path('', app1.contactPage),
    path('ajax/contact', app1.postContact, name = 'contact_submit'),
    #CBV
    path('contact_cbv', app1.ContactAjax.as_view(), name = 'contact_submit_cbv'),

    #app_2
    path('user', app2.userPanel),
    path('ajax/get_user_info', app2.getUserInfo, name = 'get_user_info'),

]
