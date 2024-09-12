print("Ejemplo de funciones")
#declarando funciones
def hola():
    print("alguien uso la funcion hola")

def chat(mensa):
    print(f"chat {mensa}")

def ellacontesta(mensa):
    print(f"chat {mensa}")

def escribenombre(ap,n):
    print(f"tu nombre completo es {n} {ap}")
    
def suma(a,b):
    s=a+b
    return s
def r(a,b):
    r=a-b
    return r
def m(a,b):
    m=a*b
    return m
def d(a,b):
    d=a/b
    return d
#llamadas a funciones
hola()
chat("que bonito estas")
ellacontesta("gracias")
escribenombre("Camperos","Eliziel")
print("operaciones basicas")
print("suma")
c1=int(input("ingresa un numero "))
c2=int(input("ingresa otro numero "))
damesuma=suma(c1,c2)
print(f"la suma de {c1} + {c2} = {damesuma}")
print("resta")
c3=int(input("ingresa un numero "))
c4=int(input("ingresa otro numero "))
dr=r(c3,c4)
print(f"la resta de {c3} - {c4} = {dr}")
print("multiplicacion")
c5=int(input("ingresa un numero "))
c6=int(input("ingresa otro numero "))
dm=m(c5,c6)
print(f"la multiplicacion de {c5} x {c6} = {dm}")
print("division")
c7=int(input("ingresa un numero "))
c8=int(input("ingresa otro numero "))
dd=d(c7,c8)
print(f"la division de {c7} / {c8} = {dd}")
#python funciones.py