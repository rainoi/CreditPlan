from django.contrib import admin
from planner.models import Major, MajorSubject, ElectiveSubject, GraduationCondition, GraudationConditionDetail, Timetable, TimetableDetail, Student

# Register your models here.
admin.site.register(Major)
admin.site.register(MajorSubject)
admin.site.register(ElectiveSubject)
admin.site.register(GraudationConditionDetail)
admin.site.register(GraduationCondition)
admin.site.register(Timetable)
admin.site.register(TimetableDetail)
admin.site.register(Student)

