import datetime
date1= datetime.date(2021,2,3)
print('Date print with specific syntax: ',date1.strftime('%A,%B,%C,%D'))

date_text = 'January-20 and year 1954'
date_formated= datetime.datetime.strptime(date_text,'%B-%d and year %Y')
print ('Date read from text: ',date_formated)

print('Now: ', datetime.datetime.now())

date3= datetime.datetime(2020,1,1)
date4= datetime.datetime.now()
rem_time=date4-date3
print('Remaining days: ',rem_time.days)