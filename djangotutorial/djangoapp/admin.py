from django.contrib import admin
from .models import AppVarity, AppReview, Store, AppCertificate
# Register your models here.

class AppReviewInline(admin.TabularInline):
    model = AppReview
    extra = 2
class AppVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [AppReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('app_varities',)

class AppCertificateAdmin(admin.ModelAdmin):
    list_display = ('app', 'certificate_number')


admin.site.register(AppVarity, AppVarityAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(AppCertificate, AppCertificateAdmin)
