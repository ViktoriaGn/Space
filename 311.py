
class Cocktail:
    def _init_(self, ingredient):
        self.ingredient=ingredient

    def drink(self):
        if self.ingredient:
            print(f"Koктейль с {self.ingredient}")
        else:
            print("Молочный коктейль без добавок")

ingredient=input("Введите добавку к коктейлю: ")

c1=Cocktail(ingredient)

c1.drink()
