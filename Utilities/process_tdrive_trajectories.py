import pandas as pd
import sys
import pathlib
import os
sys.path.append(str(pathlib.Path(__file__).parent.parent.resolve()))
#from Environment.utilities import vehicleTrajectoriesProcessor


def combine_tdrive_trajectories(dir_name: str) -> str:
    Data = pd.DataFrame()
    F= []
    for root, dirs, files in os.walk(dir_name):
        for name in files:
            F.append(os.path.join(root, name))
    D=[]
    for index, file_path in enumerate(F):
        D.append(pd.read_csv(file_path,header=None,parse_dates = [1],\
                            names= ['vehicle_id', 'time', 'longitude', 'latitude']))

    Data=Data.append(D,ignore_index=True)
    Data.drop_duplicates(inplace=True)
    Data.dropna(inplace=True)

    # Combined dataframe saved to root folder
    Data.to_csv(f"{dir_name}/../trajectories_200802xx")
    return f"{dir_name}/../trajectories_200802xx"

if __name__ == "__main__":
    """Convert T-Drive trajectory dataset into suitable format."""
    trajectories_dir_name: str = 'CSV/T-Drive/logs/'
    out_file_name = combine_tdrive_trajectories(trajectories_dir_name)
    longitude_min: float = 104.04565967220308
    latitude_min: float = 30.654605745741608
    trajectories_time_start: str = '2008-02-02 11:00:00'
    trajectories_time_end: str = '2008-02-02 11:05:00'
    trajectories_out_file_name: str = 'CSV/T-Drive/trajectories_20080202_1100_1105'
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
