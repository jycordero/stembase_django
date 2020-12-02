import graphene
from stembase.api.models import *
from stembase.api.graphql.graphqltypes import *
from stembase.api.graphql.graphqlinputs import *

class CreateCountry(graphene.Mutation):
    class Arguments:
        input = CountryInput(CountryType)
    ok = graphene.Boolean()
    country = graphene.Field(CountryType)
    @staticmethod
    def mutate(root,info,input=None):
        ok = True
        country_instance = Country(name=input.name)
        country_instance.save()
        return CreateCountry(ok=ok,country=country_instance)

class CreateCity(graphene.Mutation):
    class Arguments:
        input = CityInput(CityType)
    ok = graphene.Boolean()
    city = graphene.Field(CityType)

    @staticmethod
    def mutate(root,info,input=None):
        ok = True
        city_instance = City(name=input.name)
        city_instance.save()
        return CreateCity(ok=ok,city = city_instance)

class CreateProvince(graphene.Mutation):
    class Arguments:
        input = ProvinceInput(ProvinceType)
    ok = graphene.Boolean()
    province = graphene.Field(ProvinceType)
    @staticmethod
    def mutate(root,info,input=None):
        ok = True
        province_instance = Province(name=input.name)
        province_instance.save()
        return CreateProvince(ok=ok,province=province_instance)

class CreateHost(graphene.Mutation):
    class Arguments:
        input = HostInput(HostType)
    ok = graphene.Boolean()
    host = graphene.Field(HostType)
    @staticmethod
    def mutate(root,info,input=None):
        ok = True
        host_instance = Host(host=input.host)
        host_instance.save()
        return CreateHost(ok=ok,host=host_instance)

class CreateKind(graphene.Mutation):
    class Arguments:
        input = KindInput(KindType)
    ok = graphene.Boolean()
    kind = graphene.Field(KindType)

    @staticmethod
    def mutate(root,info,input=None):
        ok = True
        kind_intance = Kind(kind=input.kind)
        kind_instance.save()
        return CreateKind(ok=ok,kind=kind_intance)

class CreateLevel(graphene.Mutation):
    class Arguments:
        input = LevelInput(LevelType)
    ok = graphene.Boolean()
    level = graphene.Field(LevelType)
    @staticmethod
    def mutate(root,info,input=None):
        ok = True
        level_instance = Level(level=input.level)
        level_instance.save()
        return CreateLevel(ok=ok,level=level_instance)

class CreateDuration(graphene.Mutation):
    class Arguments:
        input = DurationInput(DurationType)
    ok = graphene.Boolean()
    duration = graphene.Field(DurationType)

    @staticmethod
    def mutate(root,info,input=None):
        ok = True
        duration_instance = Duration(duration=input.duration)
        duration_instance.save()
        return CreateDuration(ok=ok,duration=duration_instance)

class CreateDiscipline(graphene.Mutation):
    class Arguments:
        input = DisciplineInput(DisciplineType)
    ok = graphene.Boolean()
    discipline = graphene.Field(DisciplineType)
    @staticmethod
    def mutate(root,info,input=None):
        ok = True
        discipline_intance = Discipline(discipline=input.discipline)
        discipline_intance.save()
        return CreateDiscipline(ok=ok,discipline = discipline_intance)

class CreateContact(graphene.Mutation):
    class Arguments:
        input = ContactInput(ContactType)
    ok = graphene.Boolean()
    contact = graphene.Field(ContactType)
    @staticmethod
    def mutate(root,info,input=None):
        ok = True
        contact_instance = Contact(name=input.name,email=input.email)
        contact_instance.save()
        return CreateContact(ok=ok,contact=contact_instance)

class CreateTargetdemo(graphene.Mutation):
    class Arguments:
        input = TargetDemoInput(TargetDemoType)
    ok = graphene.Boolean()
    demographic = graphene.Field(TargetDemoType)
    @staticmethod
    def mutate(root,info,input=None):
        ok = True
        targetdemo_instance = TargetDemo(demographic=input.demographic)
        targetdemo_instance.save()
        return CreateTargetdemo(ok=ok,demographic=targetdemo_instance)

class CreateResource(graphene.Mutation):
    class Arguments:
        input = ResourceInput(ResourceType)
    ok = graphene.Boolean()
    resource = graphene.Field(ResourceType)
    @staticmethod
    def mutate(root,info,input=None):
        ok = True

        targetdemos = []
        levels = []
        kinds = []
        disciplines = []
        for targetdemo_input in input.targetdemos:
            targetdemo = TargetDemo.objects.get(pk=targetdemo_input.id) 
            if targetdemo is None:
                return CreateTargetDemo(ok=False,targetdemo=None)
            targetdemos.append(targetdemo)
        
        for level_input in input.levels:
            level = Level.objects.get(pk=level_input.id) 
            if level is None:
                return CreateLevel(ok=False,level=None)
            levels.append(level)

        for kind_input in input.kinds:
            kind = Kind.objects.get(pk=kind_input.id) 
            if kind is None:
                return CreateKind(ok=False,kind=None)
            kinds.append(kind)

        for discipline_input in input.disciplines:
            discipline = Discipline.objects.get(pk=discipline_input.id) 
            if kind is None:
                return CreateDiscipline(ok=False,discipline=None)
            disciplines.append(discipline)

        resource_instance = Resource(name=input.name,
                                     link=input.link,
                                     deadline_tba=input.deadline_tba,
                                     deadline=input.deadline,
                                     eligibility=input.eligibility,
                                     paid=input.paid,
                                     description=input.description,
                                     duration=input.duration,
                                     host=input.host,
                                     country=input.country,
                                     province=input.province,
                                     city=input.city,)
        resource_instance.save()
        resource_instance.targetdemos.set(targetdemos)
        resource_instance.levels.set(levels)
        resource_instance.kinds.set(kinds)
        resource_instance.disciplines.set(disciplines)
        return CreateResource(ok =ok, resource=resource_instance)       
