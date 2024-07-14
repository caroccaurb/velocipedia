from django.contrib import admin
from .models import Bicicleta
from .models import Neumatico
from .models import Freno


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created' , 'update')


admin.site.register(Bicicleta, ProjectAdmin)
admin.site.register(Neumatico, ProjectAdmin)
admin.site.register(Freno, ProjectAdmin)