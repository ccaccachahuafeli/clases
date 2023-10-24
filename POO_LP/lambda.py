# lambda un funcion que se autoejecuta
hola=lambda a,b:print(a+b)
# funcion normal
def suma(a,b):
    print(a+b)

suma(4,6) 
hola(10,20)   

# in ternario
ternario="soy verdad ternario" if True else "soy falso"
print(ternario)

# if normal

if True:
    print("soy verdad")
else:
    print("soy mentira")    

 # filter
 #
lista_alumnos=[{
    "nombre":"edwin",
    "edad":15,
    "hobby":"danza",
    "flaquita":"melody"
    },
    {
    "nombre":"del mar",
    "edad":30,
    "hobby":"saltar",
    "flaquita":"melody"  
    },
    {
    "nombre":"orlando",
    "edad":14,
    "hobby":"ponchar",
    "flaquita":"sami"   
    },
    {
    "nombre":"hans",
    "edad":19,
    "hobby":"quemarse",
    "flaquita":"melody"   
    }
]   
print(f"todos mis alumnitos{lista_alumnos}")
fans_melody=list(filter(lambda par:par ["flaquita"]=="melody",lista_alumnos)) # despues del : va condicion 
print(f"los que quieren con melody{fans_melody} ")


# map modifica 
nuevo_objet=list(map(lambda par:{"nombre_alumno":par}))