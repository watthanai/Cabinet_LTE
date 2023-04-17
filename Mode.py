import time
import numpy as np


def checkmode(ch):
   Key={
      'Mode' : '',
      'currnetValue' : '',
      'MemValue' : '',
   }
   mobile=[]
   Key['currentValue'] = ch
   if (Key.get('currentValue') == 'c' and Key.get('Mode')=='')  or Key.get('Mode')=='state1' :
       Key['MemValue']=Key.get('currentValue')
       Key['Mode']='Screen2'
       if (Key.get('MemValue')=='*' or Key.get('MemValue')=='#' or Key.get('MemValue')=='a' or Key.get('MemValue')=='b' or Key.get('MemValue')=='c'or Key.get('MemValue')=='d' ):
            
            if(Key.get('MemValue')=='d'):
               mobile=[]

       else:
            mobile = np.append(mobile,Key.get('MemValue'))
            return mobile,
          
    #    return (char)



def main():

  while 1:
    ch=input.Keyboard()
    print(ch)

   
if __name__ == '__main__':
  main()