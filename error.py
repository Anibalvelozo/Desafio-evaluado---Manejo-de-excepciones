class DimensionError(Exception):
    def __init__(self, mensaje: str, dimension: int = None, maximo: int = None) -> None:
        super().__init__(mensaje)
        self.dimension = dimension
        self.maximo = maximo
    
    def __str__(self) -> str:
        if self.dimension is not None and self.maximo is not None:
            return f"{self.mensaje}. La dimensión ingresada {self.dimension} es mayor a la máxima permitida {self.maximo}."
        else:
            return super().__str__()
