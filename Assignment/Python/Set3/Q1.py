import datetime
currentday=datetime.date.today()
yesterday=currentday-datetime.timedelta(days=1)
tomo=currentday+datetime.timedelta(days=1)
print('Yesterday:',yesterday)
print('Today : ',currentday)
print('Tomorrow:',tomo)
