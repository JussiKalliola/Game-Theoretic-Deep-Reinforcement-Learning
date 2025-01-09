import pandas as pd
import sys
import pathlib
import os
sys.path.append(str(pathlib.Path(__file__).parent.parent.resolve()))
from Environment.utilities import vehicleTrajectoriesProcessor


def combine_tdrive_trajectories(dir_name: str) -> str:

    if os.path.isfile(f"{dir_name}/../trajectories_200802xx.csv"):
        return f"{dir_name}/../trajectories_200802xx.csv" 

    Data = pd.DataFrame()
    F= []
    f_idx = 0
    for root, dirs, files in os.walk(dir_name):
        for name in files:
            if f_idx >= 5000:
                break
            F.append(os.path.join(root, name))
            f_idx+=1
    D=[]
    for index, file_path in enumerate(F):
        print(f"{index}. File processing...")
        D.append(pd.read_csv(file_path,header=None,parse_dates = [1],\
                            names= ['vehicle_id', 'time', 'longitude', 'latitude']))


    Data=Data.append(D,ignore_index=True)
    Data.drop_duplicates(inplace=True)
    Data.dropna(inplace=True)

    Data['time'] = pd.to_datetime(Data['time'], format="%Y-%m-%d %H:%M:%S")
    Data['time'] = Data['time'].view(int)//1e9
    
    Data["order_number"] = 0
    Data = Data[['vehicle_id', 'order_number', 'time', 'longitude', 'latitude']]

    print("Saving data to a path.")
    # Combined dataframe saved to root folder
    Data.to_csv(f"{dir_name}/../trajectories_200802xx.csv")
    return f"{dir_name}/../trajectories_200802xx.csv"

if __name__ == "__main__":
    """Convert T-Drive trajectory dataset into suitable format."""
    trajectories_dir_name: str = 'CSV/T-Drive/logs/'
    out_file_name = combine_tdrive_trajectories(trajectories_dir_name)
    longitude_min: float = 116.4000
    latitude_min: float = 39.90
    trajectories_time_start: str = '2008-02-03 07:00:00'
    trajectories_time_end: str = '2008-02-03 19:00:00'
    trajectories_out_file_name: str = 'CSV/T-Drive/trajectories_20080203_0700_0900'
    edge_number: int = 9
    communication_range: float = 500
    
    processor = vehicleTrajectoriesProcessor(
        file_name=out_file_name, 
        longitude_min=longitude_min, 
        latitude_min=latitude_min,
        edge_number=edge_number,
        map_width=3000.0,
        communication_range=communication_range,
        time_start=trajectories_time_start,
        time_end=trajectories_time_end, 
        out_file=trajectories_out_file_name,
    )    
