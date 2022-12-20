class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computation(self):
        return self.__cpu // self.__memory

    def __str__(self):
        return f'computer cpu: {self.cpu}, memory: {self.memory}'

    def __gt__(self, other):
        return self.memory > other.memory

    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = list(sim_cards_list)

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        return f'Идет звонок на номер {call_to_number}'\
               f' с сим-карты-{self.sim_cards_list[sim_card_number - 1]}'

    def __str__(self):
        return f'sim card list: {self.sim_cards_list}'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    @staticmethod
    def use_gps(location):
        return f'путь проложен до {location}'

    def __str__(self):
        return super(Computer, self).__str__() + super(Phone, self).__str__()


xiaomi_comp = Computer(520, 16)
print(xiaomi_comp)
xiaomi_phone = Phone(['Megacom', 'Beeline', 'O'])
print(f'Available operators on xiaomi phone: {xiaomi_phone.sim_cards_list}')
xiaomi_smartphone = SmartPhone(30, 129, ['Beeline', 'Megacom', 'O'])
print(f'xiaomi smartphone cpu: {xiaomi_smartphone.cpu}, memory: {xiaomi_smartphone.memory},'
      f'available operators: {xiaomi_smartphone.sim_cards_list} ')
samsung = SmartPhone(40, 64, ['Beeline', 'Megacom', 'O'])
print(f'samsung smartphone cpu: {samsung.cpu}, memory: {samsung.memory},'
      f'available operators: {samsung.sim_cards_list} ')
print(samsung.use_gps('Бишкек'))
print(xiaomi_smartphone.use_gps('Каракол'))
print(samsung.call(2, '+996558320456'))
print(xiaomi_smartphone.call(1, '+996777667490'))
print(xiaomi_comp.make_computation())
print(xiaomi_smartphone == samsung)