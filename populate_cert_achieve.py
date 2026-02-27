import os
import django
from datetime import date

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

from portfolio.models import Certification, Achievement

# Clear existing data for a clean slate
Certification.objects.all().delete()
Achievement.objects.all().delete()

# Populate Certifications
Certification.objects.create(
    title='Java',
    issuer='HackerRank',
    date_issued=date(2025, 11, 1),
    credential_url='https://www.hackerrank.com/certificates/ayush_java'
)

Certification.objects.create(
    title='Fundamentals of Network Communication',
    issuer='Coursera',
    date_issued=date(2024, 9, 1),
    credential_url='https://www.coursera.org/verify/network-comm'
)

Certification.objects.create(
    title='Legacy Responsive Web Design V8',
    issuer='freeCodeCamp',
    date_issued=date(2023, 9, 1),
    credential_url='https://www.freecodecamp.org/certification/ayush/responsive-web-design'
)

# Populate Achievements
Achievement.objects.create(
    title='Participated in "Code Off Duty" Web Hackathon (2024)',
    organization='Coding Wise',
    description='Demonstrated exceptional creativity, teamwork, and innovation in developing web-based solutions during a 2-day competitive hackathon.',
    date=date(2024, 3, 1)
)

print('Database successfully populated with Certifications and Achievements!')
