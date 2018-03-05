import requests
import json
import numpy as np
import pandas as pd

# api-endpoint
url = 'https://api.tradegecko.com/orders'
bearer = {'Authorization': 'Bearer f4855aebc4a92c0d6a09f07b105bcbae81afbaf8cb1344f47a5b5c45cf8f4c1e'}
r = requests.get(url, headers=bearer).json()

print(pd.read_json(r))
