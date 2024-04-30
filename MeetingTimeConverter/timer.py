import datetime as dt
import pytz 

format = '%Y-%m-%d %H:%M:%S %Z%z'

# program to convert from ist to gmt time

dtobj = dt.datetime.now(tz=pytz.timezone('Africa/Accra'))



# current_timezone=pytz.timezone('Africa/Accra')

converted_time =dtobj.astimezone(tz=pytz.timezone('Asia/Kolkata'))

print("GMT time :",dtobj.strftime(format))
print("IST time : ",converted_time.strftime(format))

