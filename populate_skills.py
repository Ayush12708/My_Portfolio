import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

from portfolio.models import Skill

# Technical icon mapping
icons = {
    'python': 'fab fa-python',
    'c': 'fas fa-code',
    'c++': 'fas fa-code',
    'java': 'fab fa-java',
    'html': 'fab fa-html5',
    'css': 'fab fa-css3-alt',
    'javascript': 'fab fa-js',
    'mysql': 'fas fa-database',
    'aws': 'fab fa-aws',
    'docker': 'fab fa-docker',
    'linux': 'fab fa-linux',
}

# Update existing
for skill in Skill.objects.all():
    name_lower = skill.name.lower()
    if name_lower in icons:
        skill.icon_class = icons[name_lower]
        skill.save()

# Add soft skills extracted from resume
soft_skills = [
    ('Problem Analysis', 'fas fa-lightbulb'),
    ('Cross-Functional Teamwork', 'fas fa-users'),
    ('Project Coordination', 'fas fa-project-diagram'),
    ('Adaptable and Flexible Mindset', 'fas fa-sync-alt'),
]

for name, icon in soft_skills:
    Skill.objects.get_or_create(
        name=name,
        defaults={
            'category': 'soft',
            'proficiency': 100,
            'icon_class': icon
        }
    )

print("Skills updated successfully!")
