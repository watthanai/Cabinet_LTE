import keyboard
import time
import numpy as np
import csv
from datetime import datetime







def Keypad():
    mobile=[]
    Key_Debouce={
        'lastSteadyState' : 0,
        'lastFlickerableState ': 0 ,
	    'currentState':0,
	    'lastDebounceTime': 0,
        'DebounceTime': 50
    }
    

    Key={
	    'Mode' : 'Initial_Mode',
	    'currentValue' : '',
        'MemValue' : '',
    }

    file={
       'Phonenumber':''
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
            if (((Key.get('currentValue') == 'c' and Key.get('Mode')=='Initial_Mode')  or Key.get('Mode')=='Create_Profile') and len(mobile)<10) :
                Key['MemValue']=Key.get('currentValue')
                Key['Mode']='Create_Profile'

                if (Key.get('MemValue')=='*' or Key.get('MemValue')=='#' or Key.get('MemValue')=='a' or Key.get('MemValue')=='b' or Key.get('MemValue')=='c'or Key.get('MemValue')=='d' ):
                    
                    if(Key.get('MemValue')=='d'):
                       mobile=[]
                       print("mobile",mobile)
                  

                else: 
                    mobile = np.append(mobile,Key.get('MemValue'))
                    print("mobile",mobile,len(mobile)) 

            if (len(mobile)== 10 and Key.get('currentValue') == 'c' ):
                file['Phonenumber'] = ''.join([str(elem) for elem in mobile]) 
                DateCreate = datetime.now().strftime('%Y%m%d_%H%M%S')
                csv_name=file.get('Phonenumber')+"_"+DateCreate +".csv"
                print(csv_name)
                
                myFile = open((r'D:\python_LTE\I2C\Data_logger\{}').format(csv_name), 'w')
                with myFile:
                     header = ['No.','Stock','Price','Change (Bath)','%Change (%)']
                     writer = csv.DictWriter(myFile, fieldnames=header) 
                     writer.writeheader()



                Key['MemValue']=''
                Key['Mode']='Initial_Mode'
                mobile=[]

                
       
          
   

def main():
  
  while 1:
    Keypad()

   
if __name__ == '__main__':
  main()
