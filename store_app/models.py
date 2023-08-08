from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class StoreStatusChoice(models.TextChoices):
    Active = "ACTIVE"
    Inactive = "INACTIVE"


class Store(BaseModel):

    store_id = models.CharField(max_length=100, unique=True)
    """Unique id of different store"""

    timezone_str = models.CharField(max_length=100, default='America/Chicago')
    """Timezone in string where store is located"""

    def __str__(self) -> str:
        return self.store_id
    
class BusinessHour(BaseModel):
    DAY_CHOICES = [
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (0, 'Sunday'),
    ]

    store = models.ForeignKey(Store,on_delete=models.CASCADE,related_name='store_business_hours')
    """Store foreign key of store class"""
    
    day_of_week = models.IntegerField(choices=DAY_CHOICES)
    """Which days of a week store is open"""

    start_time_local = models.TimeField()
    """Store start time in local timezone"""
    
    end_time_local = models.TimeField()
    """Store end time in local timezone"""

    class Meta:
        unique_together = ('store', 'day_of_week')
        verbose_name = "Business Hour"

    def __str__(self) -> str:
        return f"{self.store} {self.day_of_week}"
    

class StoreStatus(BaseModel):
    """
        Status model to record about store status whether it is active or inactive
    """

    store = models.ForeignKey(Store,on_delete=models.CASCADE,related_name='status_status_updates')
    """Store foreign key of store class"""

    timestamp_utc = models.DateTimeField(db_index=True)
    """Time in utc timezone"""

    status = models.CharField(max_length=10, choices=StoreStatusChoice.choices)
    """Status choice of a store about it's active or inactive"""

    class Meta:
        unique_together = ('store', 'timestamp_utc')
        verbose_name = "Store Status"

    def __str__(self) -> str:
        return f"{self.store} : {self.status}"
    

class StoreReport(BaseModel):
    """
        Report model of a store to collect all data of a store about it's opening and closing.
    """
    store = models.ForeignKey(Store,on_delete=models.CASCADE,related_name='store_reports')
    """Store foreign key of store class"""

    uptime_last_hour = models.BigIntegerField()
    """Last uptime of store in minutes"""

    uptime_last_day = models.BigIntegerField()
    """Last uptime day of store in hours"""

    uptime_last_week = models.BigIntegerField()
    """Last uptime week of store in hours"""

    downtime_last_hour = models.BigIntegerField()
    """Last down time of store in minutes"""

    downtime_last_day = models.BigIntegerField()
    """Last down day of store in hours"""

    downtime_last_week = models.BigIntegerField()
    """Last down week of store in hours"""


    def __str__(self) -> str:
        return f"{self.store} : {self.uptime_last_day} : {self.downtime_last_day}"