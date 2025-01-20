from django.db import models
choice={
    'Personal Information':'Personal Information',
    'Project':'Project',
    'Experience':'Experience',
    'Education':'Education',
    'Certification':'Certification',
    'Skills':'Skills',
    'Technology':'Technology',
}

class PersonalInfo(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    linkedin = models.URLField()
    summary = models.TextField()
    profile_image = models.ImageField(upload_to='profile', null=True, blank=True)
    title = models.CharField(max_length=200)
    about_me = models.TextField()
    resume = models.FileField(upload_to='resume', null=True, blank=True)

class Experience(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_from = models.DateField()
    date_to = models.DateField(null=True, blank=True)

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    date_from = models.DateField()
    date_to = models.DateField(null=True, blank=True)
    description = models.TextField()

class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=100)
    date_obtained = models.DateField()

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects')
    live_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

class WP(models.Model):
    image = models.ImageField(upload_to='wallpaper')

class Technology(models.Model):
    name = models.CharField(max_length=100)
    projects = models.ManyToManyField(Project, related_name='technologies')

class SocialLink(models.Model):
    platform = models.CharField(max_length=50)
    url = models.URLField()
    icon = models.CharField(max_length=50)

class Sections(models.Model):
    choices=models.CharField(max_length=200,choices=choice)

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    def __str__(self):
        return self.name