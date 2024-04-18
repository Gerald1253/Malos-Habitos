def calcular_area_rectangulo(ancho, largo):
    """
    Calcula el área de un rectángulo.
    """
    area = ancho * largo
    return area

def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo.
    """
    area = 0.5 * base * altura
    return area

def principal():
    # Datos del rectángulo
    ancho_rectangulo = 4
    largo_rectangulo = 6
    area_rectangulo = calcular_area_rectangulo(ancho_rectangulo, largo_rectangulo)
    print("Área del rectángulo:", area_rectangulo)

    # Datos del triángulo
    base_triangulo = 5
    altura_triangulo = 8
    area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
    print("Área del triángulo:", area_triangulo)

if __name__ == "__main__":
    principal()

