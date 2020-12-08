import pandas as pd
import matplotlib.pyplot as plt

def VisualizacionCO2 (data1,data2,n=0):
    """
    Parametros:
    data1 -> indoor
    data2 -> outdoor
    n -> 0 --> muestra indoor y outdoor
           --> muestra indoor
           --> muestra outdoor
    """
    if n == 1 :
        fig, axs = plt.subplots(2,2)
        fig.set_size_inches(20,10)
        fig.suptitle('CO2', fontsize=16)

        axs[0, 0].plot(data1["co2_adc_1"], label = 'S3')
        axs[0, 0].plot(data1["co2_adc_2"], label = 'S4')
        axs[0, 0].set( ylabel='adc')
        axs[0, 0].legend(fontsize = 10)
        axs[0, 0].set_title('ADC')

        axs[0, 1].plot(data1["co2_res_1"], label = 'S3')
        axs[0, 1].plot(data1["co2_res_2"], label = 'S4')
        axs[0, 1].set( ylabel='kohm')
        axs[0, 1].legend(fontsize = 10)
        axs[0, 1].set_title('RESISTENCIA' )


        axs[1, 0].plot(data1["co2_ppm_1"], label = 'S3')
        axs[1, 0].plot(data1["co2_ppm_2"], label = 'S4')
        axs[1, 0].legend(fontsize = 10)
        axs[1, 0].set( ylabel='CO2 PPM')
        axs[1, 0].set_title('PPM')


        axs[1, 1].plot(data1["co2_rzero_1"], label = 'S3')
        axs[1, 1].plot(data1["co2_rzero_2"], label = 'S4')
        axs[1, 1].legend(fontsize = 10)
        axs[1, 1].set( ylabel='kohm')
        axs[1, 1].set_title('RESISTENCIA Zero')
        
    elif n == 2 :
        fig, axs = plt.subplots(2,2)
        fig.set_size_inches(20,10)
        fig.suptitle('CO2', fontsize=16)

        axs[0, 0].plot(data2["co2_adc_1"], label = 'S3')
        axs[0, 0].plot(data2["co2_adc_2"], label = 'S4')
        axs[0, 0].set( ylabel='adc')
        axs[0, 0].legend(fontsize = 10)
        axs[0, 0].set_title('ADC')

        axs[0, 1].plot(data2["co2_res_1"], label = 'S3')
        axs[0, 1].plot(data2["co2_res_2"], label = 'S4')
        axs[0, 1].set( ylabel='kohm')
        axs[0, 1].legend(fontsize = 10)
        axs[0, 1].set_title('RESISTENCIA' )


        axs[1, 0].plot(data2["co2_ppm_1"], label = 'S3')
        axs[1, 0].plot(data2["co2_ppm_2"], label = 'S4')
        axs[1, 0].legend(fontsize = 10)
        axs[1, 0].set( ylabel='CO2 PPM')
        axs[1, 0].set_title('PPM')


        axs[1, 1].plot(data2["co2_rzero_1"], label = 'S3')
        axs[1, 1].plot(data2["co2_rzero_2"], label = 'S4')
        axs[1, 1].legend(fontsize = 10)
        axs[1, 1].set( ylabel='kohm')
        axs[1, 1].set_title('RESISTENCIA Zero')
        
    else:
        fig, axs = plt.subplots(2,2)
        fig.set_size_inches(20,10)
        fig.suptitle('CO2', fontsize=16)

        axs[0, 0].plot(data1["co2_adc_1"], label = 'S1')
        axs[0, 0].plot(data1["co2_adc_2"], label = 'S2')
        axs[0, 0].plot(data2["co2_adc_1"], label = 'S3')
        axs[0, 0].plot(data2["co2_adc_2"], label = 'S4')
        axs[0, 0].set( ylabel='adc')
        axs[0, 0].legend(fontsize = 10)
        axs[0, 0].set_title('ADC')

        axs[0, 1].plot(data1["co2_res_1"], label = 'S1')
        axs[0, 1].plot(data1["co2_res_2"], label = 'S2')
        axs[0, 1].plot(data2["co2_res_1"], label = 'S3')
        axs[0, 1].plot(data2["co2_res_2"], label = 'S4')
        axs[0, 1].set( ylabel='kohm')
        axs[0, 1].legend(fontsize = 10)
        axs[0, 1].set_title('RESISTENCIA' )


        axs[1, 0].plot(data1["co2_ppm_1"], label = 'S1')
        axs[1, 0].plot(data1["co2_ppm_2"], label = 'S2')
        axs[1, 0].plot(data2["co2_ppm_1"], label = 'S3')
        axs[1, 0].plot(data2["co2_ppm_2"], label = 'S4')
        axs[1, 0].legend(fontsize = 10)
        axs[1, 0].set( ylabel='CO2 PPM')
        axs[1, 0].set_title('PPM')

        axs[1, 1].plot(data1["co2_rzero_1"], label = 'S1')
        axs[1, 1].plot(data1["co2_rzero_2"], label = 'S2')
        axs[1, 1].plot(data2["co2_rzero_1"], label = 'S3')
        axs[1, 1].plot(data2["co2_rzero_2"], label = 'S4')
        axs[1, 1].legend(fontsize = 10)
        axs[1, 1].set( ylabel='kohm')
        axs[1, 1].set_title('RESISTENCIA Zero')
        
