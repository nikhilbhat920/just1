import time
import threading
import winsound
from funcs_for_play import *
import serial

'''
format of serial data:

1 33.32/n2 32/n3 20.32

1 33.32
2 32
3 20.32
'''

#try uncommenting this below line if it doesnt work
#ser = serial.Serial('COM10',baudrate=9600,timeout=1) 

def check_n_play_S1():
    while(True):
        MC_data=ser.readline()
        mc_Data=str(MC_data)
        mc_D=mc_Data[0:-1]
        u=mc_D.split(" ")
        if(len(u)>1):
            channel_no=u[0]
            channel_value=u[1]
            if(channel_no==1 and channel_value >30):
               winsound.PlaySound("Sound_1",winsound.SND_FILENAME)   

        
def check_n_play_S2():
    while(True):
        MC_data=ser.readline()
        mc_Data=str(MC_data)
        mc_D=mc_Data[0:-1]
        u=mc_D.split(" ")
        if(len(u)>1):
            channel_no=u[0]
            channel_value=u[1]
            if(channel_no==3 and channel_value >30):
               winsound.PlaySound("Sound_2",winsound.SND_FILENAME)

def check_n_play_S3():
    while(True):
        MC_data=ser.readline()
        mc_Data=str(MC_data)
        mc_D=mc_Data[0:-1]
        u=mc_D.split(" ")
        if(len(u)>1):
            channel_no=u[0]
            channel_value=u[1]
            if(channel_no==3 and channel_value >30):
               winsound.PlaySound("Sound_3",winsound.SND_FILENAME)

def main():
    ser = serial.Serial('COM10',baudrate=9600,timeout=1) 
    t1= threading.Thread(target=check_n_play_S1)
    t2= threading.Thread(target=check_n_play_S2)
    t3= threading.Thread(target=check_n_play_S3)
    t1.start()
    t2.start()
    t3.start()

if __name__=="__main__":
    main()

    
