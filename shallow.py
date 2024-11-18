if __name__=='__main__':
    # Criando uma lista l1
    l1 = [1,2,3,('A','b'),[4,5,6]]

    # Shallow copy da lista l1
    l2 = list(l1)

    # Conteudo igual identidade diferente
    print(f"l1 == l2: {l1==l2}")
    print(f"l1 is l2: {l1 is l2}")

    # Alteração em um item mutavel dentro de l1 altera l2
    l1[-1].append(7)
    print(f'l2: {l2}')

    # Alteração de um item imutavel dentro de l2 não altera l1
    l2[-2] += ('C',)
    print(f'l1: {l1}')
    print(f'l2: {l2}')