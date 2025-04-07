def determinar_rango_vlan():
    
    
    print("Determinador de rango de VLAN")
    
    
    while True:
        try:
            
            vlan = int(input("Introduce el número de VLAN (1-4094): "))
            
            
            if 1 <= vlan <= 4094:
                
                if vlan <= 1005:
                    print(f"La VLAN {vlan} pertenece al rango NORMAL (1-1005).")
                else:
                    print(f"La VLAN {vlan} pertenece al rango EXTENDIDO (1006-4094).")
                break
            else:
                print("Error: El número de VLAN debe estar entre 1 y 4094.")
                
        except ValueError:
            print("Error: Por favor, introduce un número válido.")


if __name__ == "__main__":
    determinar_rango_vlan()
