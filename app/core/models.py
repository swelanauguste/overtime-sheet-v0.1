import datetime
from decimal import Decimal

from django.db import models
from django.urls import reverse

TIME_HALF = 1.5
DOUBLE_TIME = 2.0
DOUBLE_TIME_HALF = 2.5
TRIPLE_TIME = 3.0

MULTIPLIER_CHOICES = (
    (TIME_HALF, "1.5"),
    (DOUBLE_TIME, "2.0"),
    (DOUBLE_TIME_HALF, "2.5"),
    (TRIPLE_TIME, "3.0"),
)


class Overtime(models.Model):
    reason = models.CharField(max_length=255)
    start_date = models.DateField(default=datetime.datetime.now, blank=True)
    start_time = models.TimeField(default=datetime.time(16, 30))
    end_date = models.DateField(default=datetime.datetime.now, blank=True)
    end_time = models.TimeField(default=datetime.time(16, 30))
    multiplier = models.DecimalField(
        max_digits=10, decimal_places=2, choices=MULTIPLIER_CHOICES, default=TIME_HALF
    )
    hourly_rate = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    salary = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    hours = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("ot-detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if not self.hourly_rate:
            self.hourly_rate = (self.salary * 12) / 1950
        if not self.hours:
            self.hours = self.get_hours
        super(Overtime, self).save(*args, **kwargs)

    @property
    def get_hours(self):
        FMT = "%H:%M"
        st = self.start_time.hour * 60
        et = self.end_time.hour * 60
        hours = et - st
        return hours / 60

    def calculate_overtime(self):
        over_time = self.multiplier * self.hourly_rate * Decimal(self.get_hours)
        return f"${'%.2f' % over_time}"

    def __str__(self):
        return f"{self.get_hours}"
