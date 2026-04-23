#ifndef DEBUG_H
#define DEBUG_H

// Comment out the line below to disable debug printing
#define DEBUG_MODE

#ifdef DEBUG_MODE
  #define DEBUG_PRINT(x) Serial.print(x)
  #define DEBUG_PRINTLN(x) Serial.println(x)
  #define DEBUG_BEGIN(baud) Serial.begin(baud)
#else
  #define DEBUG_PRINT(x)
  #define DEBUG_PRINTLN(x)
  #define DEBUG_BEGIN(baud)
#endif

#endif
