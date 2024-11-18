import copy

class Bus:
    def __init__(self,passengers = None) -> None:
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self,name):
        self.passengers.append(name)

    def drop(self,name):
        self.passengers.remove(name)

def test_mutable_parameter(a,b):
    a+=b
    return a

def test_mutable_defaults(name=None,guests=[]):
    if name is not None:
        guests.append(name)
    if guests:
        print(f"Convidados: {guests}")
        return id(guests)
    else:
        print("Sem convidadados na lista!")

if __name__=='__main__':
    # Criando uma instancia de Bus
    bus1 = Bus('Alice Bill Claire David'.split())

    # Shallow copy de bus1
    bus2 = copy.copy(bus1)

    # Deep copy de bus1
    bus3 = copy.deepcopy(bus1)

    # Identidades diferentes
    print(f"""
    bus1: {id(bus1)},
    bus2: {id(bus2)},
    bus3: {id(bus3)}
    """)

    # Como bus2 é uma shallow copy de bus1 eles compartilham a mesmo referencia atribuida ao atributo passengers
    bus1.drop('Bill')
    print(f'bus2.passengers: {bus2.passengers}')

    # Como bus3 é uma deep copy de bus1 o atributo passengers é um objeto diferente 
    print(f'bus3.passengers: {bus3.passengers}')

    # Prova de referencia
    print(f"""
    bus2.passengers: {id(bus2.passengers)},
    bus1.passengers: {id(bus1.passengers)},
    bus3.passengers: {id(bus3.passengers)}
    """)

    # Teste com parametros imutaveis nenhuma variavel fora do escopo da função foi alterada
    a = 1
    b = 2
    print(f'Teste parametro como referencia para: a={a}, b={b}: {test_mutable_parameter(a,b)}')
    print(f'a={a}, b={b}')

    # Teste com parametros mutaveis função alterou variavel a fora do escopo
    a = [1]
    b = [2]
    print(f'Teste parametro como referencia para: a={a}, b={b}: {test_mutable_parameter(a,b)}')
    print(f'a={a}, b={b}')

    # Obs: Quando for trabalhar com parametros que recebem objetos mutaveis sempre é uma boa pratica
    # trabalhar com o Principio Do Menor Espanto(Principle of least Astonishment) 
    # e realizar uma copia do atributo mutavel dentro do escopo da função

    # O perigo de se ter valores mutaveis como padrão em parametros de funções é a perpetuação da referencia a esse objeto
    # entre diferentes chamadas da função
    print(f'Test parametro mutavel como padrão id: {test_mutable_defaults('joao')}')
    print(f'Test parametro mutavel como padrão id: {test_mutable_defaults()}')