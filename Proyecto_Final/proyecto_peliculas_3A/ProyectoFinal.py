import os
repetir="si"
numerodis=0
TotalVendido=0
IvaValor=0.16
CostoRevision=50.0

def imprimir_ticket(Subtotal, Descuento, CostoRevision,Subdesc, SubIva, SubNeto):
  print("========Ticket de cobro==============")
  print(f"Total del mantenimiento   {Subtotal}$")
  print(f"Descuento realizado       {Descuento}%")
  print(f"Costo de revision es      {CostoRevision}$")
  print(f"Precio con descuento      {Subdesc}$")
  print(f"Precio con iva            {SubIva}$")
  print(f"Precio neto               {SubNeto}$")

# --- NUEVA FUNCIÓN AGREGADA ---
def resumen_sesion(total_procesos, dinero_total):
  print("*************************************")
  print("       RESUMEN DE LA JORNADA")
  print(f" Procesos realizados: {total_procesos}")
  print(f" Total neto vendido:  {dinero_total}$")
  print("*************************************")

#Calculo de la ley de ohm
#===========================================================
while repetir=="si":
 print("\033c")
 print("===Calculos de la ley de ohm===")
 print("a)Calculo de voltaje")
 print("b)Calculo de corriente")
 print("c)Calculo de resistencia")
 pregunta=input("Elije la opcion que nececitas:").lower()
 print("\033c")
#===========================================================
 if pregunta=="a":
    print("|Calculo de voltaje|")
    i=float(input("Escribe la corriente:"))
    r=float(input("Escribe la resistencia:"))
    voltaje=i*r
    print("DATOS INGRESADOS")
    print(f"El voltaje es igual a:{voltaje}")
#===========================================================
 elif pregunta=="b":
  print("|Calculo de corriente|")
  v=float(input("Escribe el voltaje:"))
  r=float(input("Escribe la resistencia:"))
  try:
   corriente=v/r
   print(f"La corriente es igual a:{corriente}")
  except ZeroDivisionError:
      print("ERROR:no se puede dividir entre cero")
#============================================================
 elif pregunta=="c":
  print("|Calculo de resistencia|")
  v=float(input("Escribe el voltaje:"))
  i=float(input("Escribe la corriente:"))
  try:
   resistencia=v/i
   print(f"La resistencia es igual a:{resistencia}")
  except ZeroDivisionError:
   print("ERROR:no se puede dividir entre cero")
 else:
   print("Numero incorrecto intente de nuevo")
#===========================================================
#Calculo de los costos======================================
 Subtotal=float(input("Escribe el total cobrado:"))
 Descuento=float(input("Tipo de descuento:"))
 Descuento = Subtotal * (Descuento / 100)
 Subdesc=Subtotal-Descuento
 SubIva=(Subdesc+CostoRevision)*IvaValor
 SubNeto=Subdesc+SubIva
 print("\033c")
 numerodis=1+numerodis
 TotalVendido=SubNeto+TotalVendido # Sumamos el neto al total vendido
 procesos=print(f"Numero de procesos realizado:{numerodis}")
 print(f"El total vendido fue:{TotalVendido}")
 #Ticket de venta============================================
 imprimir_ticket(Subtotal, Descuento, CostoRevision,Subdesc, SubIva, SubNeto)
 repetir=input("¿Quieres hacer otro proceso? (si/no)?").lower()

#Salida del programa=========================================
print("\033c")
resumen_sesion(numerodis, TotalVendido) # Llamada a la nueva función
print("Proceso finalizado tenga buen dia :)")