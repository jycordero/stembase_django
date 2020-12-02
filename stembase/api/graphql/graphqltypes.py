from graphene_django.types import DjangoObjectType
from stembase.api.models import *
from stembase.api.models import *
#TargetDemo, Level, Kind, Host, Discipline, Contact,Country,City,Province,Resource, Duration

class TargetDemoType(DjangoObjectType):
    class Meta:
        model = TargetDemo
class LevelType(DjangoObjectType):
    class Meta:
        model = Level
class KindType(DjangoObjectType):
    class Meta:
        model = Kind
class DisciplineType(DjangoObjectType):
    class Meta:
        model = Discipline
class ContactType(DjangoObjectType):
    class Meta:
        model = Contact
class HostType(DjangoObjectType):
    class Meta:
        model = Host
class CountryType(DjangoObjectType):
    class Meta:
        model = Country
class ProvinceType(DjangoObjectType):
    class Meta:
        model = Province
class CityType(DjangoObjectType):
    class Meta:
        model = City
class DurationType(DjangoObjectType):
    class Meta:
        model = Duration
class ResourceType(DjangoObjectType):
    class Meta:
        model = Resource
