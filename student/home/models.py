from django.db import models
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

def validate_max_date(value):
    if value > timezone.now().date():
        raise ValidationError(
            _('%(value)s is not a valid date. Date of birth cannot be in the future.'),
            params={'value': value},
        )
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(validators=[validate_max_date])
    physics_marks = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])
    chemistry_marks = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])
    maths_marks = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])
    cs_marks = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])

    def total_marks(self):
        return self.physics_marks + self.chemistry_marks + self.maths_marks + self.cs_marks

    def percentage(self):
        return (self.total_marks() / 400) * 100
