# Electronics lab: M3 Comparators

Gregorio Jaca, Peter Tallosy
2025.11.06.

## TASKS:

general:
ua741opamp

### 1. Build the comparator circuit

U_2 is input voltage 9.94V potentiometer
R_1 = 22k ohm
R_2 = 10k ohm

common ground for all voltages U*1, U*-, U*+ (their values have the same reference point)
U_1_calculated = (voltage divider formula) = U*+ _ (R2 / (R_1 + R_2)) = (5V) _ (10k ohm / (22k ohm + 10k ohm)) = 1.56V

U_2 < 1.5V -> U_out = 4.47V
U_2 > 1.5V -> U_out = -3.14V (=-pi)

U_1 = constant 1.575V
(if U_2 goes above 5V then
u-1 is no longer constant)

### 2. Modified the circuit

R_3 = 99.5k ohm (should be 100kohm)

hysterisis: increase: U_thres = 1.85, decrease: U_thres = 1.25V (+-0.05V)
U_histerisis = 0.6V

U_2 < 1.5V -> U_out = 4.36V
U_2 > 1.5V -> U_out = -3.14V (=-pi)

U_1 (U_out > 0) = 1.273V constant
U_1 (U_out < 0) = 1.754V constant

There is also hysterisis for the value of U_1

if U_2 > 5 (supply voltage) -> U_1 increases with U_2 (end of saturation region for U_in)

### 3. Relaxation oscillator

time constant tau = T = 2 _ R1 _ C \* ln((U*+ + U_switch1-2) / (U*+ - U_switch2-1))

R_1 = 10 kΩ, R_2 = 10 kΩ, and R_3 = 22 kΩ.

we want oscillation frequency f = 1 / tau = 12 kHz

C = 1 / (f \* R1) = 8.3333 nF

C*desired = T / (2 * R1 _ ln((U_+ + U*2) / (U*+ + U*1))) = 1 / (2 * 10kHz \_ 10k ohm \* ln((5V + 1.85V) / (5V - 1.25V)))
= 6.915712 nF

C*lit = 6.8 nF
-> tau_expected = (2 * C*lit * R_1 \* ln(U*+ + U*switch1-2) / (U*+ - U_switch2-1))
= 2 * 6.8nF \_ 10kohm \* ln((5V + 1.85V) / (5V - 1.25V)) = 81.9390
tau smaller
freq higher (f_expected = 12.2142 kHz)

triggering didnt work, freq super unstable -> solved: the two resistors, the power supply was off

using TL071:

no stray

using ua741opamp:

f_meas = 8.2 kHz (32.87% decrease) -> can be explained by inverse relationship between C and f
-> C increased (compared to desired) -> reason: stray capacitances in the op-amp and resistors

### 4. Transistor Schmitt

T1 = T2 = BC182

resistor-emmiter 81 ohms
other ones are close (without 1% of the described values in the handout)

there should be hysterisis but we dont get it

calculated values

U_e = R_e \* I_e =

U_e = 0.112V if below threshold
U_e = 0.089V if above threshold

U_thres1 = U_thres2 = 0.6V

we then got histerisis:
increasing: at U_2 = (0.95+-0.05)V: U_out1 = 0.45V, U_out2 = 5.01V
decreasing: at U_2 = (0.65+-0.05)V: U_out1 = 5.01V, U_out2 = 0.45V
