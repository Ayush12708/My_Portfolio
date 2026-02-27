import os
import django
from datetime import date

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

from portfolio.models import Education, ProfileLink

# Clear existing data for a clean slate
Education.objects.all().delete()
ProfileLink.objects.all().delete()

# Populate Education
Education.objects.create(
    institution='Lovely Professional University',
    degree='Bachelor of Technology; Computer Science and Engineering',
    score='CGPA: 7',
    start_date=date(2023, 8, 1),
    end_date=date(2027, 5, 1)  # Assuming a standard 4-year degree ending in the future
)

Education.objects.create(
    institution='Chinmaya Vidyalaya',
    degree='Intermediate',
    score='Percentage: 84.4',
    start_date=date(2020, 4, 1),
    end_date=date(2022, 3, 31)
)

Education.objects.create(
    institution="St. Joseph's School",
    degree='Matriculation',
    score='Percentage: 86.2',
    start_date=date(2018, 4, 1),
    end_date=date(2020, 3, 31)
)

# Populate Links
ProfileLink.objects.create(
    name='Email',
    url='mailto:kumarayush12708@gmail.com',
    icon_class='email'
)

ProfileLink.objects.create(
    name='GitHub',
    url='https://github.com/Ayush12708',
    icon_class='github'
)

ProfileLink.objects.create(
    name='LinkedIn',
    url='https://linkedin.com/in/ayush-kumar', # Assuming standard format, user can update in admin
    icon_class='linkedin'
)

print('Database successfully populated with Education and Links details!')
