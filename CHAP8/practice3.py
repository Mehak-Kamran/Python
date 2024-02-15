#class method
class person:
    name="Roshan"
    @classmethod
    def changename(cls,name):
        cls.name=name

p1=person()
p1.changename("eddi")
print(p1.name)
print(person.name)

