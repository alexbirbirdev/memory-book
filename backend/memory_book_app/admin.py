from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    User,
    Veteran,
    MilitaryRank,
    BranchOfService,
    Conflict,
    Battle,
    Reward,
    VeteranReward,
    Article,
    Banner,
    Document,
    Event,
    News,
    Page,
    LogEntry
)


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone')}),
        ('Permissions', {
            'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'role'),
        }),
    )


class VeteranAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'veteran_type', 'birth_date', 'death_date', 'is_approved')
    list_filter = ('veteran_type', 'is_approved', 'military_rank', 'conflict')
    search_fields = ('last_name', 'first_name', 'middle_name')
    actions = ['approve_veterans', 'reject_veterans']
    readonly_fields = ('created_at', 'updated_at')

    def approve_veterans(self, _, queryset):
        queryset.update(is_approved=True)
    approve_veterans.short_description = "Одобрить выбранных ветеранов"

    def reject_veterans(self, _, queryset):
        queryset.update(is_approved=False)
    reject_veterans.short_description = "Отклонить выбранных ветеранов"


admin.site.register(User, CustomUserAdmin)
admin.site.register(Veteran, VeteranAdmin)
admin.site.register(MilitaryRank)
admin.site.register(BranchOfService)
admin.site.register(Conflict)
admin.site.register(Battle)
admin.site.register(Reward)
admin.site.register(VeteranReward)
admin.site.register(Article)
admin.site.register(Banner)
admin.site.register(Document)
admin.site.register(Event)
admin.site.register(News)
admin.site.register(Page)
admin.site.register(LogEntry)