ticks = 0
import time

def start(devs, auto = True):
   global ticks
   while True:
      #time.sleep(0.5)
      if not auto:
         input()
      success = True
      for dev in devs:
         success = success and dev.step()
      if success:
         ticks += 1
          
      else:
         break
      
   print("Execução finalizada em", ticks, "passos.")
	
