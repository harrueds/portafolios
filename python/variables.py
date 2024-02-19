# Las variables pueden ser de tipo entero, flotante, string, boolean.
# Si escribo un número, lo asume numero y lo trata como numero.
numero1 = 34 #no necesita tipo, no necesita punto y coma al final.
numero2 = 25

tipon1 = type(numero1)
tipon2 = type(numero2)

print(tipon1)
print(tipon2)

suma = numero1 + numero2
print(suma) #los suma igual pascual, sin importar que no le dijera que son numeros.
# ojo con esto
numero1 = '34'
numero2 = "25"

tipon1 = type(numero1)
tipon2 = type(numero2)

print(tipon1)
print(tipon2)

suma = numero1 + numero2
print(suma) # Esto muestra 3425 porque al estar entre comillas (simple o doble, da lo mismo),
# asume que es string, porque está entre comillas

# Los boolean son True o son False, no son true, no son false, no son verdadero, no son falso, son True o son False.

bool1 = True # Esto está bien.
bool2 = true # Esto da error.
bool3 = verdadero # Esto ni siquiera lo mira, porque dió error en la línea anterior.

print(bool1)
print(bool2)
print(bool3)
