import numpy as np
import pytool


def gerschgorin(A=None):
    """compute gerschgorins of matrix A (row)

    .. math::
       |z - a_{ii}| \leq R_i  , R_i = R_i({\mathbf A}) = \sum_{j=1,j\neq i}^n |a_{ij}|

    Keyword Arguments:
       A {numpy array or list} -- matrix (default: {None})
    """

    if A is None:
        ValueError("A should a matrix, not None!")

    A = np.array(A)

    if np.ndim(A) is not 2:
        ValueError("A should a 2-D matrix!")

    H, W = A.shape

    cnt = 0
    Cis = []
    Ris = []
    for ai in A:
        Cis.append(ai[cnt])
        Ris.append(np.sum(np.abs(ai)) - np.abs(ai[cnt]))
        cnt = cnt + 1

    print(Cis, Ris)

    return Cis, Ris


def gerschgorin2(A=None):
    """compute gerschgorins of matrix A min(row, col)

    .. math::
       |z - {a_{ii}}| \le {R_i},{R_i} = {R_i}({\bf{A}}) = \min \left( {\sum\limits_{j = 1,j \ne i}^n | {a_{ij}}|{\rm{,}}\;\sum\limits_{i = 1,i \ne j}^n | {a_{ij}}|} \right)

    Keyword Arguments:
       A {numpy array or list} -- matrix (default: {None})
    """

    if A is None:
        ValueError("A should a matrix, not None!")

    A = np.array(A)

    if np.ndim(A) is not 2:
        ValueError("A should a 2-D matrix!")

    H, W = A.shape

    if H != W:
        ValueError("A should a square matrix!")

    cnt = 0
    Cis = []
    Ris = []

    for ai, aj in zip(A, A.transpose()):
        Cis.append(ai[cnt])
        Rii = np.sum(np.abs(ai)) - np.abs(ai[cnt])
        Rij = np.sum(np.abs(aj)) - np.abs(ai[cnt])
        Ri = np.min([Rii, Rij])

        Ris.append(Ri)
        cnt = cnt + 1
    print(Cis, Ris)

    return Cis, Ris


if __name__ == '__main__':

    from matplotlib import pyplot as plt

    A = [[20, 3, 1], [2, 10, 2], [8, 1, 0]]

    Cis = []
    Ris = []

    Cis1, Ris1 = gerschgorin(A)
    Cis2, Ris2 = gerschgorin2(A)
    Cis = Cis + Cis1
    Ris = Ris + Ris1
    Cis = Cis + Cis2
    Ris = Ris + Ris2

    print(Cis1, Ris1)
    print(Cis2, Ris2)
    print(Cis, Ris)

    evalues, evectors = np.linalg.eig(A)

    markers = ['-', '-', '-', 'o', 'o', 'o']
    edgecolors = ['r', 'g', 'b', 'r', 'g', 'b']

    colorlines = []
    for marker, edgecolor in zip(markers, edgecolors):
        colorlines.append(marker + edgecolor)

    Title = "gerschgorins"
    Legend = ['G1', 'G2', 'G3', 'G1', 'G2', 'G3']

    xs, ys = pytool.plot_circles(Cis=Cis, Ris=Ris, colorlines=colorlines,
                                 dTheta=0.1, title=Title, legend=Legend, isplot=False)

    for x, y, colorline in zip(xs, ys, colorlines):
        plt.plot(x, y, colorline, mfc='none')
    plt.grid()
    plt.title(Title)
    plt.axis('equal')
    plt.xlabel('real axis/x')
    plt.ylabel('image axis/y')
    plt.legend(Legend)
    plt.show()
