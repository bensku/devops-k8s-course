import datetime
import time
import uuid

random_str = str(uuid.uuid4())

while True:
    print(datetime.datetime.now(), random_str, flush=True)
    time.sleep(5)