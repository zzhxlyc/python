from django.conf.urls.defaults import patterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('user.views',
    (r'^list', 'list'),
    (r'^add', 'add'),
    (r'^doAdd', 'doAdd'),
)
