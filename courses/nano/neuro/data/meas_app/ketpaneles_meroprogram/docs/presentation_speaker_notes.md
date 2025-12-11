# Neuromorphic Electronics Presentation: Speaker Notes

## Format 1: Comprehensive Script
*Use this version to practice the flow and narrative. It is written to sound natural, professional, and academically grounded.*

### Slide 1: Introduction
"Good afternoon, everyone. I am Peter Tallosy, and today I will present our laboratory work on **Neuromorphic Electronics**, specifically focusing on the characterization of **Vanadium Dioxide (VO2) Memristors**.

In our measurement session, we explored how these nanoscale devices can emulate the behavior of biological neurons. I will guide you through the motivation behind this technology, the physics of the phase transition we observed, and our experimental results on switching dynamics and oscillatory circuits."

---

### Slide 2: Part 1 - The Challenge and Motivation
"So, why are we researching this? The primary driver is the **energy efficiency gap** between modern computers and the biological brain.

**The Problem (Left):**
Current AI computation faces a severe 'Energy Crisis'. This is largely due to the **von Neumann Bottleneck**. In standard hardware, we waste massive amounts of energy just shuffling data back and forth between the CPU and memory. Recent studies, such as those by **Huang et al.**, highlight that this data movement costs orders of magnitude more energy than the computation itself.

**The Solution (Right):**
The biological brain ($\approx 20W$) solves this by collocating memory and processing.
We can mimic this using a **Memristor Crossbar Array**. As shown in the figure, this architecture places a memory device at every intersection. This allows us to perform **Matrix-Vector Multiplication** in a single analog step using Ohm’s and Kirchhoff’s laws. As **Aguirre et al.** recently demonstrated, this hardware-level parallelism is the key to next-generation efficient AI."

---

### Slide 3: Outline
"My presentation will follow this structure:
First, I will briefly explain the theory behind VO2 physics.
Then, I will walk you through our experimental setup.
The core of the talk will focus on our three key results: the I-V switching, the thermal analysis, and the relaxation dynamics.
Finally, I will conclude with an outlook on future potential."

---

### Slide 3: Theory - Vanadium Dioxide (VO2)
"To build these crossbars, we need a device that acts like a neuron. Our material of choice is **Vanadium Dioxide (VO2)**.

**The Physics:**
VO2 is a strongly correlated material that exhibits an **Insulator-to-Metal Transition (IMT)**.
At room temperature, it is an insulator. But if we heat it above **68°C**—or trigger it electrically—its crystal structure physically changes, and it becomes a conductive metal.

**Why it matters:**
The key property here is **Thermal Hysteresis**. The device heats up to switch ON, but must cool down significantly to switch OFF. This 'lag' creates a volatile memory effect. Unlike non-volatile storage, this device naturally 'forgets' and resets, which is exactly the instability we need to generate voltage spikes similar to biological neuron firing."

---

### Slide 4: Measurement Session Roadmap
"Our lab work was structured into four distinct characterization tasks:

1.  **Circuit Validation:** Verifying the safety of our setup to prevent thermal destruction of the samples.
2.  **I(V) Characterization:** Mapping the voltage-dependent switching thresholds and the hysteresis loop.
3.  **Temperature Dependence:** Physically heating of the sample to prove the thermal origin of the switching.
4.  **Relaxation Dynamics:** Analyzing the time-domain response to specific pulses to evaluate its potential as an oscillator."

---

### Slide 5: Experimental Setup
"Here you can see our experimental arrangement.

We contacted the micron-scale devices using a probe station (shown right).
The circuit topology is simple but vital: **Source $\rightarrow$ Series Resistor $\rightarrow$ VO2**.
I want to emphasize the role of the **Series Resistor ($2.17 k\Omega$)**. Without it, the moment the VO2 switches to metal, the current would run away, leading to permanent breakdown. This resistor limits the current and protects the device. We controlled the entire measurement using a custom automation script via an NI myDAQ."

---

