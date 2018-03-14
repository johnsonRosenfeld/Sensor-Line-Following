import RoboPiLib as RPL
import setup
import multiprocessing
import time

#Reading Analog Distance

DistA = (500 * RPL.analogRead(0))/1024
DistB = (500 * RPL.analogRead(1))/1024

#Setting True and False Distance
True = (DistA > 150) and (DistB > 150)
False = (DistA <= 149) and (DistB <= 149)

#All the important moving
while 1:

    if(DistA==True and DistB==True): #both while move forward
        print "IT GOES STRAIGHT!"
        RPL.servoWrite(0,2000)
        RPL.servoWrite(1,1000)

    elif(DistA==True and DistB==False): #turn right
        print "IT TURNS RIGHT!"
        RPL.servoWrite(0,0)
        RPL.servoWrite(1,1000)

    elif(DistA==False and DistB==True): #turn left
        print "IT TURNS LEFT!"
        RPL.servoWrite(0,2000)
        RPL.servoWrite(1,0)

    else:  #stay still
        print "IT CAN STAND STILL!"
        RPL.servoWrite(0,0)
        RPL.servoWrite(1,0)
