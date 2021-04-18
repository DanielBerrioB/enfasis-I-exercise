import datetime
import grequests
import numpy as np
import time

class CovidDataService:
    def __init__(self):
        self.api_url = 'https://api.covid19api.com/dayone/country/'      

    def get_countries_data(self, countries = []):
        response = (grequests.get(self.api_url + country) for country in countries)
        data = np.array(grequests.map(response)).flatten()

        result = []

        for i in data:
            for res in i.json():
                result.append(res)

        return result
        
    def get_countries_historic_data(self, countries, start_date, end_date):
        start_date_parsed = time.mktime(datetime.datetime.strptime(start_date,"%Y-%m-%d").timetuple())
        end_date_parsed = time.mktime(datetime.datetime.strptime(end_date,"%Y-%m-%d").timetuple())

        response = (grequests.get(self.api_url + country) for country in countries)
        maped_response = np.array(grequests.map(response)).flatten()

        response = []

        for i in maped_response:
            for res in i.json():
                response.append(res)

        result = []

        for data in response:
            data_date = time.mktime(datetime.datetime.strptime(data["Date"],"%Y-%m-%dT%H:%M:%SZ").timetuple()) 

            if (data_date <= end_date_parsed and data_date >= start_date_parsed):
                result.append(data)
        
        return result