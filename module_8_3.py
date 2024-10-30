class IncorrectVinNumber(Exception):
    def __init__(self, message: str):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message: str):
        self.message = message

class Car:
    def __init__(self, model: str, vin: int, numbers: str):
        if self.__is_valid_vin(vin) and self.__is_valid_numbers(numbers):
            self.__vin = vin
            self.__numbers = numbers
            self.model = model
            print(f'{self.model} успешно создан')
    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный vin номер')
        if not(1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else: return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if not(len(numbers) == 6):
            raise IncorrectCarNumbers('Неверная длина номера')
        else: return True

class Try_Except_Car(Car):
    def __init__(self, *args):
        try:
            super().__init__(*args)
        except IncorrectVinNumber as exc:
            print(exc.message)
        except IncorrectCarNumbers as exc:
            print(exc.message)

if __name__ == '__main__':
    first = Try_Except_Car('Model1', 1000000, 'f123dj')
    second = Try_Except_Car('Model2', 300, 'т001тр')
    third = Try_Except_Car('Model3', 2020202, 'нет номера')