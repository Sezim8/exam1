# # Композиция позволяет повторно использовать код, добавляя объекты к другим объектам, в отличие от наследования интерфейса и реализации других классов. Классы Horse и Dog могут использовать функциональность Tail посредством композиции, не выводя один класс из другого.

# Композиция в Python. Композиция — это объектно-ориентированная концепция дизайна, которая моделирует отношения. В композиции класс, известный как составной, содержит объект другого класса, известный как компонент. Другими словами, составной класс имеет компонент другого класса.

class Address:
    def __init__(self, street, city, state, zipcode, street2=''):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode
    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state} {self.zipcode}')
        return '\n'.join(lines)