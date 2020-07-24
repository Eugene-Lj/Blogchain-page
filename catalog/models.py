from django.db import models



class Procurement(models.Model):
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    title = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.title

class ProcurementFiles(models.Model):
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    procurement = models.ForeignKey(Procurement, on_delete=models.CASCADE, related_name='file')
    
