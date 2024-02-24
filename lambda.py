people=[
    {"name": "Harry","house":"eakamega"},
    {"name":"aode","house":"tisumu"},
    {"name":"kelvin","house":"jilifi"}


]

def f(person):
    return person["house"]

people.sort(key=f)
print(people)