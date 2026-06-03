from django.db import models
from django.utils.text import slugify


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('programming', 'Programming Languages'),
        ('ml', 'Machine Learning'),
        ('dl', 'Deep Learning & CV'),
        ('data', 'Data Processing'),
        ('tools', 'Tools & Platforms'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(default=80, help_text="Proficiency level (0-100)")
    icon = models.CharField(max_length=50, blank=True, help_text="Icon class name")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['category', 'order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Project(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('ongoing', 'Ongoing'),
        ('archived', 'Archived'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    technologies = models.CharField(max_length=300, help_text="Comma-separated technologies")
    github_url = models.URLField(blank=True)
    live_demo_url = models.URLField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed')
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    # Metrics
    accuracy = models.CharField(max_length=100, blank=True, help_text="e.g., 91.5% accuracy")
    metric_1_label = models.CharField(max_length=50, blank=True)
    metric_1_value = models.CharField(max_length=50, blank=True)
    metric_2_label = models.CharField(max_length=50, blank=True)
    metric_2_value = models.CharField(max_length=50, blank=True)
    
    date_completed = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-featured', 'order', '-date_completed']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=100)
    issue_date = models.DateField()
    credential_id = models.CharField(max_length=100, blank=True)
    credential_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='certifications/', blank=True, null=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-issue_date', 'order']
    
    def __str__(self):
        return f"{self.title} - {self.issuer}"


class Publication(models.Model):
    title = models.CharField(max_length=300)
    authors = models.CharField(max_length=300)
    conference = models.CharField(max_length=200)
    year = models.IntegerField()
    doi = models.CharField(max_length=100, blank=True)
    paper_url = models.URLField(blank=True)
    abstract = models.TextField()
    keywords = models.CharField(max_length=300)
    image = models.ImageField(upload_to='publications/', blank=True, null=True)
    
    class Meta:
        ordering = ['-year']
    
    def __str__(self):
        return self.title


class Experience(models.Model):
    EXPERIENCE_TYPE = [
        ('work', 'Work Experience'),
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
    ]
    
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    experience_type = models.CharField(max_length=20, choices=EXPERIENCE_TYPE, default='work')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text="Leave blank if current")
    description = models.TextField()
    achievements = models.TextField(blank=True, help_text="One achievement per line")
    
    class Meta:
        ordering = ['-start_date']
    
    @property
    def is_current(self):
        return self.end_date is None
    
    def __str__(self):
        return f"{self.title} at {self.organization}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"


class SiteConfiguration(models.Model):
    # Hero Section
    hero_title = models.CharField(max_length=200, default="Hi, I'm Varun")
    hero_subtitle = models.TextField(default="AI researcher, IEEE published developer, and someone who builds things that actually work.")
    hero_cta_text = models.CharField(max_length=50, default="View My Work")
    hero_video_url = models.URLField(blank=True, help_text="External video URL (YouTube, Vimeo, etc.)")
    hero_video_file = models.FileField(upload_to='videos/', blank=True, null=True, help_text="Or upload video file directly (MP4 recommended)")
    
    # About Section
    about_title = models.CharField(max_length=200, default="About Me")
    about_description = models.TextField(default="", blank=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    
    # Contact Info
    email = models.EmailField(default="varunnatesh10@gmail.com")
    phone = models.CharField(max_length=20, default="9740791782")
    location = models.CharField(max_length=100, default="Mysuru, Karnataka")
    linkedin_url = models.URLField(default="https://linkedin.com/in/varun-k-n-566135251")
    github_url = models.URLField(default="https://github.com/varunnatesh")
    
    # Resume
    resume_file = models.FileField(upload_to='resume/', blank=True, null=True)
    
    # SEO
    meta_description = models.CharField(max_length=160, blank=True)
    meta_keywords = models.CharField(max_length=300, blank=True)
    
    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configuration"
    
    def __str__(self):
        return "Site Configuration"
    
    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        self.pk = 1
        super().save(*args, **kwargs)
    
    @classmethod
    def get_config(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
