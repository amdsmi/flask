# first install pandas library
# second install requests library
# third install xlsxwriter library
# you can install all of them using pip install

import requests
import json
import pandas as pd

url = "https://www.azki.com/api/product/third/prices?vehicleTypeID=1&vehicleModelID=182091&vehicleBrandID=18&vehicleConstructionYear=1399&thirdDiscountID=2&driverDiscountID=2&oldInsureUsed=false&vehicleUsageID=1&withoutInsure=false&zeroKilometer=false&oldCompanyID=1&oldInsureStartDate=2021-12-21&oldInsureExpireDate=2022-12-21&marketer=false"


def data_loader(url):
    payload = {}
    headers = {
        'deviceID': '7',
        'durationID': '12'

    }
    response = requests.request("GET", url, headers=headers, data=payload)
    my_text = response.text

    files = open('azki.txt', 'w')
    files.writelines(my_text)
    files.close()

    f = open('azki.txt')
    data = json.load(f)

    total_data = {}
    for i in range(len(data)):
        sub_dict = {}
        insurance = data[i]
        name = insurance['title']
        prices = insurance['prices']
        keys = list(prices[0].keys())[:-1]
        for key in keys:
            sub_dict[key] = []
        for j in range(len(prices)):
            price = prices[j]
            for key in keys:
                sub_dict[key].append(price[key])
        total_data[name] = sub_dict

    writer = pd.ExcelWriter('emad_data.xlsx', engine='xlsxwriter')
    for key, values in total_data.items():
        pd.DataFrame(values).to_excel(writer, sheet_name=key)

    writer.save()

if __name__ == '__main__':
    data_loader(url)
