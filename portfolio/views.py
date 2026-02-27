from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Skill, Experience, Education, ProfileLink, Certification, Achievement, ContactMessage

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            # Save to database
            ContactMessage.objects.create(name=name, email=email, message=message)
            
            # Send Email Notification via SMTP
            if getattr(settings, 'NOTIFY_EMAIL', None):
                try:
                    send_mail(
                        subject=f'New Portfolio Message from {name}',
                        message=f'You have a new message from your portfolio!\n\nName: {name}\nEmail: {email}\nMessage: {message}',
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[settings.NOTIFY_EMAIL],
                        fail_silently=True,
                    )
                except Exception:
                    pass

            messages.success(request, 'Your message has been sent successfully! I will get back to you soon.')
        else:
            messages.error(request, 'Please fill in all the required fields.')
            
        return redirect('index')

    projects = Project.objects.all().order_by('-created_at')
    backend_skills = Skill.objects.filter(category='backend').order_by('-proficiency')
    frontend_skills = Skill.objects.filter(category='frontend').order_by('-proficiency')
    tools_skills = Skill.objects.filter(category='tools').order_by('-proficiency')
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    links = ProfileLink.objects.all()
    certifications = Certification.objects.all()
    achievements = Achievement.objects.all()

    context = {
        'projects': projects,
        'backend_skills': backend_skills,
        'frontend_skills': frontend_skills,
        'tools_skills': tools_skills,
        'experiences': experiences,
        'educations': educations,
        'links': links,
        'certifications': certifications,
        'achievements': achievements,
    }
    return render(request, 'portfolio/index.html', context)
