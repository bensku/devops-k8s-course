import datetime
import time

while True:
    last_time = datetime.datetime.now()
    with open('/var/shared/time', 'w') as f:
        f.write(str(last_time))
    time.sleep(5)