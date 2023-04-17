import serial
import KeyIn as input
ch=''
message=0
def init():
    ser = serial.Serial(
        port='COM5',
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )
    ser.timeout = 2   
    return ser

def comman(ch,ser,message):
   if ch=='1':
        ser.dtr = False
        tx = 'AT\r'
        ser.write(tx.encode())
        char=ser.read_until(expected=b'\x00')
        # print(ch,tx,char)
        return (char)
   
   if ch=='2':
        ser.dtr = False
        tx = 'AT+COPS?\r'
        ser.write(tx.encode())
        char=ser.read_until(expected=b'\x00')
        # print(ch,tx,char)
        return (char)
   
   if message==1:
        ser.dtr = False
        tx = 'AT\r'
        ser.write(tx.encode())
        char=ser.read_until(expected=b'\x00')
        if char != '' :
          ser.dtr = False
          tx = 'AT+QURCCFG="urcport","uart1"\r'
          ser.write(tx.encode())
          char=ser.read_until(expected=b'\x00')
          if char != '' :
              ser.dtr = False
              tx = 'AT+CMGF=1\r'
              ser.write(tx.encode())
              char=ser.read_until(expected=b'\x00')
              if char != '' :
                  ser.dtr = False
                  tx = 'AT+CMGS="0958069493"\r'
                  ser.write(tx.encode())
                  char=ser.read_until(expected=b'\x00')
                  if char != '' :
                    ser.dtr = False
                    tx = 'Alarm250'
                    ser.write(tx.encode())
                    char=ser.read_until(expected=b'\x00')  
                                 
                    return (char)
   
   if ch=='5' and message==0:
        ser.dtr = False
        tx = 'AT\r'
        ser.write(tx.encode())
        char=ser.read_until(expected=b'\x00')
        if char != '' :
          ser.dtr = False
          tx = 'ATD0958069493;\r'
          ser.write(tx.encode())
          char=ser.read_until(expected=b'\x00')
          return (char)
   
   if ch=='q':
      exit()

        


def main():
  ser=init()
  print("Connected to"+ ser.portstr)
  while 1:
    ch=input.Keyboard()
    print(ch)
    if ch =='5':
      message=0
      respone=comman(ch,ser,message)
      # print(respone)
      message=1
      if message==1:
        respone=comman(ch,ser,message)
        # print(respone)
    else:
      message=0 
      respone=comman(ch,ser,message)
      print(respone)
  

   
if __name__ == '__main__':
  main()

