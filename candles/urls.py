from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views as home_views
from registration import views as registerviews
from purchase import views as purchase_views
from payment import views as payment_views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', registerviews.register_form, name='register'),
    path('login/', registerviews.login_form, name='login'),
    path('logout/', registerviews.log_out, name='logout'),
    path('shop/<str:slug_url>', home_views.listing, name='listing'),
    path('purchase/', purchase_views.dashboard, name='dashboard'), 
    path('purchase/remove_product/', purchase_views.remove_basket),  
    path('purchase/submit_order/', payment_views.create_order, name='submit-order'),
    path('purchase/view_order/', payment_views.orders_page, name='view-order'),
    path('purchase/view_order/remove_order/', payment_views.remove_order),
    path('purchase/checkout/', payment_views.checkout, name='checkout'),
    path('purchase/checkout_success/<str:order_id>/', payment_views.paymentsuccess, name='success'),
    path('purchase/checkout_failed/<str:order_id>/', payment_views.paymentfailed, name='failed'),
    path('', home_views.home, name='home'),
    path('', include('paypal.standard.ipn.urls'))
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)