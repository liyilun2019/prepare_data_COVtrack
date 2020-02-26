import requests
import json

keys=['1045209d4f9bc833843441ab0c467269']

class Caller:
    def __init__(self, key):
        self.key = key
        self.url = {
            'geo': r'https://restapi.amap.com/v3/geocode/geo',
            'convert': r'https://restapi.amap.com/v3/assistant/coordinate/convert',
            'distance': r'https://restapi.amap.com/v3/distance'
        }
    def get_geo(self,address:str,city:str):
        url=self.url['geo']+f"?key={self.key}&address={address}&city={city}"
        try:
            r = requests.get(url)
            r.raise_for_status()
            r=r.json()['geocodes'][-1]['location']
            # print(r.json())
            loc=r.split(',')
            loc=(float(loc[0]),float(loc[1]))
            return loc
        except Exception as e:
            print(e)
            raise Exception
            

if __name__=='__main__':
    caller=Caller(keys[0])
    locs=['北京市朝阳区阜通东大街6号','紫竹院街道鑫德嘉园','鑫德嘉园','天安门']
    city='北京'
    for l in locs:
        r = caller.get_geo(city,l)
        print(r)
    