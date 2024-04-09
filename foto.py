from error import DimensionError

class FiguraGeometrica:
    MAX_DIMENSION = 100

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self._dimension = 0

    @property
    def dimension(self) -> int:
        return self._dimension

    @dimension.setter
    def dimension(self, value: int) -> None:
        try:
            if value < 1 or value > self.MAX_DIMENSION:
                raise DimensionError(f"Error al establecer la dimensión de la {self.nombre}", value, self.MAX_DIMENSION)
        except DimensionError as e:
            print(e)
        else:
            self._dimension = value
            
#Pruebas             
cuadrado = FiguraGeometrica("cuadrado")

cuadrado.dimension = 120  # Esto debería lanzar una excepción de DimensionError