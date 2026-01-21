from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ASSIGNED', 'Assigned'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
        ('REJECTED', 'Rejected'),
    ]

    customer_name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    provider = models.ForeignKey(Provider, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)


class BookingEvent(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    old_status = models.CharField(max_length=20)
    new_status = models.CharField(max_length=20)
    actor = models.CharField(max_length=20)  # customer/provider/admin/system
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True)
