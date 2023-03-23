import pandas as pd

# data=pd.read_json('data.json')
# d=data.to_string() 
# print(d)
# # print(pd.DataFrame(data))

import mysql.connector
import pandas

empdb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Tout@52',
    database='pythondb'
)

