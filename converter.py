from pymongo import MongoClient
from datetime import datetime

client = MongoClient(
    'mongodb://unithon_db:qwer1234@ec2-13-124-79-245.ap-northeast-2.compute.amazonaws.com:27017/unithon_db').unithon_db

#
# client.daily_report.insert_one()

with open('./data/kamis.txt', 'r', encoding='UTF-8') as file:
    item_price = []
    for line in file.readlines():
        if len(item_price) == 3:
            price_list = item_price[2].strip().split(sep='\t')[1:]
            for idx, date in enumerate(item_price[1].strip().split(sep='\t')[1:]):
                month, day = date.strip().split(sep='/')

                result = client.daily_report.insert_one({
                    'time_stamp': datetime(year=2018, month=int(month), day=int(day)).timestamp(),
                    'datetime': '%d-%02d-%02d' % (2018, int(month), int(day)),
                    'code': item_price[0].strip(),
                    'unit': 'kg',
                    'price': float(price_list[idx].replace(',', ''))
                })
                print(result)
            item_price.clear()
        else:
            item_price.append(line)

