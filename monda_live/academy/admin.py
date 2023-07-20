from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from . import models


@admin.register(models.CourseTopic)
class CourseTopicAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('__str__', 'order')
    list_filter = ('course', )


@admin.register(models.CourseGroup)
class CourseGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'starting_date', 'price')
    list_filter = ('course', )


@admin.register(models.CourseGroupMember)
class CourseGroupMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'price', 'paid')
    list_filter = ('course_group', 'is_student', 'is_lecturer', 'is_assistant', 'is_expert', 'is_recruiter')


@admin.register(models.TopicMaterial)
class TopicMaterialAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'topic', 'order', 'file')
    list_filter = ('topic', )


admin.site.register(models.Course)
admin.site.register(models.Topic)