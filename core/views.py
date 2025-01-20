from email._header_value_parser import Section
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.views.generic import TemplateView
from django.shortcuts import render

from .forms import ContactForm
from .models import PersonalInfo, Experience, Education, Certification, Skill, Sections, Project, SocialLink, WP


#@login_required
def portfolio_view(request):

    context = {
        'personal_info': PersonalInfo.objects.first(),
        'experiences': Experience.objects.all().order_by('-date_from'),
        'education': Education.objects.all().order_by('-date_from'),
        'certifications': Certification.objects.all().order_by('-date_obtained'),
        'skills': Skill.objects.all(),
        'Section':Sections.objects.all(),
        'project': Project.objects.all(),
        'Sociallink': SocialLink.objects.all(),
        'wps':WP.objects.first(),

    }

    return render(request, 'portfolio/index.html', context)

