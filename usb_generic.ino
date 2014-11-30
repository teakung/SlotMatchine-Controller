#include <Practicum.h>

extern "C" {
#include "usbdrv.h"
}

#define RQ_SET_LED    0
#define RQ_GET_SWITCH 1
#define RQ_GET_LIGHT  2
#define RQ_SET_OUTLED 3
#define RQ_SET_INLED 4

//////////////////////////////////////////////////////////////////////
usbMsgLen_t usbFunctionSetup(uint8_t data[8])
{
  usbRequest_t *rq = (usbRequest_t*)data;
    static uint8_t switch_state;  /* must stay when usbFunctionSetup returns */
    // static uint16_t lightValue;

  // if (rq->bRequest == RQ_SET_LED)
  // {
  //   uint8_t led_val = rq->wValue.bytes[0];
  //   uint8_t led_no  = rq->wIndex.bytes[0];

  //   if (led_no == 0)
  //     digitalWrite(PIN_PC0, led_val);
  //   else if (led_no == 1)
  //     digitalWrite(PIN_PC1, led_val);
  //   else if (led_no == 2)
  //     digitalWrite(PIN_PC2, led_val);

  //   return 0;  // return no data back to host
  // }

  if (rq->bRequest == RQ_GET_SWITCH)
  {
    if (digitalRead(PIN_PC0) == LOW) /* switch is pressed */ 
      switch_state = 1;
    else
      switch_state = 0;

    /* point usbMsgPtr to the data to be returned to host */
    usbMsgPtr = (uint8_t*) &switch_state;

    /* return the number of bytes of data to be returned to host */
    return sizeof(switch_state);
  }
  else if(rq->bRequest == RQ_SET_OUTLED){
    uint8_t led_val = rq->wValue.bytes[0];
    uint8_t led_no  = rq->wIndex.bytes[0];

    if (led_no == 1)
      digitalWrite(PIN_PC1, led_val);
    else if (led_no == 6)
      digitalWrite(PIN_PC2, led_val);
    else if (led_no == 3)
      digitalWrite(PIN_PD5, led_val);
    else if (led_no == 4)
      digitalWrite(PIN_PD1, led_val);
    else if (led_no == 5)
      digitalWrite(PIN_PD0, led_val);
    else if (led_no == 2)
      digitalWrite(PIN_PD6, led_val);

    return 0;

  }
  else if(rq->bRequest == RQ_SET_INLED){
    uint8_t led_val = rq->wValue.bytes[0];
    uint8_t led_no  = rq->wIndex.bytes[0];

    if (led_no == 1)
      digitalWrite(PIN_PB0, led_val);
    else if (led_no == 6)
      digitalWrite(PIN_PB1, led_val);
    else if (led_no == 5)
      digitalWrite(PIN_PB2, led_val);
    else if (led_no == 4)
      digitalWrite(PIN_PB3, led_val);
    else if (led_no == 3)
      digitalWrite(PIN_PB4, led_val);
    else if (led_no == 2)
      digitalWrite(PIN_PB5, led_val);

    return 0;

  }
    // else if(rq->bRequest == RQ_GET_LIGHT){
    //     lightValue = analogRead(PIN_PC4);
    //     usbMsgPtr = (uint8_t*) &lightValue;
    //     return sizeof(lightValue);
        
    // }
  return 0;   /* nothing to do; return no data back to host */
}

//////////////////////////////////////////////////////////////////////
void setup()
{
    pinMode(PIN_PB0, OUTPUT);
    pinMode(PIN_PB1, OUTPUT);
    pinMode(PIN_PB2, OUTPUT);
    pinMode(PIN_PB3, OUTPUT);
    pinMode(PIN_PB4, OUTPUT);
    pinMode(PIN_PB5, OUTPUT);
    pinMode(PIN_PC0, INPUT_PULLUP);
    pinMode(PIN_PC1, OUTPUT);
    pinMode(PIN_PC2, OUTPUT);
    pinMode(PIN_PD0, OUTPUT);
    pinMode(PIN_PD1, OUTPUT);
    pinMode(PIN_PD5, OUTPUT);
    pinMode(PIN_PD6, OUTPUT);

    usbInit();

    /* enforce re-enumeration of USB devices */
    usbDeviceDisconnect();
    delay(300);
    usbDeviceConnect();
}

//////////////////////////////////////////////////////////////////////
void loop()
{
  usbPoll();
}
