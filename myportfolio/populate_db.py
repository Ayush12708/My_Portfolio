import os
import django
from datetime import date

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

from portfolio.models import Skill, Project, Experience

# Clear existing data for a clean slate
Skill.objects.all().delete()
Project.objects.all().delete()
Experience.objects.all().delete()

# Populate Skills
skills_data = [
    ('Python', 'backend', 85),
    ('C', 'backend', 70),
    ('C++', 'backend', 75),
    ('Java', 'backend', 70),
    ('HTML', 'frontend', 85),
    ('CSS', 'frontend', 80),
    ('JavaScript', 'frontend', 80),
    ('MySQL', 'tools', 80),
    ('AWS', 'tools', 75),
    ('Docker', 'tools', 60),
    ('Linux', 'tools', 70),
]
for name, category, proficiency in skills_data:
    Skill.objects.create(name=name, category=category, proficiency=proficiency)

# Populate Projects (Excluding the 2nd project)
Project.objects.create(
    title='BASTION - Cloud-Based File Management System',
    description='Designed and developed a secure full-stack web application for file sharing with role-based access control (Admin/User).\n\n• Built responsive frontend pages using HTML, CSS, and JavaScript with client-side validation.\n• Developed backend using Django with MongoDB for storing user credentials and metadata.\n• Enabled Admin-controlled user management and access control.\n• Integrated AWS S3 for secure file storage and AWS EC2 for application deployment.',
    technologies='Python, Django, MongoDB, AWS S3, HTML, CSS, JavaScript, EC2',
    github_link='https://github.com/Ayush12708/Bastion-cloud_based_Storage_system',
)

# Populate Experience (Trainings)
Experience.objects.create(
    company='Lovely Professional University',
    role='Data Structures and Algorithms using C++',
    description='Completed a 6-week intensive training in Data Structures and Algorithms using C++.\n\n• Gained hands-on experience with arrays, linked lists, stacks, queues, trees, recursion, and hashing.\n• Developed a C++-based Library Management System using multiple data structures.',
    start_date=date(2025, 6, 1),
    end_date=date(2025, 7, 31)
)

Experience.objects.create(
    company='InternsElite',
    role='Web Development Training',
    description='Completed structured industrial training in Web Development.\n\n• Trained in building responsive layouts, form validation, animations, and interactive web elements.\n• Improved understanding of MVC concepts, API basics, and real-world website architecture.',
    start_date=date(2024, 1, 1),
    end_date=date(2024, 2, 28)
)

print('Database successfully populated with Resume details (excluding 2nd project)!')
