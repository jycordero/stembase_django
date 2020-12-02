import graphene
from stembase.api.models import *
from stembase.api.graphql.graphqltypes import *
from stembase.api.graphql.graphqlinputs import *


class UpdateLevel(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = LevelInput(required=True)

    ok = graphene.Boolean()
    level = graphene.Field(LevelType)

    @staticmethod
    def mutate(root,info,id,input=None):
        ok = False
        level_instance = Level.objects.get(pk=id)
        if level_instance:
            ok = True
            level_instance.level = input.level
            level_instance.save()
            return UpdateLevel(ok=ok,level=level_instance)
        return UpdateLevel(ok=ok,level=level_instance)


class UpdateKind(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = KindInput(required=True)

    ok = graphene.Boolean()
    kind = graphene.Field(KindType)

    @staticmethod
    def mutate(root,info,id,input=None):
        ok = False
        kind_instance= Kind.objects.get(pk=id)
        if kind_instant:
            ok = True
            kind_instance = input.kind
            kind_instance.save()
            return UpdateLevel(ok=ok,level=level_instance)
        return UpdateLevel(ok=ok,level=None)

class UpdateDiscipline(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = DisciplineInput(required=True)

    ok = graphene.Boolean()
    discipline = graphene.Field(DisciplineType)

    @staticmethod
    def mutate(root,info,id,input=None):
        ok = False
        discipline_instance = Discipline.objects.get(pk=id)
        if discipline_instance:
            discipline_instance.discipline = input.discipline
            discipline_instance.save()
            return UpdateDiscipline(ok=ok,discipline=discipline_instance)
        return UpdateDiscipline(ok=ok,discipline=None)

class UpdateContact(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = ContactInput(required=True)

    ok = graphene.Boolean()
    contact = graphene.Field(ContactType)

    @staticmethod
    def mutate(root,info,id,input=None):
        ok = False
        if contact_instance:
            contact_instance.name = input.name
            contact_instance.email = input.email
            contact_instance.save()
            return UpdateContact(ok=ok,contact=contact_instance)
        return UpdateContact(ok=ok,contact=None)

class UpdateHost(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = HostInput(required=True)

    ok = graphene.Boolean()
    host = graphene.Field(HostType)

    @staticmethod
    def mutate(root,info,id,input=None):
        ok = False
        host_instance = Host.objects.get(pk=id)
        if host_instance:
            host_instance.name = input.name
            host_instance.save()
            return UpdateHost(ok=ok,host=host_instance)
        return UpdateHost(ok=ok,host=None)


class UpdateTargetDemo(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = TargetDemoInput(required=True)

    ok = graphene.Boolean()
    targetdemo = graphene.Field(TargetDemoType)

    @staticmethod
    def mutate(root,info,id,input=None):
        ok = False
        targetdemo_instance = TargetDemo.objects.get(pk=id)
        if targetdemo_instance:
            targetdemo_instance.demographic = input.demographic
            targetdemo_instance.save()
            return UpdateTargetDemo(ok=ok,targetdemo=targetdemo_instance)
        return UpdateTagerDemo(ok=ok,targetdemo=None)


class UpdateCountry(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = CountryInput(required=True)

    ok = graphene.Boolean()
    country = graphene.Field(CountryType)

    @staticmethod
    def mutate(root,info,id,input=None):
        ok = False
        country_instance = Country.objects.get(pk=id)
        if targetdemo_instance:
            country_instance.name = input.name
            country_instance.save()
            return UpdateCountry(ok=ok,country=country_instance)
        return UpdateCountry(ok=ok,country=None)
        
class UpdateProvince(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = ProvinceInput(required=True)

    ok = graphene.Boolean()
    province = graphene.Field(ProvinceType)

    @staticmethod
    def mutate(root,info,id,input=None):
        ok = False
        province_instance = Province.objects.get(pk=id)
        if province_instance:
            province_instance.name = input.name
            province_instance.save()
            return UpdateProvince(ok=ok,province=province_instance)
        return UpdateProvince(ok=ok,province=None)

class UpdateCity(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = CityInput(required=True)

    ok = graphene.Boolean()
    city = graphene.Field(CityType)

    @staticmethod
    def mutate(root,info,id,input=None):
        ok = False
        city_instance = City.objects.get(pk=id)
        if city_instance:
            city_instance.name = input.name
            city_instance.save()
            return UpdateCity(ok=ok,city=city_instance)
        return UpdateCity(ok=ok,city=None)

class UpdateDuration(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = DurationInput(required=True)

    ok = graphene.Boolean()
    duration = graphene.Field(DurationType)

    @staticmethod
    def mutate(root,info,id,input=None):
        ok = False   
        duration_instance = Duration.objects.get(pk=id)
        if duration_instance:
            duration_instance.duration = input.duration
            duration_instance.save()
            return UpdateDuration(ok=ok,duration=duration_instance)
        return UpdateDuration(ok=ok,duration=None)     
'''
       
class UpdateResource(graphene.Mutate):
    class Arguments:
        id = graphene.Int(required=True)
        input = ResourceInput(required=True)

    ok = graphene.Boolean()
    resource = graphene.Field(ResourceType)

    @staticmethod
    def mutate(root,info,id,input=None):
        ok = False
'''