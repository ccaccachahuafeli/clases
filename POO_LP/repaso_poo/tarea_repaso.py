class Vehiculo:
    def _init_(self,marca:str,modelo:str,color:str,ruedas:int):
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.ruedas=ruedas

    def prender(self,motor_prende):
        return motor_prende

    def apagar(self):
        return "se apago el auto"

    def avanzar(self):
        return "el auto esta en movimiento"

    def retroceder(self):
        return "el autos esta marcha atraz"
class Auto(Vehiculo):
    def _init_(self, marca: str, modelo: str, color: str, ruedas: int,rpm:int):
        super()._init_(marca, modelo, color, ruedas)
        self.rpm=rpm

    def nitro(self):
        return "nitro x10 activado"

class Omnibus(Vehiculo):
    def _init_(self, marca: str, modelo: str, color: str, ruedas: int,num_asientos:int):
        super()._init_(marca, modelo, color, ruedas)
        self.num_asientos=num_asientos
    
    def recojer_pasajero(self):
        return "parando en la parada y recojiendo positivas"

lambo=Auto("lamborguini","veneno","dorado",4,8400)
print(f"[bold blue]"+lambo.prender("encedido con llave"))
print("[bold blue]"+lambo.avanzar())
print("[bold blue]"+lambo.retroceder())
print("[bold blue]"+lambo.apagar())
print("[bold blue]"+lambo.nitro())

omnibus_palomino=Omnibus("mercedes","0500 RSD","blaco y verde",18,60)
print(f"[bold blue]"+omnibus_palomino.prender("encedido con llave"))
print("[bold blue]"+omnibus_palomino.avanzar())
print("[bold blue]"+omnibus_palomino.retroceder())
print("[bold blue]"+omnibus_palomino.apagar())
print("[bold blue]"+omnibus_palomino.recojer_pasajero())