def VisualizacionMP (data1,data2,n=0):
    """
    Parametros:
    data1 -> indoor
    data2 -> outdoor
    n -> 0 --> muestra indoor y outdoor
           --> muestra indoor
           --> muestra outdoor
    """
    if n == 1:
        fig, axs = plt.subplots(3)
        fig.set_size_inches(20,10)
        fig.suptitle('Material Particulado', fontsize=16)

        axs[0].plot(data1["pm10_0_au"], label = 'S1')
        axs[0].set( ylabel='PM10 [ug/m3')
        axs[0].legend(fontsize = 10)
        #axs[0].set_title('PM10')

        axs[1].plot(data1["pm2_5_au"], label = 'S1')
        axs[1].set( ylabel='PM2.5 [ug/m3')
        axs[1].legend(fontsize = 10)
        #axs[1].set_title('PM2.5')

        axs[2].plot(data1["pm1_0_au"], label = 'S1')
        axs[2].set(ylabel='PM1 [ug/m3')
        axs[2].legend(fontsize = 10)
        #axs[2].set_title('PM1'
     
    elif n == 2:
        fig, axs = plt.subplots(3)
        fig.set_size_inches(20,10)
        fig.suptitle('Material Particulado', fontsize=16)

        axs[0].plot(data2["pm10_0_au"], label = 'S2')
        axs[0].set( ylabel='PM10 [ug/m3')
        axs[0].legend(fontsize = 10)
        #axs[0].set_title('PM10')

        axs[1].plot(data2["pm2_5_au"], label = 'S2')
        axs[1].set( ylabel='PM2.5 [ug/m3')
        axs[1].legend(fontsize = 10)
        #axs[1].set_title('PM2.5')

        axs[2].plot(data2["pm1_0_au"], label = 'S2')
        axs[2].set(ylabel='PM1 [ug/m3')
        axs[2].legend(fontsize = 10)
        #axs[2].set_title('PM1'
        
    else:
        fig, axs = plt.subplots(3)
        fig.set_size_inches(20,10)
        fig.suptitle('Material Particulado', fontsize=16)

        axs[0].plot(data1["pm10_0_au"], label = 'S1')
        axs[0].plot(data2["pm10_0_au"], label = 'S2')
        axs[0].set( ylabel='PM10 [ug/m3')
        axs[0].legend(fontsize = 10)
        #axs[0].set_title('PM10')

        axs[1].plot(data1["pm2_5_au"], label = 'S1')
        axs[1].plot(data2["pm2_5_au"], label = 'S2')
        axs[1].set( ylabel='PM2.5 [ug/m3')
        axs[1].legend(fontsize = 10)
        #axs[1].set_title('PM2.5')

        axs[2].plot(data1["pm1_0_au"], label = 'S1')
        axs[2].plot(data2["pm1_0_au"], label = 'S2')
        axs[2].set(ylabel='PM1 [ug/m3')
        axs[2].legend(fontsize = 10)
        #axs[2].set_title('PM1')