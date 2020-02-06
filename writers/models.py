from django.db import models
from django.contrib.auth.models import User
import datetime
from core.models import Base

class Writer (Base):
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.name