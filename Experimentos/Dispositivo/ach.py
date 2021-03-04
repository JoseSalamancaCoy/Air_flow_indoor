import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

def cutdata(datas:list,start_date,end_date):
    result = []
    for i in datas:
        mask = (i.index >= start_date) & (i.index <= end_date)
        i=i[mask]
        result.append(i)
    return result

def calidad (ACH):
    if ACH >= 6:
        calidad = 'Ideal'
    elif ACH >= 5 and ACH < 6 :
        calidad = 'Excelente'
    elif ACH >= 4 and ACH < 5:
        calidad = 'Buena'
    elif ACH >= 4 and ACH < 5:
        calidad = 'Mínima'
    elif ACH < 3:
        calidad = 'Baja'
    
    return calidad


def ACH (name:str,time:list):
    """
    Parameters:
    name:str -> Ruta del archivo que se quiere cargar
    """
    start_date = time[2]
    end_date = time[3]
    data = pd.read_csv(name)
    data.index = pd.DatetimeIndex(data.timestamp)
    data = data.resample('1T').mean()

    data_1 = cutdata([data],time[0],time[1])[0]
    data_2 = cutdata([data],time[4],time[5])[0]
    data = cutdata([data],start_date,end_date)[0]

    c_ambient = np.mean(np.array([float(data_2.CO2.mean()), float(data_1.CO2.mean())]))

    aux = int(list(np.where(data['CO2'] == float(data.CO2.max())))[0])
    c_star =float(data.CO2.max())
    t_star = data[data['CO2']== c_star].index.tolist()[0]
    c_end = c_ambient +  0.37 * (int(data.max() - c_ambient))
    t_end = data[aux:][data['CO2'][aux:] <= c_end].index.tolist()[0]

    ACH =  (-1 * np.log((c_end-c_ambient)/(c_star - c_ambient)))/((t_end -t_star).seconds / 3600)


    plt.figure(figsize=(18,6))
    plt.gcf().autofmt_xdate()
    plt.plot(t_star,c_star, color = 'Green', marker = 'o', markersize = 10)
    plt.plot(t_end,c_end, color = 'r', marker = 'o', markersize = 10)
    plt.plot(data.CO2)
    plt.annotate(str(t_star) + ':' + str(c_star) + ' ppm', (t_star + pd.Timedelta(minutes = 2), c_star ))
    plt.annotate(str(t_end) + ':' + str(c_end) + ' ppm', (t_end  + pd.Timedelta(minutes = 2), c_end  ))
    plt.ylabel('CO2 [ppm]', fontsize = 16)
    plt.xlabel('Tiempo', fontsize = 16)
    plt.show()

    print( 'Calidad:', calidad(ACH), ', ACH:', ACH)
    return (calidad(ACH),ACH,c_ambient)