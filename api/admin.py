from django.contrib import admin
from .models import User, Department, Doctor, Patient, Prescription, admin_doc

admin.site.register(User)
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Prescription)
admin.site.register(admin_doc)

# @admin.register(User)
# class admin_doc(admin.ModelAdmin):
#     list_display = ('id', 'name', 'email', 'password')