### Slide 6: Result - Voltage-Induced Switching (Task 2)
"Let's look at our first major result: the **Current-Voltage (I-V) Characteristic**.

This 'butterfly' loop is the hallmark of a memristor.
*   **The Sweep:** As we increase voltage from 0V, the device stays insulating (low current).
*   **The Switch:** Around **2.5V**, we see a sharp vertical jump. This is the **SET** transition.
*   **The Hysteresis:** On the way back down, the device stays conductive until a much lower voltage.

Crucially, the loop always closes at 0V. This confirms the device is **volatile**—it doesn't store data permanently like a flash drive, but acts as a dynamic switch, which is essential for neuron emulation."

---

### Slide 7: Result - Time-Dependent Behavior
"To ensure this wasn't just a measurement artifact, we checked the time-domain signals.

**Top Graph:** Our triangular input voltage.
**Bottom Graph:** The current response.

You can see clear, sharp current spikes that align perfectly with the hysteresis thresholds from the previous slide. The repeatability of these spikes confirms that the phase transition is robust and follows a deterministic physical process."

---

### Slide 8: Result - Thermal Phase Transition (Task 3)
"In Task 3, we investigated the underlying mechanism. Is this switching *really* due to a phase change, or just electronic breakdown?

**The 'Thermal Origin':**
We hypothesized that the switching is driven by **Joule heating**. The current heats the device internally until it hits the phase transition temperature.

**The Evidence:**
To prove this, we externally heated the entire chip on a hot plate.
Looking at the data, you can see a massive drop in resistance right around **57-60°C**. This matches the known Insulator-Metal Transition temperature of VO2. This effectively proves that our voltage switching is indeed a **thermal process**: we are electrically driving the material through its physical phase change."

---

### Slide 9: Result - Activation Energy Analysis
"We took this thermal data one step further by performing an **Arrhenius Analysis**.

By plotting the natural log of resistance against inverse temperature ($1/T$), we observed a linear relationship in the insulating state.
In semiconductor physics, this linear slope indicates **thermally activated transport**.
From the slope, we determined that the activation energy is consistent with the standard bandgap of VO2 ($\approx 0.3-0.5 eV$). This confirms that in the 'Off' state, our VO2 sample behaves as a high-quality intrinsic semiconductor."

---

### Slide 10: Result - Relaxation Dynamics (Task 4)
"Finally, we attempted to construct a **Neuristor**—a relaxation oscillator.
By biasing the device in its unstable 'negative differential resistance' region and adding a capacitor, the circuit should self-oscillate.

**The Measurement:**
As you can see in the trace, we successfully captured a **single neuronal spike**. The capacitor charged up, caused the VO2 to switch, and discharged.
However, we faced challenges with stability. We could not sustain a continuous train of oscillations, likely due to thermal drift or degradation. This highlights a key engineering challenge: improving the **endurance** of these nanoscale films for continuous operation."

---

### Slide 11: From Lab to State of the Art - Ising Machines
"While our single oscillator had stability issues, scaling this concept is currently a hot topic in research.

**Connecting to Literature:**
Just this year, **Maher et al. (2024)** demonstrated a massive system of coupled VO2 oscillators on a chip.
They utilize the synchronization dynamics of these oscillators to build an **Ising Machine**. This is a special type of analog computer that can solve NP-hard optimization problems (like Graph Coloring) vastly faster than digital logic. Our lab experiment represents the fundamental unit—the single oscillator—of this cutting-edge architecture."

---

### Slide 12: From Lab to State of the Art - Biological Plausibility
"Furthermore, regarding the 'noise' we observed in our measurements: Task 3 showed some variability in the switching threshold.

**Connecting to Literature:**
**Yi et al.** have shown that this stochasticity in VO2 is actually beneficial. It mimics the noise found in biological ion channels.
In Artificial Neural Networks, this intrinsic noise introduces probabilistic behavior, which helps algorithms escape 'local minima' during learning. Thus, the physical fluctuations in our device make it a **biologically plausible** candidate for stochastic computing."

---

### Slide 13: Conclusion
"To summarize:

