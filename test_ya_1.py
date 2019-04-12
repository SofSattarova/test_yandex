import pandas as pd
import numpy as np

#создаёт столбцы rate (доля успешно выполненных заданий) и faluires (кол-во неудач), сортирует по первому

assesors_df = pd.read_csv('D:\\Desktop\\test_ya\\data_task3.csv', sep='\t').set_index('uid')
assesors_df['sucсess'] = np.where(assesors_df['jud'] == assesors_df['cjud'], 1, 0)
assesors_df['tasks'] = 1

assesors_df = assesors_df.drop(['cjud', 'jud', 'docid'], axis=1).groupby(assesors_df.index).sum()

assesors_df['rate'] = assesors_df['sucсess'] / assesors_df['tasks']
assesors_df = assesors_df.sort_values(by=['rate'])
assesors_df['faluires'] = assesors_df['tasks'] - assesors_df['sucсess']


assesors_df.to_csv('assesors_rating.csv', sep = '\t', encoding='utf-8')



