# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
   
    if m <= 0:     # para que la altura sea correcta
        return "Error: La altura debe ser un entero positivo"

    
    lineas = []        # Para la parte superior, es un triángulo invertido y así queda como en la referencia
    espacios = 0
    cantidad = m

    while cantidad > 0:
        lineas.append(" " * espacios + s * (2 * cantidad - 1))
        espacios += 1
        cantidad -= 1

   
    espacios -= 2   # Parte de abajo de la figura, el triengulo normalito
    cantidad = 2

    while cantidad <= m:
        lineas.append(" " * espacios + s * (2 * cantidad - 1))
        espacios -= 1
        cantidad += 1

    
    return "\n".join(lineas)     # para regresar a toda la figura como un solo string