1.  We successfully characterized the VO2 memristor, demonstrating a high **On/Off ratio (>1000)** and volatile switching.
2.  We physically verified the **Thermal Origin (IMT)** of the switching mechanism.
3.  We identified the challenge of device endurance, which is the immediate barrier to scaling up.

**Outlook:**
The physics is sound. With improved materials engineering, these devices can enable the large-scale oscillatory neural networks envisioned by researchers like Maher and Yi, moving us closer to truly brain-like hardware."

---

### Slide 14: Acknowledgments
"I would like to thank the **Neuromorphic Electronics Lab Staff** and the **Dept. of Physics at BME** for the opportunity to work on this project. 
Special thanks to my lab partners **Grego & Peti** for their collaboration in these measurements. 

Thank you for your attention."

---
---

## Format 2: Bullet Points (Cues)
*Use this version for quick glances during the actual presentation.*

**Slide 1: Intro**
*   Welcome / Peter Tallosy (K14WR1).
*   Topic: Neuromorphic Electronics & VO2 Memristors.
*   Goal: Emulating biological neurons with hardware.

**Slide 2: Motivation**
*   **Problem:** Energy Crisis / Von Neumann Bottleneck (CPU $\leftrightarrow$ RAM costs energy).
*   **Ref:** Huang et al. (2024).
*   **Solution:** Brain (20W) collocates memory/processing.
*   **Our approach:** Memristor Crossbar Arrays = Analog Matrix-Vector Multiplication.
*   **Ref:** Aguirre et al. (2024).

**Slide 3: Theory (VO2)**
*   **Physics:** Insulator-Metal Transition (IMT) at ~68°C.
*   **Mechanism:** Insulator $\rightarrow$ Heat $\rightarrow$ Metal.
*   **Key:** Thermal Hysteresis = Volatile Memory.
*   **Result:** Instability allows spiking (like neurons).

**Slide 4: Overview**
*   Task 1: Safety/Circuit validation.
*   Task 2: I-V Curves (Switching).
*   Task 3: Thermal Physics (Proving IMT).
*   Task 4: Oscillators (Dynamics).

**Slide 5: Setup**
*   Probe station / NI myDAQ.
*   **Crucial:** Series Resistor (2.17 $k\Omega$) protects sample from burnout!
*   Automated C# measurement.

**Slide 6: I(V) Result**
*   Butterfly Loop = Memristor signature.
*   SET transition ~2.5V (Joule heating).
*   Loop closes at 0V $\rightarrow$ Volatile (Reset).

**Slide 7: Time Domain**
*   Top: Triangle drive. Bottom: Current spikes.
*   Spikes align with thresholds $\rightarrow$ Robust, repeatable physics.

**Slide 8: Thermal Origin**
*   **Q:** Is it really a phase change?
*   **A:** Yes. External heating shows drop at ~60°C.
*   **Conclusion:** Switching is driven by **Thermal Origin** (Joule heating triggers IMT).

**Slide 9: Arrhenius**
*   Plot $\ln(R)$ vs $1/T$.
*   Linear slope = Thermally activated transport.
*   Confirms intrinsic semiconductor behavior in 'Off' state.

**Slide 10: Oscillator**
*   Goal: Neuristor (Relaxation Oscillator).
*   Result: Caught **single spike**.
*   Issue: Stability/Endurance (device degradation).

**Slide 11: Ising Machines (Context)**
*   **Maher et al. (2024):** Large-scale coupled VO2 oscillators.
*   Solves properties like Graph Coloring (NP-hard).
*   Our single oscillator is the building block for this.

**Slide 12: Bio-Plausibility (Context)**
*   **Yi et al.:** Intrinsic noise/stochasticity is good.
*   Mimics biological ion channels.
*   Helps AI escape local minima (Probabilistic computing).

**Slide 13: Conclusion**
*   $\checkmark$ High On/Off ratio (>1000).
*   $\checkmark$ Verified Thermal Origin.
*   **Next step:** Improve endurance for large-scale scaling.
