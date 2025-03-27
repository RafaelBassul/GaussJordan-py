def print_matrix(M, decimals=3):
    for row in M:
        print([round(x, decimals) + 0 for x in row])


def zeros_matrix(rows, cols):
    return [[0.0] * cols for _ in range(rows)]


def coef_matrix(augMat):
    return [row[:-1] for row in augMat]


def trocarLinhas(AM, i, n):
    if AM[i][i] == 0:
        for j in range(i + 1, n):
            if AM[j][i] != 0:
                AM[i], AM[j] = AM[j], AM[i]
        return AM


def determinant(AM):
    n = len(AM)
    for fd in range(n):
        trocarLinhas(AM, fd, n)
        for i in range(fd + 1, n):
            crScaler = AM[i][fd] / AM[fd][fd]
            for j in range(n):
                AM[i][j] -= crScaler * AM[fd][j]
    product = 1.0
    for i in range(n):
        product *= AM[i][i]
    return product


def verifica_non_singularidade(A):
    if A != 0:
        print("Matriz não singular")
        return True
    else:
        print("Matriz singular !!!!!!!!!!")
        return False


def GaussJordanMethod(augMat):
    n = len(augMat)
    m = len(augMat[0])
    
    for i in range(n):
        trocarLinhas(augMat, i, n)
        divisor = augMat[i][i]
        if divisor != 0:
            augMat[i] = [x / divisor for x in augMat[i]]
        
        for j in range(n):
            if i != j:
                coef = augMat[j][i]
                augMat[j] = [a - coef * b for a, b in zip(augMat[j], augMat[i])]

    solution = [max(0, round(row[-1])) for row in augMat]
    
    return solution


def Resolver(matrix):
    mc = coef_matrix(matrix)
    print("Matriz de coeficientes:")
    print_matrix(mc)
    
    det = determinant([row[:] for row in mc])  # Copia para não modificar a original
    print(f"Determinante: {det}")
    
    if verifica_non_singularidade(det):
        solution = GaussJordanMethod(matrix)
        print("Número de barcos em cada zona:")
        print(f"Zona A: {solution[0]} barcos")
        print(f"Zona B: {solution[1]} barcos")
        print(f"Zona C: {solution[2]} barcos")


x1 = float(input("Coloque o kg de peixes(A) por barco na zona A: "))
x2 = float(input("Coloque o kg de peixes(A) por barco na zona B: "))
x3 = float(input("Coloque o kg de peixes(A) por barco na zona C: "))
r1 = float(input("Coloque o KG max permitido de captura do peixe A: "))

x4 = float(input("Coloque o kg de peixes(B) por barco na zona A: "))
x5 = float(input("Coloque o kg de peixes(B) por barco na zona B: "))
x6 = float(input("Coloque o kg de peixes(B) por barco na zona C: "))
r2 = float(input("Coloque o KG max permitido de captura do peixe B: "))

x7 = float(input("Coloque o kg de peixes(C) por barco na zona A: "))
x8 = float(input("Coloque o kg de peixes(C) por barco na zona B: "))
x9 = float(input("Coloque o kg de peixes(C) por barco na zona C: "))
r3 = float(input("Coloque o KG max permitido de captura do peixe C: "))

matrix = [[x1, x2, x3, r1],
          [x4, x5, x6, r2],
          [x7, x8, x9, r3]]

Resolver(matrix)
print("Valores arredondados!")