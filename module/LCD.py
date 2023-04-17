
import smbus2
import time
import numpy as np

I2CADDR = 0x38   	# valid range is 0x20 - 0x27
PULUPA = 0x0F		# PullUp enable register base address
PULUPB = 0xF0		# PullUp enable register base address


mobile =  np.array([])


Key_Debouce={
        'lastSteadyState' : 0,
        'lastFlickerableState ': 0 ,
	'currentState':0,
	'lastDebounceTime': 0,
        'DebounceTime': 50
 }

  #Keypad Keycode matrix
KEYCODE  = [['1','4','7','*'], # KEYCOL0
            ['2','5','8','0'], # KEYCOL1
            ['3','6','9','#'], # KEYCOL2
            ['A','B','C','D']] # KEYCOL3

  # Decide the row
DECODE = [0,0,0,0, 0,0,0,0, 0,0,0,1, 0,2,3,0]

  # initialize I2C comm, 1 = rev2 Pi, 0 for Rev1 Pi
i2c = smbus2.SMBus(1)
ch=''
while 1:
  time.sleep(0.01)
  i2c.write_byte(I2CADDR,PULUPA)
  row = i2c.read_byte(I2CADDR)
  ms= round(time.time()*1000)
  Key_Debouce['currentState'] =0
  if (row) != 0b1111:
      i2c.write_byte(I2CADDR,PULUPB)
      col = i2c.read_byte(I2CADDR) >> 4
#      	 print(row,col)
      row = DECODE[row]
      col = DECODE[col]
      ch =(KEYCODE[row][col])
      Key_Debouce['currentState']=1
      if ch == 'D':
        exit()

  if (Key_Debouce.get('currentState') !=Key_Debouce.get('lastFlickerableState')):
      Key_Debouce['lastDebounceTime'] =  ms
      Key_Debouce['lastFlickerableState'] = Key_Debouce.get('currentState')

  if (ms - Key_Debouce.get('lastDebounceTime') >  Key_Debouce.get('DebounceTime')):
     if (Key_Debouce.get('lastSteadyState') == 0 and  Key_Debouce.get('currentState') == 1):
          print("press")

     elif (Key_Debouce.get('lastSteadyState') == 1 and Key_Debouce.get('currentState') == 0):
           print("release")
           mobile = np.append(mobile,[ch])
           print("mobile",mobile)

     Key_Debouce['lastSteadyState'] =  Key_Debouce.get('currentState')



