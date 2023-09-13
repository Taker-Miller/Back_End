from Fiesta import Fiesta
class FiestaGala(Fiesta):
    def __init__(self, numero_personas: int):
        super(numero_personas)
        self.__costo_fijo_persona = 2000
        self.__opcion_saludable = False

    def set_opcion_saludable(self, opcion_saludable:bool):
        self.__opcion_saludable = opcion_saludable
        if opcion_saludable:
            self.__costo_fijo_persona = 4000

    def calcular_costo(self):
        #se deberia sumar el costo de una fiesta mas el costo de la gala y retornar su resultado
        costo_fiesta = super().calcular_costo()
        costo_gala = self.__costo_fijo_persona * super().__numero_personas
        total = costo_fiesta + costo_gala
        return total