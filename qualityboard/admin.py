from django.contrib import admin
from .models import DP,DPExternal,DPM,DPMExternal,MOB,MOBExternal,ImpactAreas,ImpactApplications,EDAPreviousMonth,EDACurrentMonth,EDALearnings

# Register your models here.

admin.site.register(DP)
admin.site.register(DPExternal)
admin.site.register(DPM)
admin.site.register(DPMExternal)
admin.site.register(MOB)
admin.site.register(MOBExternal)
admin.site.register(ImpactAreas)
admin.site.register(ImpactApplications)
admin.site.register(EDAPreviousMonth)
admin.site.register(EDACurrentMonth)
admin.site.register(EDALearnings)
