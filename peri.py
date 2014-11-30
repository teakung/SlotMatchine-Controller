from practicum import McuBoard

RQ_SET_LED    = 0
RQ_GET_SWITCH = 1
RQ_GET_LIGHT  = 2
RQ_SET_OUTLED = 3
RQ_SET_INLED = 4

####################################
class PeriBoard(McuBoard):

    ################################
    def setLed(self, led_no, led_val):
        '''
        Set status of LED led_no on peripheral board to led_val
        '''
        self.usbWrite(RQ_SET_LED,index = led_no,value = led_val)
    #######################################################
    def setoutLed(self, led_no, led_val):
        '''
        Set status of LED led_no on peripheral board to led_val
        '''
        self.usbWrite(RQ_SET_OUTLED ,index = led_no,value = led_val)
    ################################
    def setinLed(self, led_no, led_val):
        '''
        Set status of LED led_no on peripheral board to led_val
        '''
        self.usbWrite(RQ_SET_INLED ,index = led_no,value = led_val)
    #################################
 #    def setLedValue(self, value):
 #        '''
 #        Display value's 3 LSBs on peripheral board's LEDs
 #        '''
 #        self.usbWrite(RQ_SET_LED,index = 2,value = value/2/2)
    # self.usbWrite(RQ_SET_LED,index = 1,value = value/2%2)
    # self.usbWrite(RQ_SET_LED,index = 0,value = value%2)
    ################################
    def getSwitch(self):
        '''
        Return a boolean value indicating whether the switch on the peripheral
        board is currently pressed
        '''
        if(self.usbRead(request = RQ_GET_SWITCH)[0]):
            return True
        else:
            return False
        return self.usbRead(request = RQ_GET_SWITCH)

    # ################################
    # def getLight(self):
    #     '''
    #     Return the current reading of light sensor on peripheral board
    #     '''
    #     return (self.usbRead(RQ_GET_LIGHT,length = 2)[0]+(self.usbRead(RQ_GET_LIGHT,length = 2)[1]*256))
    
