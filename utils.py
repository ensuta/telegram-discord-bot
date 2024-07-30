import datetime

async def log(message):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y:%m:%d:%H:%M:%S")
    print(formatted_time, message)
