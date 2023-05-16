import datetime
import time
import schedule
import screen_brightness_control as sbc

set_low = False
set_high = False

def set_brightness():
	global set_low, set_high
	print("set_brightness")
	now = datetime.datetime.now().time()
	if now >= datetime.time(23, 0) or now < datetime.time(7, 0):
		if not set_low:
			print("Set brightness to 0")
			sbc.set_brightness(0, display=0)
			set_low = True
			set_high = False
	else:
		if not set_high:
			print("Set brightness to 100")
			sbc.set_brightness(100, display=0)
			set_high = True
			set_low = False

# Schedule the function to run every minute
schedule.every(1).minutes.do(set_brightness)

def main():
	while True:
		# Run scheduled tasks
		schedule.run_pending()
		# Wait for 5 second before checking again
		time.sleep(5)
		
main()