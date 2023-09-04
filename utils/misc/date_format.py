import datetime

import pytz


async def date_format(date):
    timezone = pytz.timezone("Asia/Tashkent")
    now = datetime.datetime.now(timezone)
    date_ = str(now.date()).split('-')
    month = date[1]
    day = date[2]
    year = date[0]
    date_1 = str(date).split('/')
    month1 = date_1[1]
    day1 = date_1[0]
    year1 = date_1[2]
    if int(day) <= int(day1):
        if int(month) <= int(month1):
            if int(year) <= int(year1):
                return True


