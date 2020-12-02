from django.db import models

#####################
# Many-To-Many
class TargetDemo(models.Model):
    demographic = models.CharField(max_length=255)
    def __repr__(self):
        return self.demographic
    def __str__(self):
        return self.demographic

class Citizenship(models.Model):
    citizenship = models.CharField(max_length=255)
    def __repr__(self):
        return self.citizenship
    def __str__(self):
        return self.citizenship
    

class Level(models.Model):
    level = models.CharField(max_length=255)
    def __repr__(self):
        return self.level
    def __str__(self):
        return self.level

class Kind(models.Model):
    kind = models.CharField(max_length=255)
    def __repr__(self):
        return self.kind
    def __str__(self):
        return self.kind

class Discipline(models.Model):
    discipline = models.CharField(max_length=4095)
    def __repr__(self):
        return self.discipline
    def __str__(self):
        return self.discipline

#####################
# One-To-Many
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    def __str__(self):
        contact = 'N:%s, E:%s'
        return contact % (self.name,self.email)

class Host(models.Model):
    name = models.CharField(max_length=255)
    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=255, blank=True)
    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Province(models.Model):
    name = models.CharField(max_length=255, blank=True)
    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=255, blank=True)
    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Duration(models.Model):
    duration = models.CharField(max_length=255)
    def __repr__(self):
        return self.duration

    def __str__(self):
        return self.duration

#####################
# Parent
class Resource(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    deadline_tba = models.IntegerField(null=True)
    deadline = models.DateField()
    eligibility = models.CharField(max_length=4095)
    paid = models.IntegerField(null=True)
    description = models.TextField(max_length=4095)
    contact = models.ForeignKey(Contact,on_delete=models.CASCADE)

    # One-To-Many (member-to-resource)
    duration = models.ForeignKey(Duration,on_delete=models.CASCADE)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    #many-to-many
    citizenship = models.ManyToManyField(Citizenship)
    targetdemo = models.ManyToManyField(TargetDemo)
    level = models.ManyToManyField(Level)
    kind = models.ManyToManyField(Kind)
    discipline = models.ManyToManyField(Discipline)

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            'resource_id':self.id,
            'resource_name':self.name,
            'resource_link':self.link,
            'resource_deadline_tba':self.deadline_tba,
            'resource_deadline':self.deadline,
            'resource_eligibility':self.eligibility,
            'resource_paid':self.paid,
            'resource_description':self.description,
            'resource_duration':self.duration,
            'resource_host':self.host,
            'resource_country':self.country,
            'resource_province':self.province,
            'resource_city':self.city,
            'resource_targetdemo':{s for s in self.targetdemo.all()},
            'resource_level':{s for s in self.level.all()},
            'resource_kind':{s for s in self.kind.all()},
            'resource_discipline':{s for s in self.discipline.all()},
        }

'''
name
link
deadline_tba
deadline
eligibility
paid
description
contact
duration
host
country
province
city
citizenship
targetdemo
level
kind
discipline
'''