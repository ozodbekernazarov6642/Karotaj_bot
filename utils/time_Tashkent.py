import datetime
import pytz


async def time():
    # O'zbekistan vaqti uchun timezone ni aniqlash
    timezone = pytz.timezone("Asia/Tashkent")

    # Ayni damdagi vaqtni olish
    now = datetime.datetime.now(timezone)
    time1 = str(now).split('.')
    return time1[0]

