import pandas as pd

# 读取 Excel 文件
excel_data = pd.read_excel('./data.xlsx', sheet_name='Sheet1')
# 将数据转换为字典列表
data_list = excel_data.to_dict(orient='records')

# 打印字典列表
for data in data_list:
    data['Note'] = [x for x in data['Note'].split(',')]
    print(data)
