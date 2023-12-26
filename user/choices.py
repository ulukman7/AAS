from django.db import models


class TypeOfAward(models.TextChoices):
    administration = 'административная','административная'
    stateOwned = 'государственная', 'государственная'