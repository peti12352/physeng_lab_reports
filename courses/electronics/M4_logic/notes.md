# Electronics lab: M4 Digital circuits

Gregorio Jaca, Peter Tallosy
2025.11.06.

## TASKS:

general:
SN74LS00

### Task 1: Black box analysis

a) Apply V_cc = 5V relative to GND

connect inputs A and B to GND (0V) and measure output Y voltage.

V_cc: pin 14
A: pin 1
B: pin 2
Y: pin 3

truth table (csv):
A,B,Y
0,0,1 (4V)
1,0,1 (4V)
0,1,1 (4V)
1,1,0 (0.17V)

-> probably a NOR gate

b) input 1,2 together what happens?

truth table (csv):
X,Y
0,1 (4V)
1,0 (0.17V)
-> NAND gate (single bit)

c) ---

d) f = 1 kHz square wave, amplitude 5V -> determine fall and rise time of output Y wrt input X

f = 1 kHz
Rise time delays (CH2→CH1): 499999.99 ± 0.03 ns
Fall time delays (CH2→CH1): 500000.02 ± 0.05 ns

### Task 2:

a) built

b) truth table (csv) (4-bit):

c)
the least significant digit flips at every change of state
the second most significant digit flips at every two changes of state
the third most significant digit flips at every four changes of state
the most significant digit flips at every eight changes of state
