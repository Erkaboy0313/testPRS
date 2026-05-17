from django.db import models

# Create your models here.
class Test(models.Model):
    
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        IN_PROGRESS = 'in_progress', 'In Progress'
        COMPLETED = 'completed', 'Completed'
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default='pending',choices=Status.choices)
    
    class Meta:
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['status']),
        ]
        permissions = [
            ('can_view_test', 'Can view test'),
            ('can_edit_test', 'Can edit test'),
        ]
        
    def __str__(self):
        return self.title
