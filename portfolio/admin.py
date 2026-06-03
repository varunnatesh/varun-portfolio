from django.contrib import admin
from .models import (
    Skill, Project, Certification, Publication, 
    Experience, Contact, SiteConfiguration
)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_filter = ['category']
    search_fields = ['name']
    list_editable = ['proficiency', 'order']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'featured', 'date_completed', 'order']
    list_filter = ['status', 'featured', 'date_completed']
    search_fields = ['title', 'description', 'technologies']
    list_editable = ['featured', 'order']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'short_description', 'description', 'image')
        }),
        ('Technical Details', {
            'fields': ('technologies', 'github_url', 'live_demo_url', 'status')
        }),
        ('Metrics', {
            'fields': (
                'accuracy',
                ('metric_1_label', 'metric_1_value'),
                ('metric_2_label', 'metric_2_value')
            )
        }),
        ('Display Settings', {
            'fields': ('featured', 'order', 'date_completed')
        }),
    )


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'issuer', 'issue_date', 'order']
    list_filter = ['issuer', 'issue_date']
    search_fields = ['title', 'issuer']
    list_editable = ['order']


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'conference', 'year']
    list_filter = ['year', 'conference']
    search_fields = ['title', 'authors', 'abstract']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'organization', 'experience_type', 'start_date', 'end_date', 'is_current']
    list_filter = ['experience_type', 'start_date']
    search_fields = ['title', 'organization', 'description']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    list_editable = ['is_read']
    readonly_fields = ['created_at']


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle', 'hero_cta_text', 'hero_video_file', 'hero_video_url'),
            'description': 'Upload a video file OR provide an external URL (file takes priority)'
        }),
        ('About Section', {
            'fields': ('about_title', 'about_description', 'profile_image')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location', 'linkedin_url', 'github_url')
        }),
        ('Resume', {
            'fields': ('resume_file',)
        }),
        ('SEO', {
            'fields': ('meta_description', 'meta_keywords')
        }),
    )
    
    def has_add_permission(self, request):
        # Only allow one configuration
        return not SiteConfiguration.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of configuration
        return False
