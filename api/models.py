from django.db import models

class Dispatch(models.Model):
    passenger_id = models.IntegerField
    driver_id = models.IntegerField
    address = models.CharField(max_length=100)
    assigned_at = models.DateTimeField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '[{}] {}'.format(self.passenger_id, self.address)