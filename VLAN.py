def verificar_vlan(numero_vlan):
    if 1 <= numero_vlan <= 1000:
        return "VLAN del rango normal"
    elif 1002 <= numero_vlan <= 4094:
        return "VLAN del rango extendido"
    else:
        return "Número de VLAN inválido"

try:
    numero_vlan = int(input("Ingresa el número de VLAN: "))
    resultado = verificar_vlan(numero_vlan)
    print(resultado)
except ValueError:
    print("Error: Ingresa un número válido.")
