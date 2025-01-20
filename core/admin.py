from django.contrib import admin
from .models import PersonalInfo, Education, Experience, Certification, Skill, Technology, SocialLink, Sections, \
    Project, WP

admin.site.register(PersonalInfo)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Certification)
admin.site.register(Skill)
admin.site.register(Technology)
admin.site.register(SocialLink)
admin.site.register(Sections)
admin.site.register(Project)
admin.site.register(WP)
# Register your models here.
