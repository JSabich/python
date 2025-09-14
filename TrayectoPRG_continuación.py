'''
#Ejercicio 1
Numero1=int( input("Ingrese el Primer número : "))
Numero2=int(input("Ingrese el segundo número : "))
Numero3=int (input("Ingrese el tercer número : "))

while (Numero1==Numero2 or Numero2==Numero3 or Numero1==Numero3):
    
    
    Numero1=int( input("Ingrese el Primer número : "))
    Numero2=int(input("Ingrese el segundo número : "))
    Numero3= int (input("Ingrese el tercer número : "))
      
if (Numero1>Numero2 and Numero1>Numero3):
    print(f'El numero  {Numero1} es el mayor')
    if(Numero2>Numero3):
        print(f'El número  {Numero3} es el menor')
    else:
        print(f'El número  {Numero2} es el menor')

elif (Numero2>Numero1 and Numero2>Numero3):    
    print(f'El numero  {Numero2} es el mayor')
    if(Numero1>Numero3):
        print(f'El número  {Numero3} es el menor')
    else:
        print(f'El número  {Numero1} es el menor')
   
elif (Numero3>Numero1 and Numero3>Numero2):    
    print(f'El numero  {Numero3} es el mayor')
    if(Numero1>Numero2):
        print(f'El número  {Numero2} es el menor')
    else:
        print(f'El número  {Numero1} es el menor')
      
   
 #Ejercicio 1 opción de la IA
 # Pedimos los números en un bucle que se repite solo si son iguales
while True:
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    numero3 = int(input("Ingrese el tercer número: "))

    if numero1 != numero2 and numero2 != numero3 and numero1 != numero3:
        break # Si los números son todos distintos, salimos del bucle
    else:
        print("Los números no pueden ser iguales. Inténtalo de nuevo.")

# Usamos las funciones integradas de Python para encontrar el mayor y el menor
mayor = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)

print(f'El número {mayor} es el mayor')
print(f'El número {menor} es el menor')  
       

# Ejercicio 2
Numero1=int( input("Ingrese el Primer número : "))
Numero2=int(input("Ingrese el segundo número : "))
Numero3= int (input("Ingrese el tercer número : "))

if (Numero1+Numero2==Numero3):
    print("Son Iguales")
    
elif(Numero3+Numero1==Numero2):
    print("Son Iguales")
    
elif(Numero2+Numero3==Numero1):
    print("Son Iguales")
    
else:
    print("No son iguales")'''
    
Valor_hora= 2
Nombre=input("Ingrese el Nombre del empleado: ")
Horas_trabajadas=float(input("Ingrese la cantida de horas trabajadas: "))

if (Horas_trabajadas<=40):
    print(f'El empleado {Nombre} cobrará la suma de $ {Horas_trabajadas*Valor_hora}')
else:
    print(f'El empleado {Nombre} cobrará la suma de $ {((Horas_trabajadas-40)*(Valor_hora*1.5))+(40*Valor_hora)}')
    
    
