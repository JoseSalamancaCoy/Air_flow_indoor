import yaml
import pandas as pd
__config = None

def config(Experimento):
    global __config
    if not __config: #Solo accede a disco si no ha sido cargado el archivo de config.yaml
        with open(Experimento + "/config.yaml",mode='r') as f:
            __config = yaml.load(f)
    return __config

def get_medicion(data,variable):
    mask = ~data[variable].isna()
    return pd.concat([data['fecha_hora_med'][mask],  data[variable][mask] ] , axis=1) 