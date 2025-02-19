from datetime import datetime, timedelta
current_date = datetime.now()
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)
print("keshe:", yesterday.strftime("%Y-%m-%d"))
print("bugin:", current_date.strftime("%Y-%m-%d"))
print("erten:", tomorrow.strftime("%Y-%m-%d"))