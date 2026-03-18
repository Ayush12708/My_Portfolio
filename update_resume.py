import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

from portfolio.models import UserProfile

if __name__ == "__main__":
    profile = UserProfile.objects.first()
    if not profile:
        profile = UserProfile.objects.create()
    
    resume_path = '/Users/ayushkumar/Desktop/portfolio_workspace/resume.pdf'
    if os.path.exists(resume_path):
        with open(resume_path, 'rb') as f:
            profile.resume_file.save('resume.pdf', File(f), save=True)
            print("Successfully uploaded Resume PDF directly to the database backend!")
    else:
        print("Resume PDF not found.")
