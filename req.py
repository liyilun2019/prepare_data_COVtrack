import requests
import json

keys=['6f79cd6692a55591d95172847171f00c','b96c9a530e17f21ebb195b335f3d1185']

class Caller:
    def __init__(self, keys):
        self.keys=keys
        self.count=0
        self.key = self.keys[0]
        self.url = {
            'geo': r'https://restapi.amap.com/v3/geocode/geo',
            'convert': r'https://restapi.amap.com/v3/assistant/coordinate/convert',
            'distance': r'https://restapi.amap.com/v3/distance'
        }
    def get_geo(self,address:str,city:str):
        self.count+=1
        if self.count==4000:
            self.key=self.keys[1]
        url=self.url['geo']+f"?key={self.key}&address={address}"
        print(url)
        try:
            r = requests.get(url)
            r.raise_for_status()
            # print(r.json())
            r=r.json()['geocodes'][0]['location']
            loc=r.split(',')
            loc=f'({float(loc[0])},{float(loc[1])});'
            return loc
        except Exception as e:
            print(e)
            raise Exception
            

if __name__=='__main__':
    caller=Caller(keys)
    locs=['磁器口古镇']
    city='北京'
    for l in locs:
        r = caller.get_geo(l,city)
        print(r)
    