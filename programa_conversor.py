import pandas as pd

def cm_a_pulgadas(cm):
    return cm / 2.54

#leer el archivo excel
df = pd.read_excel("muebles_medidas.xlsx")

#Anadir una columna al DataFrame que sea de pulgadas y se rellene con el calculo de la funcion 

df["Pulgadas"] = df["Centimetros"].apply(cm_a_pulgadas)

df.to_excel("muebles_medidas_pulgadas.xlsx", index=False)

print("Su archivo se convirtio exitosamente")
