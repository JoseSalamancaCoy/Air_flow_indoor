import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

from scipy.ndimage import gaussian_filter1d
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sfm 

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------

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

def LinearModel(variables,porcentage):
    """
    Parameters:
        - Variables:list -->
        - Porcentage:float  --> 
    

    Returns:
        - RMSE:float --> mean square error
        - coefficients:list --> 
        - Intercept:float  -->  
    """

    Y = variables[0]
    X = pd.DataFrame({str(i):variables[i] for i in range(1,len(variables))})
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = porcentage, random_state=9)
    lin_reg_mod = LinearRegression()
    lin_reg_mod.fit(X_train, y_train)
    pred = lin_reg_mod.predict(X_test)
    test_set_rmse = (np.sqrt(mean_squared_error(y_test, pred)))
    coef = lin_reg_mod.coef_
    intercept = lin_reg_mod.intercept_
    Yc = sum([variables[i] * coef[i-1] for i in range(1,len(variables))] ) + intercept
    return lin_reg_mod.coef_, lin_reg_mod.intercept_ , Yc
    #return Yc
    



def ACH (data,col,start_date,interim_date,end_date):
    """
    Parameters:
    name:str -> Ruta del archivo que se quiere cargar
    start_date:str -> Momento desde donde quiere iniciar a visualizar
    interim_date:str -> Momento en el que inicia la prueba
    end_date:str -> Momento hasta donde quiere visualizar
    """
    data.index = pd.DatetimeIndex(data.index)
    data1 = cutdata([data],start_date,end_date)[0]
   
    data = cutdata([data],interim_date,end_date)[0]

    c_ambient = 400 #np.mean(np.array([float(data_2.CO2.mean()), float(data_1.CO2.mean())]))

    aux = list(np.where(data.iloc[:,col] == float(data.iloc[:,col].max()))[0])[0]
    c_star =float(data.iloc[:,col].max())
    t_star = data[data.iloc[:,col]== c_star].index.tolist()[0]
    c_end = c_ambient +  0.37 * (int(data.iloc[:,col].max() - c_ambient))
    t_end = data[aux:][data.iloc[:,col][aux:] <= c_end].index.tolist()[0]

    ACH =  (-1 * np.log((c_end-c_ambient)/(c_star - c_ambient)))/((t_end -t_star).seconds / 3600)


    plt.figure(figsize=(18,6))
    plt.gcf().autofmt_xdate()
    plt.plot(t_star,c_star, color = 'Green', marker = 'o', markersize = 10)
    plt.plot(t_end,data.iloc[:,col][t_end], color = 'r', marker = 'o', markersize = 10)
    plt.plot(data1.iloc[:,col])
    #plt.plot(data.index, [c_ambient for i in range(len(data.index))], color = 'k' )
    plt.annotate(str(t_star) + ':' + str(round(c_star,2)) + ' ppm', (t_star + pd.Timedelta(minutes = 0), c_star ))
    plt.annotate(str(t_end) + ':' + str(round(c_end,2)) + ' ppm', (t_end  + pd.Timedelta(minutes = 0), c_end  ))
    plt.ylabel('CO2 [ppm]', fontsize = 16)
    plt.xlabel('Tiempo', fontsize = 16)
    plt.show()

    print( 'Calidad:', calidad(ACH), ', ACH:', ACH)
    #return (calidad(ACH),ACH,c_ambient)