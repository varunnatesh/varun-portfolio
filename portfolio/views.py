from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import (
    Project, Skill, Certification, Publication, 
    Experience, Contact, SiteConfiguration
)


def home(request):
    """Homepage with hero, featured projects, and skills"""
    config = SiteConfiguration.get_config()
    featured_projects = Project.objects.filter(featured=True, status='completed')[:3]
    skills = Skill.objects.all()
    certifications = Certification.objects.all()[:4]
    publications = Publication.objects.all()
    
    # Group skills by category
    skills_by_category = {}
    for skill in skills:
        category = skill.get_category_display()
        if category not in skills_by_category:
            skills_by_category[category] = []
        skills_by_category[category].append(skill)
    
    context = {
        'config': config,
        'featured_projects': featured_projects,
        'skills_by_category': skills_by_category,
        'certifications': certifications,
        'publications': publications,
    }
    return render(request, 'portfolio/home.html', context)


def projects(request):
    """All projects page with filtering"""
    config = SiteConfiguration.get_config()
    status_filter = request.GET.get('status', 'all')
    
    if status_filter == 'all':
        projects_list = Project.objects.all()
    else:
        projects_list = Project.objects.filter(status=status_filter)
    
    paginator = Paginator(projects_list, 9)  # 9 projects per page
    page_number = request.GET.get('page')
    projects_page = paginator.get_page(page_number)
    
    context = {
        'config': config,
        'projects': projects_page,
        'status_filter': status_filter,
    }
    return render(request, 'portfolio/projects.html', context)


def project_detail(request, slug):
    """Individual project detail page"""
    config = SiteConfiguration.get_config()
    project = get_object_or_404(Project, slug=slug)
    
    # Get related projects (same technologies)
    tech_list = [t.strip() for t in project.technologies.split(',')]
    related_projects = Project.objects.exclude(id=project.id).filter(
        technologies__icontains=tech_list[0] if tech_list else ''
    )[:3]
    
    context = {
        'config': config,
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'portfolio/project_detail.html', context)


def about(request):
    """About page with experience and education"""
    config = SiteConfiguration.get_config()
    experiences = Experience.objects.all()
    certifications = Certification.objects.all()
    
    context = {
        'config': config,
        'experiences': experiences,
        'certifications': certifications,
    }
    return render(request, 'portfolio/about.html', context)


def contact(request):
    """Contact page with form"""
    config = SiteConfiguration.get_config()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    context = {
        'config': config,
    }
    return render(request, 'portfolio/contact.html', context)


def research(request):
    """Research and publications page"""
    config = SiteConfiguration.get_config()
    publications = Publication.objects.all()
    
    context = {
        'config': config,
        'publications': publications,
    }
    return render(request, 'portfolio/research.html', context)
