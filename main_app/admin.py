from django.contrib import admin
from models import Resume
from models import Qualification
from models import Experience
# Register your models here.


class ResumeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Resume, ResumeAdmin)


class QualificationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Qualification, QualificationAdmin)


class ExperienceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Experience, ExperienceAdmin)