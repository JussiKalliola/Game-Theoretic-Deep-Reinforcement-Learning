import pandas as pd
import numpy as np
import os 
import matplotlib.pyplot as plt


def read_data(file_name: str) -> pd.DataFrame:
    try:
        if not os.path.isfile(file_name):
    except ValueError:
        raise ValueError("File not found.")
            

    Data = pd.DataFrame()
    Data = pd.read_csv(file_path,header=None,parse_dates = [1],\
                            names=['vehicle_id', 'order_number', 'time', 'longitude', 'latitude'])
    return Data


def map_viz(Data: pd.DataFrame,
            min_longitude: float, 
            max_longitude: float, 
            min_latitude: float,
            max_latitude: float):

    Beijing = Data[(min_longitude < Data.longitude) & (Data.longitude < max_longitude) & (min_latitude < Data.latitude) & ( Data.latitude < max_latitude)]

    plt.figure(figsize = (9,6), dpi=150)
    #ax1 = plt.subplot2grid((1,2),(0,0))
    plt.hexbin(Beijing.longitude,Beijing.latitude,bins='log', gridsize=600, cmap=plt.cm.hot)   
    plt.axis([116.05, 116.8, 39.5, 40.25])
    plt.title("(a) Data overview in Beijing")
    cb = plt.colorbar()
    cb.set_label('log10(N)')

    #ax2 = plt.subplot2grid((1,2),(0,1))
    #Ring_Road = Data[(116.17 < Data.longitude) & (Data.longitude < 116.57) & (39.76 < Data.latitude) & ( Data.latitude < 40.09)]
    #plt.hexbin(Ring_Road.longitude,Ring_Road.latitude,bins='log', gridsize=600, cmap=plt.cm.hot)   
    #plt.axis([116.17, 116.57, 39.76, 40.09])
    #plt.title("(b) Within the 5th Ring Road of Beijing")
    #cb = plt.colorbar()
    #cb.set_label('log10(N)')

    plt.show()

if __name__ == "__main__":

    dir_name: str = 'CSV/T-Drive/logs/'
    Data = read_data(f"{dir_name}/../trajectories_200802xx.csv")
    map_viz(Data, 116.05, 116.8, 39.5, 40.25)

