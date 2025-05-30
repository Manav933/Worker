from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

class WorkerProduction(models.Model):
    MACHINE_CHOICES = [(i, f'Machine {i}') for i in range(1, 193)]
    
    # Basic fields
    name = models.CharField(max_length=100, verbose_name="Worker Name")
    machine_no = models.IntegerField(
        choices=MACHINE_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(192)],
        verbose_name="Machine Number"
    )
    date = models.DateField(verbose_name="Date")
    
    # Daily meter fields (Day 1 to Day 15)
    day_1_meter = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Day 1 Meter")
    day_2_meter = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Day 2 Meter")
    day_3_meter = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Day 3 Meter")
    day_4_meter = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Day 4 Meter")
    day_5_meter = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Day 5 Meter")
    day_6_meter = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Day 6 Meter")
    day_7_meter = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Day 7 Meter")
    day_8_meter = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Day 8 Meter")
    day_9_meter = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Day 9 Meter")
    day_10_meter = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Day 10 Meter")
    day_11_meter = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Day 11 Meter")
    day_12_meter = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Day 12 Meter")
    day_13_meter = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Day 13 Meter")
    day_14_meter = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Day 14 Meter")
    day_15_meter = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Day 15 Meter")
    
    # Rate per meter
    rate_per_meter = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0,
        verbose_name="Rate Per Meter"
    )
    
    # Auto-calculated fields
    total_meter = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        default=0,
        verbose_name="Total Meter (15 days)"
    )
    total_rate = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        default=0,
        verbose_name="Total Rate (15 days)"
    )
    avg_meter_per_day = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0,
        verbose_name="Average Meter Per Day"
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Worker Production Record"
        verbose_name_plural = "Worker Production Records"
        unique_together = ['name', 'machine_no', 'date']
        ordering = ['-date', 'name', 'machine_no']
    
    def save(self, *args, **kwargs):
        self.calculate_totals()
        super().save(*args, **kwargs)
    
    def calculate_totals(self):
        daily_meters = self.get_daily_meters_list()
        self.total_meter = sum(daily_meters)
        self.total_rate = self.total_meter * self.rate_per_meter
        self.avg_meter_per_day = self.total_meter / Decimal('15') if self.total_meter > 0 else Decimal('0')
    
    def get_daily_meters_list(self):
        return [
            self.day_1_meter, self.day_2_meter, self.day_3_meter, self.day_4_meter,
            self.day_5_meter, self.day_6_meter, self.day_7_meter, self.day_8_meter,
            self.day_9_meter, self.day_10_meter, self.day_11_meter, self.day_12_meter,
            self.day_13_meter, self.day_14_meter, self.day_15_meter
        ]
    
    def __str__(self):
        return f"{self.name} - Machine {self.machine_no} - {self.date}"
    
    @classmethod
    def get_worker_total_by_date(cls, worker_name, date):
        records = cls.objects.filter(name=worker_name, date=date)
        return sum(record.total_meter for record in records)
    
    @classmethod
    def get_worker_total_rate_by_date(cls, worker_name, date):
        records = cls.objects.filter(name=worker_name, date=date)
        return sum(record.total_rate for record in records)
    
    @classmethod
    def get_machine_daily_total(cls, machine_no, date):
        records = cls.objects.filter(machine_no=machine_no, date=date)
        return sum(record.total_meter for record in records)
