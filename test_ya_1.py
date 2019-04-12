import pandas as pd
import numpy as np

#создаёт столбцы rate (доля успешно выполненных заданий) и faluires (кол-во неудач), сортирует по первому

asessors_df = pd.read_csv('D:\\Desktop\\test_ya\\data_task3.csv', sep='\t').set_index('uid')
asessors_df['sucсess'] = np.where(asessors_df['jud'] == asessors_df['cjud'], 1, 0)
asessors_df['tasks'] = 1

asessors_df = asessors_df.drop(['cjud', 'jud', 'docid'], axis=1).groupby(asessors_df.index).sum()

asessors_df['rate'] = asessors_df['sucсess'] / asessors_df['tasks']
asessors_df = asessors_df.sort_values(by=['rate'])
asessors_df['faluires'] = asessors_df['tasks'] - asessors_df['sucсess']


assesors_df.to_csv('asessors_rating.csv', sep = '\t', encoding='utf-8')



