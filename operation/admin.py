from django.contrib import admin

from operation.models import Add, Subtract, Multiply, Divide
# Register your models here.
admin.site.register(Add)
admin.site.register(Subtract)
admin.site.register(Multiply)
admin.site.register(Divide)
