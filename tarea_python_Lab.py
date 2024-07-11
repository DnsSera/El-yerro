#Dennis Serafin Rodriguez Armenteros 31 G:21

def el_laberinto(mapa, inicio, fin) :
    cola = [(inicio, [])]
    pasos = []
    recorrido = []

    while (len(cola)) :
        pasos = cola.pop(0)

        if not(pasos[0] in pasos[1] ):
            pasos[1].append(pasos[0])

            if pasos[0] == fin :
                recorrido = pasos[1]
                cola = []
            else :
                direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                size = len(direcciones)
                for i in range (size) :
                    x, y = pasos[0][0] + direcciones[i][0], pasos[0][1] + direcciones[i][1]
                    if (x >= 0 and y >= 0) and (x < len(mapa)) and (y < len(mapa[0])) and (mapa[x][y] != 1) :
                        cola.append(((x, y), pasos[1].copy()))
    
    return recorrido

mapa = [[0,1,0,0,0],
        [0,0,0,1,0],
        [0,1,0,1,0],
        [0,1,1,1,1],
        [0,0,0,0,0]]

inicio = (2,2)
fin = (4,4)

print(el_laberinto(mapa, inicio, fin))


