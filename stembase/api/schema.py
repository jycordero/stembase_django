import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from stembase.api.graphql.graphqltypes import *
from stembase.api.graphql.graphqlinputs import *
from stembase.api.graphql.graphqlcreates import *
from stembase.api.graphql.graphqlupdates import *
from stembase.api.models import *


class Query(ObjectType):
    targetdemo = graphene.Field(TargetDemoType,id=graphene.Int())
    level = graphene.Field(LevelType,id=graphene.Int())
    kind = graphene.Field(KindType,id=graphene.Int())
    discipline = graphene.Field(DisciplineType,id=graphene.Int())
    contact = graphene.Field(ContactType,id=graphene.Int())
    host = graphene.Field(HostType,id=graphene.Int())
    country = graphene.Field(CountryType,id=graphene.Int())
    province = graphene.Field(ProvinceType,id=graphene.Int())
    city = graphene.Field(CityType,id=graphene.Int())
    duration = graphene.Field(DurationType,id=graphene.Int())
    resource = graphene.Field(ResourceType,id=graphene.Int())

    targetdemos = graphene.List(TargetDemoType)
    levels = graphene.List(LevelType)
    kinds = graphene.List(KindType)
    disciplines = graphene.List(DisciplineType)
    contacts = graphene.List(ContactType)
    hosts = graphene.List(HostType)
    countrys = graphene.List(CountryType)
    provinces = graphene.List(ProvinceType)
    citys = graphene.List(CityType)
    durations = graphene.List(DurationType)
    resources = graphene.List(ResourceType)

    def resolve_targetdemo(self,info,**kwargs):
        id = kwargs.get('id')
        if id is not None:
            return TargetDemo.objects.get(pk=id)
        return None

    def resolve_level(self,info,**kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Level.objects.get(pk=id)
        return None

    def resolve_kind(self,info,**kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Kind.objects.get(pk=id)
        return None

    def resolve_discipline(self,info,**kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Discipline.objects.get(pk=id)
        return None

    def resolve_contact(self,info,**kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Contact.objects.get(pk=id)
        return None

    def resolve_host(self,info,**kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Host.objects.get(pk=id)
        return None

    def resolve_country(self,info,**kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Country.objects.get(pk=id)
        return None

    def resolve_province(self,info,**kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Province.objects.get(pk=id)
        return None

    def resolve_city(self,info,**kwargs):
        id = kwargs.get('id')
        if id is not None:
            return City.objects.get(pk=id)
        return None

    def resolve_duration(self,info,**kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Duration.objects.get(pk=id)
        return None

    def resolve_resource(self,info,**kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Resource.objects.get(pk=id)
        return None

    def resolve_targetdemos(self,info,**kwargs):
        return TargetDemo.objects.all()

    def resolve_levels(self,info,**kwargs):
        return Level.objects.all()

    def resolve_kinds(self,info,**kwargs):
        return Kind.objects.all()

    def resolve_disciplines(self,info,**kwargs):
        return Discipline.objects.all()

    def resolve_contacts(self,info,**kwargs):
        return Contact.objects.all()

    def resolve_hosts(self,info,**kwargs):
        return Host.objects.all()

    def resolve_countrys(self,info,**kwargs):
        return Country.objects.all()

    def resolve_provinces(self,info,**kwargs):
        return Province.objects.all()

    def resolve_citys(self,info,**kwargs):
        return City.objects.all()

    def resolve_durations(self,info,**kwargs):
        return Duration.objects.all()

    def resolve_resources(self,info,**kwargs):
        return Resource.objects.all()


class Mutation(ObjectType):
    create_targetdemo = CreateTargetdemo.Field()
    create_level = CreateLevel.Field()
    create_kind = CreateKind.Field()
    create_discipline = CreateDiscipline.Field()
    create_contact = CreateContact.Field()
    create_host = CreateHost.Field()
    create_country = CreateCountry.Field()
    create_province = CreateProvince.Field()
    create_city = CreateCity.Field()
    create_duration = CreateDuration.Field()
    create_resource = CreateResource.Field()

    update_targetdemo = UpdateTargetDemo.Field()
    update_level = UpdateLevel.Field()
    update_kind = UpdateKind.Field()
    update_discipline = UpdateDiscipline.Field()
    update_contact = UpdateContact.Field()
    update_host = UpdateHost.Field()
    update_country = UpdateCountry.Field()
    update_province = UpdateProvince.Field()
    update_city = UpdateCity.Field()
    update_duration = UpdateDuration.Field()
    #update_resource = UpdateResource.Field()
