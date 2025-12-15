# Microcontroller Programming Lab - Data Collection

## Circuit Setup

- Microcontroller: PIC18F2620
- Clock frequency: Fosc = 8 MHz
- Supply voltage: [measured] V
- LED: [type/color], forward voltage: [V]
- Series resistor: [value] Ω
- Potentiometer: 10 kΩ

## Task 1: LED Current

we are using a oscilloscope to measure the voltage across the LED and the resistor.

- V_LED: 1.88 [V] (across the LED)
- V_res: 2.96 [V] (across the resistor)
- V_res_LED: 3.4 [V] (across the resistor and LED)
- V_supply: 5.00 [V]
- R: 270 [Ω]
- I_calculated: 7.03 [mA] # V_res / R
- I_measured: [mA]
- Method: [multimeter/oscilloscope]

## Task 2: Square Wave Period (Initial)

- Period T: 1054 [ms]
- t_high: 526 [ms]
- t_low: 528 [ms]
- Duty cycle: 50 [%] # formula: t_high / T
- Frequency: 0.95 [Hz] # formula: 1 / T

## Task 3: Delay Variation (second delay)

### Delay = [original value] # task 2 values

### Delay = 25.000

- f = 1.39 [Hz], t_high: 270 [ms], t_low: 530 [ms]

### Delay = 100.000 # expected: delay will essentially be shorter than expected or erratic

- f: 1.27 [Hz], t_high: 365 [ms], t_low: 525 [ms] (lower than expected, if we use 10000 mod 65535 = 34464 we get the same value <-> overflow)

## Task 4: Timer0

- T0CON: 0b00000011

- f = 0.95 [Hz], t_high: 530 [ms], t_low: 530 [ms]

## Task 5: T0CON Change

- T0CON = 0b10000011:
  T = 1.05 [ms],
  f = 0.95[Hz]
- T0CON = 0b10000100:
  T = 2.11 [ms],
  f = 0.47 [Hz] # half
- Difference: [explanation]

## Task 6: PWM (50% Duty Cycle)

this was with the oscillosvope probe on LED

- PR2: 0xF9 [value]
- CCPR2L: 125[value]
- Prescaler: 16
- f_calculated: [Hz] # formula: 1 / (T \* 16)
- f_measured: 497.5 [Hz]
- T = 2.01 [ms]
- Duty cycle measured: 50 [%] # formula: CCPR2L / PR2, 1.01/2.01

with the oscilloscope probe on RC1, it gives the same stuff

### PWM Frequency Calculation:

Given:

- System clock: F_osc = 8 MHz
- Timer2 prescaler: 16
- PR2 = 0xF9 = 249

PWM period formula (from datasheet):

- T_PWM = [(PR2) + 1] × 4 × T_osc × (TMR2 prescaler)

Calculation:

- T_osc = 1 / F_osc = 1 / (8 × 10^6) = 125 ns
- T_PWM = (249 + 1) × 4 × 125 ns × 16 = 2000 μs = 2.0 ms
- f_PWM = 1 / T_PWM = 1 / 2.0 ms = 500 Hz

measured and calculated are the same: 497.5 Hz (0.5% error)

## Task 7: PWM Variation + A/D

### PWM Duty Cycle Variation

- CCPR2L = 25:
  t_high = 210 [us]
  T = 2.01 [ms]
  f = 497.5 [Hz]
  duty cycle calc = [%], measured = [%]

- CCPR2L = 225: (inverted high and low times)
  t_high = 420 [us]
  T = 1.81 [ms]
  f = 497.5 [Hz]
  duty cycle calc = [%], measured = [%]

### A/D Integration

- CCPR2L = AD_value / 4.1:
  t_high = 1.3 [ms]
  T = 2.01 [ms]
  f = 497.5 [Hz]
  duty cycle calc = [%], measured = [%]
- Potentiometer middle position: 5.14 [V]
- LED brightness observation: increasing resistance -> increasing duty cycle (t_high increases) -> increasing brightness

## Task 8: A/D Calibration (get data from other group)

| V_in [V] | AD_value (calc) | CCPR2L (calc) | Duty Cycle (calc) [%] | Duty Cycle (meas) [%] | Error [%] |
| -------- | --------------- | ------------- | --------------------- | --------------------- | --------- |
| 0.0      |                 |               |                       |                       |           |
| 0.5      |                 |               |                       |                       |           |
| 1.0      |                 |               |                       |                       |           |
| 1.5      |                 |               |                       |                       |           |
| 2.0      |                 |               |                       |                       |           |
| 2.5      |                 |               |                       |                       |           |
| 3.0      |                 |               |                       |                       |           |
| 3.5      |                 |               |                       |                       |           |
| 4.0      |                 |               |                       |                       |           |
| 4.5      |                 |               |                       |                       |           |
| 5.0      |                 |               |                       |                       |           |

## Observations & Notes

- [Any unexpected behavior]
- [Sources of error]
- [Comparison between methods]
