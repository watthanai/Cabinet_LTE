import keyboard
import time
import numpy as np

def Keyboard():
    mobile=[]
    Key_Debouce={
        'lastSteadyState' : 0,
        'lastFlickerableState ': 0 ,
	    'currentState':0,
	    'lastDebounceTime': 0,
        'DebounceTime': 50
    }
    

    Key={
	    'Mode' : '',
	    'currentValue' : '',
        'MemValue' : '',
    }

    while 1:
        time.sleep(0.01)
        ms= round(time.time()*1000)
        Key_Debouce['currentState']=keyboard.read_key()
        if  Key_Debouce.get('currentState') !=Key_Debouce.get('lastFlickerableState'):
            Key_Debouce['lastDebounceTime'] =  ms
            Key_Debouce['lastFlickerableState'] = Key_Debouce.get('currentState')
        else:
           Key_Debouce['lastFlickerableState'] =0
           
        if (ms - Key_Debouce.get('lastDebounceTime') >  Key_Debouce.get('DebounceTime')):

            Key['currentValue']=Key_Debouce.get('currentState')
            return Key['currentValue']
   

def main():
  
  while 1:
    ch=Keyboard()
    print(ch)
   
if __name__ == '__main__':
  main()
