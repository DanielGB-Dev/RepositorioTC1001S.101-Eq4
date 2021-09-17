
import random

Lado_A = ['Granjero', 'Zorro', 'Ganzo', 'Maiz']
Lado_B = []
Path = []


def seleccion(L):
    """Select a random element from a list.

    Args:
        L (list): Lado_A

    Returns:
        str: element from L
    """
    op = random.randint(0, len(L)-1)
    return (L[op])


def Viaje(F, D):
    """Simula el viaje que realiza el granjero del lado A al lado B, llevando a uno de 
    los animales

    Args:
        F (list): Lado_A
        D (list): Lado_B

    Returns:
        str: Granjero, p1
    """
    p1 = seleccion(F)  # Select a random element from Lado_A
    #print ('Selección -> ', p1)
    if p1 != 'Granjero':
        F.remove(p1)
        D.append(p1)

    F.remove('Granjero')
    D.append('Granjero')

    #print (F)
    #print (D)
    return ('Granjero', p1)


def valida_estado(L):
    """Check that neither the goose and the corn are together nor 
    the fox and the goose

    Args:
        L (list)

    Returns:
        boolean
    """
    if 'Maiz' in L and 'Ganzo' in L and len(L) == 2:
        return False
    elif 'Zorro' in L and 'Ganzo' in L and len(L) == 2:
        return False
    return True


def reiniciar_sistema():
    """
    Reset global variables
    """
    global Lado_A, Lado_B, Path

    Lado_A = ['Granjero', 'Zorro', 'Ganzo', 'Maiz']
    Lado_B = []
    Path = []


def HCR():
    """Check the possible solutions and display a list 
    with the solution  

    Returns:
        list: problem solution
    """
    F = Lado_A
    D = Lado_B
    while len(Lado_B) != 4:
        p1, p2 = Viaje(F, D)
        if valida_estado(F) and valida_estado(D):
            #print ('Estado valido, continuamos')
            if F == Lado_A:
                Path.append('A->B :')
            else:
                Path.append('B->A :')
            Path.append(p1)
            Path.append(p2)

            Temp = F
            F = D
            D = Temp
        else:
            #print ('Estado inválido, REINICIO DEL SISTE;A')
            reiniciar_sistema()
            F = Lado_A
            D = Lado_B
    return (Path)


def main():
    """Call HCR() until it finds the best solution
    """
    P = HCR()
    while len(P) > 22:
        reiniciar_sistema()
        print('\nBuscando una mejor solución, Longitud del Path', len(P))
        P = HCR()
    print(P)
    print(len(P))


main()
