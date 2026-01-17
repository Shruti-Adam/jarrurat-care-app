from django.db import models

class Volunteer(models.Model):
    SKILL_CHOICES = [
        ('medical', '👨‍⚕️ Medical Professional'),
        ('logistics', '🚚 Logistics Support'),
        ('tech', '💻 Tech Support'),
        ('counseling', '🧠 Counseling'),
        ('other', '✨ Other'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    skills = models.CharField(max_length=20, choices=SKILL_CHOICES)
    hours_per_week = models.IntegerField()
    motivation = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.get_skills_display()}"