from abc import ABC, abstractmethod
from collections.abc import Iterable
from datetime import timedelta
from typing import Any
from django.db import models
from django.forms import ValidationError


class BaseCharacter(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        abstract = True
        
        
class Mage(BaseCharacter):
    elemental_power = models.CharField(max_length=100)
    spellbook_type = models.CharField(max_length=100)
    
    
class Assassin(BaseCharacter):
    weapon_type = models.CharField(max_length=100)
    assassination_technique = models.CharField(max_length=100)
    
    
class DemonHunter(BaseCharacter):
    weapon_type = models.CharField(max_length=100)
    demon_slaying_ability = models.CharField(max_length=100)
    
    
class TimeMage(Mage):
    time_magic_mastery = models.CharField(max_length=100)
    temporal_shift_ability = models.CharField(max_length=100)
    
    
class Necromancer(Mage):
    raise_dead_ability = models.CharField(max_length=100)
    
    
class ViperAssassin(Assassin):
    venomous_strikes_mastery = models.CharField(max_length=100)
    venomous_bite_ability = models.CharField(max_length=100)
    
    
class ShadowbladeAssassin(Assassin):
    shadowstep_ability = models.CharField(max_length=100)
    
    
class VengeanceDemonHunter(DemonHunter):
    vengeance_mastery = models.CharField(max_length=100)
    retribution_ability = models.CharField(max_length=100)
    
    
class FelbladeDemonHunter(DemonHunter):
    felblade_ability = models.CharField(max_length=100)
    
    
class UserProfile(models.Model):
    username = models.CharField(max_length=75, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)
    
    
class Message(models.Model):
    sender = models.ForeignKey(to=UserProfile, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(to=UserProfile, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def mark_as_read(self):
        self.is_read = True
        
    def mark_as_unread(self):
        self.is_read = False
        
    def reply_to_message(self, reply_content, receiver):
        message = Message.objects.create(sender=self.receiver, receiver=receiver, content=reply_content)
        
        return message
    
    def forward_message(self, sender, receiver):
        massage = Message.objects.create(sender=sender, receiver=receiver, content=self.content)
        
        return massage
    

class StudentIDField(models.PositiveIntegerField):
    # def to_python(self, value: Any) -> Any:
    #     try:
    #         return int(value)
    #     except ValueError:
    #         pass
    pass

    

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = StudentIDField()


class MaskedCreditCardField(models.CharField):
    def to_python(self, value: Any) -> Any:
        if not isinstance(value, str):
            raise ValidationError("The card number must be a string")
        
        try:
            int(value)
        except ValueError:
            raise ValidationError("The card number must contain only digits")
        
        if len(value) != 16:
            raise ValidationError("The card number must be exactly 16 characters long")
        
        return f'****-****-****-{value[-4:]}'


class CreditCard(models.Model):
    card_owner = models.CharField(max_length=100)
    card_number = MaskedCreditCardField(max_length=20)


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)


class Room(models.Model):
    hotel = models.ForeignKey(to=Hotel, on_delete=models.CASCADE)
    number = models.CharField(max_length=100, unique=True)
    capacity = models.PositiveIntegerField()
    total_guests = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self) -> None:
        if self.total_guests > self.capacity:
            raise ValidationError("Total guests are more than the capacity of the room")

    def save(self, *args, **kwargs) -> str:
        self.clean()

        super().save(*args, **kwargs)

        return f"Room {self.number} created successfully"
    

class BaseReservation(models.Model):
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        abstract = True

    def reservation_period(self):
        return self.end_date.day - self.start_date.day
    
    def calculate_total_cost(self):
        result = self.reservation_period() * self.room.price_per_night
        return round(result, 1)
    
    def get_room_type(self):
        pass
    
    def save(self, *args, **kwargs) -> None:

        if self.start_date >= self.end_date:

            raise ValidationError("Start date cannot be after or in the same end date")

        if  self.__class__.objects.filter(end_date__gte=self.start_date, start_date__lte=self.end_date):
                
            raise ValidationError(f"Room {self.room.number} cannot be reserved")

        super().save(*args, **kwargs)

        return f"{self.get_room_type()} reservation for room {self.room.number}"
    

class RegularReservation(BaseReservation):
    def get_room_type(self):
        return "Regular"

class SpecialReservation(BaseReservation):
    def get_room_type(self):
        return "Special"
    
    def extend_reservation(self, days: int):

        try:
            self.end_date = self.end_date + timedelta(days=days)
            self.save()
        except ValidationError:
            raise ValidationError("Error during extending reservation")
        
        return f"Extended reservation for room {self.room.number} with {days} days"
    

    
    
        
    
