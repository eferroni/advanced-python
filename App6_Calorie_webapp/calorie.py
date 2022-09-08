from temperature import Temperature


class Calorie:

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        return 0


if __name__ == 'main':
    temperature = Temperature(country='brazil', city='porto-alegre').get()
    calorie = Calorie(weight=70,
                      height=175,
                      age=32,
                      temperature=temperature)
    print(calorie.calculate())
