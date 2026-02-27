from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/projects/')
    technologies = models.CharField(max_length=200, help_text="e.g., Python, Django, AWS")
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    CATEGORY_CHOICES = (
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('tools', 'Tools & DevOps'),
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='backend')
    proficiency = models.IntegerField(default=50, help_text="Percentage out of 100")

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Leave blank if current role")

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.role} at {self.company}"

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    score = models.CharField(max_length=50, blank=True, null=True, help_text="CGPA or Percentage")
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        ordering = ['-end_date']

    def __str__(self):
        return f"{self.degree} from {self.institution}"

class ProfileLink(models.Model):
    name = models.CharField(max_length=100, help_text="e.g., GitHub, LinkedIn, Email")
    url = models.URLField()
    icon_class = models.CharField(max_length=100, blank=True, null=True, help_text="FontAwesome class or similar")

    def __str__(self):
        return self.name

class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    date_issued = models.DateField(blank=True, null=True)
    credential_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['-date_issued']

    def __str__(self):
        return f"{self.title} by {self.issuer}"

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    date = models.DateField(blank=True, null=True)
    credential_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} - {self.email}"
