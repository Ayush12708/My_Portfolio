import os
import django
from datetime import date

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

from portfolio.models import Certification, Achievement

# NOTE: Uses get_or_create - will NOT overwrite existing admin entries.

# Populate Certifications (only if not already present)
Certification.objects.get_or_create(
    title='Java',
    defaults={
        'issuer': 'HackerRank',
        'date_issued': date(2025, 11, 1),
        'credential_url': ''
    }
)

Certification.objects.get_or_create(
    title='Fundamentals of Network Communication',
    defaults={
        'issuer': 'Coursera',
        'date_issued': date(2024, 9, 1),
        'credential_url': ''
    }
)

Certification.objects.get_or_create(
    title='Legacy Responsive Web Design V8',
    defaults={
        'issuer': 'freeCodeCamp',
        'date_issued': date(2023, 9, 1),
        'credential_url': ''
    }
)

# Populate Achievements (only if not already present)
Achievement.objects.get_or_create(
    title='Participated in "Code Off Duty" Web Hackathon (2024)',
    defaults={
        'organization': 'Coding Wise',
        'description': 'Demonstrated exceptional creativity, teamwork, and innovation in developing web-based solutions during a 2-day competitive hackathon.',
        'date': date(2024, 3, 1)
    }
)

print('Database population complete (existing entries preserved)!')
