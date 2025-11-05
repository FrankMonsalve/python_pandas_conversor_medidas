import pandas as pd

# Dataframe es la informacion basica con el nombre de las piezas  y centimetros para poder armar el excel

data = {
    "Piezas": ["Pata", "Tablero", "Puerta", "Estante", "Panel lateral" ],
    "Centimetros": [40,120,60,30,180 ], 
}

df = pd.DataFrame(data)

#Guardar el DataFrame en un archivo excel

df.to_excel("muebles_medidas.xlsx", index=False)