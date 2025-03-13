from django.db import models

# Create your models here.
class NavBar(models.Model):
    nav_item = models.CharField(max_length=100)
    nav_link = models.CharField(max_length=100)

    def __str__(self):
        return self.nav_item

class Background(models.Model):
    background_title = models.CharField(max_length=100)
    background_description = models.TextField()
    background_image = models.ImageField(upload_to='background_images/')
    activated = models.BooleanField(default=False)

    def __str__(self):
        return self.background_title

class About(models.Model):
    about_title = models.CharField(max_length=100)
    about_description = models.TextField()
    cv_file = models.FileField(upload_to='cv/')
    activated = models.BooleanField(default=False)

    def __str__(self):
        return self.about_title

class Service(models.Model):
    service_title = models.CharField(max_length=100)
    service_description = models.TextField()
    service_image = models.ImageField(upload_to='service_images/')
    activated = models.BooleanField(default=False)

    def __str__(self):
        return self.service_title

class PortfolioCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Portfolio(models.Model):
    portfolio_title = models.CharField(max_length=100)
    portfolio_description = models.TextField()
    portfolio_image = models.ImageField(upload_to='portfolio_images/')
    portfolio_category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return self.portfolio_title

class Testimonial(models.Model):
    testimonial_name = models.CharField(max_length=100)
    testimonial_description = models.TextField()
    testimonial_image = models.ImageField(upload_to='testimonial_images/')
    activated = models.BooleanField(default=False)

    def __str__(self):
        return self.testimonial_name

class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_description = models.TextField()
    blog_image = models.ImageField(upload_to='blog_images/')
    activated = models.BooleanField(default=False)

    def __str__(self):
        return self.blog_title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.TextField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    
    def __str__(self):
        return self.name

class ProfilePicture(models.Model):
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    