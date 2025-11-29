# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if m <= 0:     # para que la altura sea correcta
        return "Error: La altura debe ser un entero positivo"
    # TODO: implementar la lógica para generar el reloj de arena en ASCII
    lineas = []        # Para la parte superior, es un triángulo invertido y así queda como en la referencia
    espacios = 0
    cantidad = m

    while cantidad > 0:
        lineas.append(" " * espacios + s * (2 * cantidad - 1))
        espacios += 1
        cantidad -= 1

    espacios = m - 2   # Parte inferior de la figura, el triángulo normal
    cantidad = 2

    while cantidad <= m:
        lineas.append(" " * espacios + s * (2 * cantidad - 1))
        espacios -= 1
        cantidad += 1

    
    return 

    # En este archivo debes implementar la función


   
    

    
