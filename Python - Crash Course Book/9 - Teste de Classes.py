class Car():
    def __init__(self, model, year, odometer) -> None:
        self.model = model
        self.year = year
        self.odometer = odometer
    
    def range(self):
        '''''Mostra quantos Km o carro pode andar'''
        motor_range = 300000 - int(self.odometer)
        return int(motor_range)

    def update_odometer(self, new_mileage):
        if self.odometer >= new_mileage:
            print('Você colocou uma milhagem maior')
        else:
            self.odometer = new_mileage

Meu_Carro = Car('Ferrari', 1990, 245000)
print(Meu_Carro.range())
Meu_Carro.update_odometer(250000)
print(Meu_Carro.range())