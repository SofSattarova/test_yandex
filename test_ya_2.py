import pandas as pd
import numpy as np
microtasks_df = pd.read_csv('data_task4_old.txt', sep = '\t')

def time_spent (): #создаёт столбец со временем, потраченным ассесором на задачу
    microtasks_df['assigned_ts'] = pd.to_datetime(microtasks_df.assigned_ts) 
    microtasks_df['closed_ts'] = pd.to_datetime(microtasks_df.closed_ts) 
    microtasks_df['time_spent'] = microtasks_df['closed_ts'] - microtasks_df['assigned_ts']


def time_for_microtask (): #вычисляет среднее время выполнения микрозадания в секундах   
    microtasks_df['time_spent'] = microtasks_df['time_spent'] / np.timedelta64(1, 's') / microtasks_df['Microtasks']
    time = microtasks_df['time_spent'].sum () / len(microtasks_df)
    return time

if __name__=='__main__':
    time_spent()
    print (time_for_microtask() / 30, 'N')



