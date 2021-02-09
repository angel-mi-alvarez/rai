#####################################################
####### FUNCIONES GRAFICAS 
#####################################################

#Importante: 
# las funciones incluidas en este librería tienen que incluir la ruta completa de las liberias que usen
# tambien los tipos de datos, p.e. title() tiene que ser plt.title()
# si dieran error de refresco tras hacer cambios en este fichero. Grabar siempre el fichero
# tras hacer las modificacione y si es necesario incluir estas dos lineas en el notebook 
# desde donde se invocarán estas funciones
## %load_ext autoreload
## %autoreload 2
## %matplotlib inplace


# Funcion que muestra un gráfico con la Volatilidad vs Rentabilidad
# para los valores que se pasen en df_valores (campo indice: fecha, precio), 
# pasarle el nombre del fondo y la frecuencia de los periodos de agrupación:
# Quarter, Week, Month, Business day, Daily


import matplotlib.pyplot as plt
import pandas as pd

def grafico_volat_renta(df_valores,nombre_fondo,frecuencia='W'):
    
    # se podría hacer la carga de datos de esta funcion en base al nombre del FI 
    # y el rango de fechas sin embargo no lo vamos ha hacer ya que la libreria de datos
    # no es eficiente invocarla cada vez que se llame y utilizaremos filtros de
    # extraccion de datos de nuestra propia base de datos
    ##
    ##>>>> PODRÍA SER UNA MEJORA POSTERIOR UNA VEZ ACLARADO EL MODELO DE DATOS Y LA FORMA
    ##     DE EXTRACCION DE LOS DATOS
    ##
    #from_date='01/01/2008'
    #to_date='24/01/2009'
    #df_hist1 = investpy.get_fund_historical_data(fund='Rural Mixto Internacional 25 Fi', country='spain', from_date=from_date, to_date=to_date)


    fig, ax = plt.subplots(1, 1)
    agrupRisk=pd.DataFrame(df_valores.Close.resample(frecuencia).std())
    agrupReturn=df_valores.Close.resample(frecuencia).mean().pct_change()

    ax.plot(agrupRisk,color="C0")

    ax2 = ax.twinx()
    ax2.plot(agrupReturn,color="C1")
    #legend(('Return','Risk'),prop = {'size': 10}, loc='lower left')
    plt.title(nombre_fondo+' - Volatility vs Return (Weekly)')
    ax.set_xlabel("Fecha", color="C0")
    ax.set_ylabel("Volatility", color="C0")
    ax.tick_params(axis='x', colors="C0")
    ax.tick_params(axis='y', colors="C0")
    ax2.set_ylabel("Return", color="C1")
    ax2.tick_params(axis='x', colors="C1")
    ax2.tick_params(axis='y', colors="C1")
    plt.show()
    return 0
    
    
