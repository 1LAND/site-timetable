from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(User)
admin.site.register(LearningPlace)
admin.site.register(LearningPlaceClasses)
admin.site.register(LearningPlaceClassUser)
admin.site.register(LearningPlacetTimetable)
admin.site.register(LearningPlaceTimetableLesson)