def print_matrix(M, decimals=3):
    """
    Print a matrix one row at a time

    :param M: The matrix to be printed
    """
    for row in M:
        print([round(x, decimals) + 0 for x in row])


def zeros_matrix(rows, cols):
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)
    return M


def coef_matrix(augMat):
    rows = len(augMat)
    cols = len(augMat[0])

    MC = zeros_matrix(rows, cols - 1)

    for i in range(rows):
        for j in range(cols - 1):
            MC[i][j] = augMat[i][j]

    return MC


def trocarLinhas(AM, i, n):
    if AM[i][i] == 0:
        for j in range(i + 1, n):
            if AM[j][i] != 0:
                AM[i], AM[j] = AM[j], AM[i]
        return AM


def determinant(AM):
    n = len(AM)

    # Redução à forma triangular superior
    for fd in range(n):  # fd: foco diagonal values
        trocarLinhas(AM, fd, n)

        for i in range(fd + 1, n):
            crScaler = AM[i][fd] / AM[fd][fd]
            for j in range(n):
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]

    # Uma vez que temos a forma triangular, calculamos o produto da diagonal principal
    product = 1.0
    for i in range(n):
        product *= AM[i][i]

    return product


def verifica_non_singularidade(A):
    if A != 0:
        return print("Matriz não singular !!!!!!!!!!")
    else:
        print("Matriz singular !!!!!!!!!!")
        return False


def GaussJordanMethod(augMat):
    n = len(augMat)  # Número de linhas
    m = len(augMat[0])  # Número de colunas

    for i in range(n):
        # Verifica se o pivô é zero e muda a linha se necessário
        trocarLinhas(augMat, i, n)

        # Normalizando cada linha
        # L_i <-- L_i / a_ii
        if augMat[i][i] != 1:
            divisor = augMat[i][i]
            for k in range(m):
                augMat[i][k] /= divisor

        # Zera as entradas referentes aos pivôs
        # L_j <-- L_j - a_ji * L_i
        for j in range(n):
            if i != j:
                coef = augMat[j][i]
                for k in range(m):
                    augMat[j][k] -= coef * augMat[i][k]

    print(augMat)


def Resolver(matrix):
    mc = coef_matrix(matrix)
    print("Matriz de coeficientes:")
    print_matrix(mc)

    det = determinant(mc)
    print(f"Determinante: {det}")

    if verifica_non_singularidade(det) != False:
        GaussJordanMethod(matrix)


x = float(input("Coloque quantas proções você colocou do item X na primeira mistura: "))
y = float(input("Coloque quantas proções você colocou do item Y na primeira mistura: "))

xx = float(input("Coloque quantas proções você colocou do item X na segunda mistura: "))
yy = float(input("Coloque quantas proções você colocou do item Y na segunda mistura: "))

r = float(input("Coloque o total de caloria a primeira porção tem: "))
rr = float(input("Coloque o total de caloria a segunda porção tem: "))





matrix = [[x , y, r],
          [xx, yy, rr]]





Resolver(matrix)
