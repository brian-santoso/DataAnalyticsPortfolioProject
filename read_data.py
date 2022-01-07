import pandas as pd
from datetime import datetime

# Load Usage data
with open('App_usage_trace.txt') as f:
    lines = f.readlines()
    df = []
    for line in lines:
        data = line.split()
        df.append(data)
usage = pd.DataFrame(df, columns=['uid','timestamp', 'loc', 'app_id','traffic'])
usage['traffic'] = usage['traffic'].astype('float64') / 1e6 # Convert traffic to MB
usage['timestamp'] = usage['timestamp'].apply(lambda x: datetime.strptime(x, "%Y%m%d%H%M%S")) # Convert to datetime object

# Load App2Category data
with open('App2Category.txt') as f:
    lines = f.readlines()
    df = []
    for line in lines:
        data = line.split()
        df.append(data)
app2cat = pd.DataFrame(df, columns=['app_id','cat_id'])

# Load base station POI data
base_poi = pd.read_csv("base_poi.txt", delimiter='\t')

print("< ---- Basic information ---- >")
print("- {} base stations".format(base_poi.shape[0]))

#Done