import pandas as pd

lista_direcciones=["Financial Sample.csv","https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/datasets/csv/paraEntrenarYProbarLaIA/enfermo_test_csv/04be43ab919b6b22d950d3b59834f4a1%20(1).csv"]
lista_imagenes=[]
for direccion in lista_direcciones:
    filename = direccion
    data = pd.read_csv(filename, header= 0 )
    a= data.shape
    b=a[0]
    #print(b)
    #print(data.shape)
    #print (data.head(b))
    
    lista_imagenes.append(data)
    print(lista_imagenes)
    