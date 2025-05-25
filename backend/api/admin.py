from django.contrib import admin
from .models import (
    SuspectList,
    MurderStat,
    Location,
    Detective,
    Trait,
    SuspectTrait,
    Statement
)

# Admin regisztrációk
admin.site.register(SuspectList)
admin.site.register(MurderStat)
admin.site.register(Location)
admin.site.register(Detective)
admin.site.register(Trait)
admin.site.register(SuspectTrait)
admin.site.register(Statement)