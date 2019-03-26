from django.contrib import admin

from contact.models import TeamMember

# Register your models here.


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "email", "number", "status",)
