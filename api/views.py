from django.shortcuts import render
from .models import NavBar, Background, About, Service, PortfolioCategory, Portfolio, Testimonial, ProfilePicture

# Create your views here.
def homepage(request):
    nav_items = NavBar.objects.all()
    background = Background.objects.all()
    about = About.objects.filter(activated=True)
    services = Service.objects.filter(activated=True)
    portfolio_categories = PortfolioCategory.objects.all()
    portfolios = Portfolio.objects.filter(activated=True)
    testimonials = Testimonial.objects.filter(activated=True)
    profile_picture = ProfilePicture.objects.first()
    context = {
        'nav_items': nav_items,
        'background': background,
        'about': about,
        'services': services,
        'portfolio_categories': portfolio_categories,
        'portfolios': portfolios,
        'testimonials': testimonials,
        'profile_picture': profile_picture,
    }
    return render(request, 'index.html', context)
