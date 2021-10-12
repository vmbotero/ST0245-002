import numpy as np
from scipy import misc
from numpy.linalg import norm
from tqdm import trange
from math import sqrt
import imageio

#definimos el meto costura y mapeamos el csv

def costura(ganado_file, area, filtro_imagen = None): 
	ancho   = "ancho" in area
    largo = "largo" in area
    imagen = imageio.imread("Sample.csv Financiera" , "https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/datasets/csv/paraEntrenarYProbarLaIA/enfermo_test_csv/04be43ab919b6b22d950d3b59834f4a1%20(1).csv")
    #filtro_imagen = ""
    filtro_imagen = np.array([[0 for i in range(imagen.shape[1])] for j in range(imagen.shape[0])])
	if type(filtro_imagen) == str 
	else np.copy(filtro_imagen)
    elif largo:
		filtro_imagen = np.transpose(filtro_imagen, (1, 0))
        imagen  = np.transpose(imagen, (1, 0, 2))
        filtro_imagen = np.transpose(filtro_imagen, (1, 0))

# redefinimos el filtro

    filtro_imagen = filtro_imagen.tolist()
    valor_longitud  = imagen.shape[0]
    valor_altitud = imagen.shape[1]
    margen = lambda x, c: x if 0 < x < c else 0 if x <= 0 else c
    scale = [[0 for i in range(valor_altitud)] for j in range(valor_longitud)]
    min = [[0 for i in range(valor_altitud)] for j in range(valor_longitud)]
    mat = [[0 for i in range(valor_altitud)] for j in range(valor_longitud)]
    imagen = imagen.tolist()

        
    for i in range(valor_long):
        for j in range(valor_altitud):
            i_mtx[i][j] = 0.256 * imagen[i][j][0] + 0.587 * imagen[i][j][1] + 0.114 * imagen[i][j][2]

    for i in range(valor_longitud):
        for j in range(valor_altitud):

            mat[i][j] =  filtro_imagen[i][j] * valor_longitud * valor_altitud * 256

            coordenada_x = i_mat[margen(i + 1, valor_longitud - 1)][j] - i_mat[margen(i - 1, valor_longitud - 1)][j]
            coordenada_y = i_mat[i][margen(j + 1, valor_altitud - 1)] - i_mat[i][margen(j - 1, valor_altitud - 1)]
            mat[i][j] += sqrt(coordenada_x ** 2 + coordenada_y ** 2)

            if i > 0:
                mat[i][j] += min(mat[i - 1][margen(j - 1, valor_altitud - 1)], 
                                      mat[i - 1][margen(j    , valor_altitud - 1)],
                                      mat[i - 1][margen(j + 1, valor_altitud - 1)])
    
    i = valor_longitud - 1
    j = np.argmin(mat[i])
    if SHRINK:
        imagen[i].pop(j)
        filtro_imagen[i].pop(j)
    else:
        temporal = [(imagen[i][j][0] + imagen[i][margen(j + 1, valor_altitud - 1)][0]) // 2,
                (imagen[i][j][1] + imagen[i][margen(j + 1, valor_altitud - 1)][1]) // 2,
                (imagen[i][j][2] + imagen[i][margen(j + 1, valor_altitud - 1)][2]) // 2]
        imagen[i].insert(j + 1, temp)
        filtro_imagen[i].insert(j + 1, filtro_imagen[i][j])
    min[i][j] = 1
    while (true):
        compresion = np.argmin((mat[i - 1][margen(j - 1, valor_altitud - 1)], 
                            mat[i - 1][margen(j    , valor_altitud - 1)],
                            mat[i - 1][margen(j + 1, valor_altitud - 1)])) - 1
        j = margen(j + compresion, valor_altitud - 1)
        i -= 1
        if SHRINK:
            imagen[i].pop(j)
            filtro_imagen[i].pop(j)
        else:
            temporal = [(imagen[i][j][0] + imagen[i][margen(j + 1, valor_altitud - 1)][0]) // 2,
                    (imagen[i][j][1] + imagen[i][margen(j + 1, valor_altitud - 1)][1]) //2,
                    (imagen[i][j][2] + imagen[i][margen(j + 1, valor_altitud - 1)][2]) // 2]
            imagen[i].insert(j + 1, temporal)
            filtro_imagen[i].insert(j + 1, filtro_imagen[i][j])
        min[i][j] = 1

    imagen = np.array(imagen, np.dtype('uint8'))
    filtro_imagen = np.array(filtro_imagen, np.dtype('uint8'))
    if VERTICAL:
        imagen = np.transpose(imagen, (1, 0, 2))
        filtro_imagen = np.transpose(filtro_imagen, (1, 0))
        min= np.transpose(min, (1, 0))      
    
    return (imagen, filtro_imagen, min)
