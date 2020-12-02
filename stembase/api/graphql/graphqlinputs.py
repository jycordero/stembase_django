import graphene

class TargetDemoInput(graphene.InputObjectType):
    id = graphene.ID()
    demographic = graphene.String()
    
class LevelInput(graphene.InputObjectType):
    id = graphene.ID()
    level = graphene.String()
    
class KindInput(graphene.InputObjectType):
    id = graphene.ID()
    kind = graphene.String()
    
class DisciplineInput(graphene.InputObjectType):
    id = graphene.ID()
    discipline = graphene.String()
    
class ContactInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()
    
class HostInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()

    
class CountryInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    
class ProvinceInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    
class CityInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    
class DurationInput(graphene.InputObjectType):
    id = graphene.ID()
    duration = graphene.String()
    
class ResourceInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    link = graphene.String()
    deadline_tba = graphene.Int()
    deadline = graphene.String()
    eligibility = graphene.String()
    paid = graphene.Int()
    description = graphene.String()

    #contact = graphene.String()
    contact_name = graphene.String()
    contact_email = graphene.String()
    
    duration = graphene.String()
    host = graphene.String()
    country = graphene.String()
    province = graphene.String()
    city = graphene.String()


    targetdemos = graphene.List(TargetDemoInput)
    levels = graphene.List(LevelInput)
    kinds = graphene.List(KindInput)
    disciplines = graphene.List(DisciplineInput)
    



#class TargetDemoInput
#class LevelInput
#class KindInput
#class DisciplineInput
#class ContactInput
#class HostInput
#class CountryInput
#class ProvinceInput
#class CityInput
#class DurationInput
#class ResourceInput


#TargetDemo
#Level
#Kind
#Discipline
#Contact
#Host
#Country
#Province
#City
#Duration
#Resource


#targetdemo
#level
#kind
#discipline
#contact
#host
#country
#province
#city
#duration
#resource