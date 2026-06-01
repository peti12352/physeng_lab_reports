# Oral Presentation Rehearsal Script & Practice Bullet Points

This practice script provides a slide-by-slide set of spoken bullet points to rehearse for your oral defense. Each slide includes **visual action prompts** (what to point at or indicate) and **exact, spoken-English bullet points** designed to project physical rigor and absolute confidence before Profs. Csonka, Halbritter, Kurtossy, and Makk.

---

## Part 1: Slide-by-Slide Practice Guide

### Slide 1: Title Slide
* **Visual Action:**
  * Stand tall, look directly at the committee, and click to the first slide.
* **Practice Bullet Points:**
  * Good afternoon, respected professors and colleagues.
  * Today, I will present the characterization of a high-temperature YBCO DC SQUID.
  * This characterization was performed under liquid nitrogen cooling at 77 K in the BME Department of Physics Nanoelectronics Lab.
  * We will cover both single-junction superconducting transport and advanced quantum metrology using Shapiro steps.

### Slide 2: Outline
* **Visual Action:**
  * Quickly walk the committee through the outline, showing you have a clear plan.
* **Practice Bullet Points:**
  * Our talk is structured into five distinct phases:
  * 1. we will review the physical motivation and the theoretical foundation of Josephson junction and SQUIDs.
  * 2. we will discuss our cryogenic setup and our noise mitigation techniques.
  * 3. we will dive into our quantitative transport results, SQUID magnetometry, and mutual inductance calibration.
  * 4. we will present our **step extraction methodology**—Gaussian Kernel Density Estimation with Least-Squares Cross-Validation—to extract Shapiro steps under microwave drive.
  * Finally, we will present our conclusions and outline systematic future improvements.

---

### Divider: Part 1 — Motivation & Theoretical Foundation
* **Visual Action:**
  * Take a slow, deep breath, pause for 3 seconds to let the transition sink in.
* **Practice Bullet Points:**
  * Let's begin with our motivation and the core theoretical physics.

### Slide 3: Motivation — Frontier of High-Sensitivity Quantum Sensing
* **Visual Action:**
  * Point to the textbook schematic (`squide.png`) on the right showing the SQUID loop.
* **Practice Bullet Points:**
  * SQUIDs occupy the absolute **frontier of high-sensitivity magnetometry**.
  * By coupling **macroscopic quantum coherence** with **magnetic fields**, SQUIDs transduce tiny magnetic flux changes into measurable micro V signals.
  * This extreme sensitivity is used in biomedical Magnetoencephalography (MEG) to map brain activity...
  * ...and in scanning SQUID-on-Tip microscopy to image nano-spins and thermal dissipation at the single-electron level.
  * Today, we demonstrate how this **transduction** behaves in high-Tc grain-boundary junctions.

### Slide 4: Theoretical Foundation — Josephson Effect
* **Visual Action:**
  * Draw attention to the equations on the slide.
* **Practice Bullet Points:**
  * The heart of a SQUID is the **Josephson junction**: two SCs separated by a thin weak-link barrier (insulator).
  * In Ginzburg-Landau theory, the superconducting condensate is described by a **single wave function**: $\Psi = \sqrt{\rho}e^{i\phi}$.
  * The phase difference $\delta = \phi_1 - \phi_2$ across the barrier governs the transport, yielding the two fundamental Josephson relations:
  * First, the DC relation: $I = I_c \sin\delta$, showing that a **dissipationless supercurrent flows at zero voltage**.
  * Second, the AC relation: $\dot{\delta} = \frac{2\pi}{\Phi_0}V$, showing that a voltage **$V$ drives linear phase evolution**, generating AC microwave current at frequency $\nu_J = 2eV/h$.
  * Differentiating these yields a highly non-linear Josephson inductance: $L_J(\delta) = \frac{\Phi_0}{2\pi I_c \cos\delta}$.
  * This non-linearity is critical in modern quantum computing, where it breaks the harmonic spacing of energy levels to isolate a two-level qubit system.

### Slide 5: Theoretical Foundation — DC SQUID
* **Visual Action:**
  * Indicate the parallel junction geometry on the slide.
* **Practice Bullet Points:**
  * A DC SQUID consists of two Josephson junctions connected in parallel within a closed loop.
  * Macroscopic quantum coherence forces a strict phase constraint around the loop: the difference between phase differences must match the enclosed magnetic flux.
  * This interference modulates the total critical current: $I_{c,\text{SQUID}} = 2I_c |\cos(\pi\Phi/\Phi_0)|$, highly analogous to optical double-slit interference.
  * By applying a constant current bias slightly above $2I_c$, we can transduce flux directly into voltage via the overdamped RCSJ model: $V(\Phi_{\text{ext}}) = \frac{R}{2} \sqrt{I_{\text{bias}}^2 - I_{c,\text{SQUID}}^2}$.
  * The sensitivity is characterized by the transfer coefficient $V_{\Phi} = |\partial V / \partial \Phi|$, which we maximize by biasing at the steepest slope.

---

### Divider: Part 2 — Cryogenic Experimental Setup and Noise Mitigation
* **Visual Action:**
  * Pause for 3 seconds, turning to the experimental side of the talk.
* **Practice Bullet Points:**
  * Next, we present our cryogenic experimental setup and signal processing.

### Slide 6: Cryogenic Experimental Setup
* **Visual Action:**
  * Retrace the physical signal path: Arbitrary Waveform Generator $\to$ Probe submerged in Liquid Nitrogen $\to$ Preamp $\to$ Scope.
* **Practice Bullet Points:**
  * Our YBCO grain-boundary bicrystal DC SQUID is mounted inside a sample holder probe.
  * This probe is submerged directly in a liquid nitrogen thermostat to reach the 77 K superconducting phase.
  * We apply a sweeping bias current using an AWG driven through a $10\text{ k}\Omega$ pre-resistor, establishing current-bias mode.
  * The SQUID output voltage is amplified by a low-noise, home-built differential amplifier with a gain of $1000\times$.
  * The amplified signal is filtered and read out on an Owon digital oscilloscope, while RF microwaves are coupled via an open SMA cable antenna.

### Slide 7: Noise Mitigation & Parametric Derivatives
* **Visual Action:**
  * Point to the formula for parametric derivatives on the slide: $(dV/dt)/(dI/dt)$.
* **Practice Bullet Points:**
  * Cryogenic data suffers from **high thermal noise at 77 K**. While we used hardware averaging, standard numerical differentiation $dV/dI$ was highly unstable.
  * Numerical derivatives amplify high-frequency digitizer noise stemming from DA and AD converters, producing massive artificial spikes that wash out the true physical switching transitions.
  * To resolve this, we computed parametric derivatives in the **time domain**: dividing $dV/dt$ by $dI/dt$.
  * Because both voltage and current sweeps are recorded simultaneously, this time-domain division yields exceptionally clean, physical **differential resistance curves** without artificial numerical artifacts.

---

### Divider: Part 3 — Quantitative Results and Characterization
* **Visual Action:**
  * Smile slightly, pause for 3 seconds, and look ready to showcase real data.
* **Practice Bullet Points:**
  * Let's review our primary quantitative characterization results.

### Slide 8: Single Junction V-I Characteristics (Task 1)
* **What this task is about:** Measuring the single-junction V-I transport at 77 K to extract its critical current ($I_c = 82\ \mu\text{A}$) and identify underdamped, hysteretic switching.
* **Visual Action:**
  * Point to the black experimental trace in `task1_iv.png` on the left. Indicate the **hysteretic loop**.
* **Practice Bullet Points:**
  * This slide shows our recorded **single-junction V-I curve at 77 K**, sweeping at $\pm 120\ \mu\text{A}$.
  * It displays highly stable, **hysteretic switching** with a critical superconducting switching current of $I_c = 82\ \mu\text{A}$.
  * The hysteretic return path is a clear signature of an **underdamped Josephson junction**.
  * In the RCSJ model, this corresponds to a McCumber parameter $\beta_c > 1$.
  * The physical origin of this capacitance is the dielectric grain-boundary bicrystal barrier of YBCO, which behaves as a parallel parasitic capacitor.
  * Finally, the SQUID voltage span of $\pm 1.5\text{ mV}$ perfectly matches the scope's $\pm 1.5\text{ V}$ range, validating our differential amplifier's $1000\times$ gain calibration.

### Slide 9: SQUID Voltage Modulation under Flux Drive (Task 2)
* **What this task is about:** Recording SQUID voltage modulation under a triangular flux sweep to demonstrate active flux-to-voltage transduction for magnetometry.
* **Visual Action:**
  * Point to the periodic modulation curve in `task2_iv.png` on the left. Indicate the x-axis, which is correctly plotted against Flux Bias Current.
* **Practice Bullet Points:**
  * Here we observe the periodic SQUID voltage modulation under a 41 Hz triangular flux drive.
  * We biased the SQUID **current slightly above the critical threshold and swept the flux bias** current over a range of $\pm 300\ \mu\text{A}$.
  * Result: Approximately 6 full flux periods (7 peaks) are clearly resolved in a single sweep direction.
  * This stable, clean modulation confirms robust, **phase-coherent** cooling under liquid nitrogen at 77 K.
  * It demonstrates active **flux-to-voltage transduction**, proving that our device is behaving as an operational **magnetometer**.
* **Theoretical Core (For defense questions):**
  * This is NOT the AC Josephson effect (which governs high-frequency microwave phase-locking seen in Shapiro steps).
  * This is the **DC Josephson Effect** ($I_i = I_c \sin\delta_i$) combined with **Macroscopic Quantum Interference**.
  * Integrating the phase around the SQUID loop containing external flux $\Phi_{\text{ext}}$ forces the phase constraint: $\delta_2 - \delta_1 = 2\pi \Phi_{\text{ext}} / \Phi_0$.
  * This modulates the SQUID's critical current: $I_{c,\text{SQUID}}(\Phi_{\text{ext}}) = 2I_c |\cos(\pi\Phi_{\text{ext}}/\Phi_0)|$ (quantum double-slit interference).
  * Biasing with a constant DC current $I_{\text{bias}} > 2I_c$ forces SQUID voltage $V(\Phi_{\text{ext}}) = \frac{R}{2} \sqrt{I_{\text{bias}}^2 - I_{c,\text{SQUID}}(\Phi_{\text{ext}})^2}$ to oscillate periodically with period $\Phi_0$.

### Slide 10: SQUID Voltage-Flux Transduction & Mutual Inductance (Task 3)
* **What this task is about:** Zooming in on the periodic SQUID voltage modulation to extract the average period ($\Delta I_{\text{flux}} = 82.9\ \mu\text{A}$) and SQUID mutual inductance ($M = 24.9\text{ pH}$).
* **Visual Action:**
  * Point to the zoomed-in data in `task3_flux.png` on the right. Point to the extracted mutual inductance value $M = 24.9\text{ pH}$.
* **Practice Bullet Points:**
  * To extract the mutual inductance, we analyzed the periodicity over a highly stable 14-cycle segment.
  * A **Gaussian filter** smooths out digitizer noise, allowing standard peak detection to extract the average period.
  * The **average period is $\Delta I_{\text{flux}} = 82.9\ \mu\text{A}$.**
  * Since one period corresponds to one flux quantum entering the loop, we use the relation $\Delta\Phi = M \Delta I_{\text{flux}} = \Phi_0$.
  * This yields a calculated mutual inductance of $M = 24.9\text{ pH}$.
  * This matches our manual calculation of $25.2\text{ pH}$ to within 1.2%, validating our automated peak-detection calibration.

### Slide 11: Critical Current Modulation (Task 3b)
* **What this task is about:** Recording V-I curves at 11 flux points to directly visualize the continuous modulation and suppression of the SQUID's critical switching current.
* **Visual Action:**
  * Point to the overlay of 11 V-I traces on the right (`task3_flux_vi_overlay.png`), showing the envelope changing.
* **Practice Bullet Points:**
  * To directly **visualize macroscopic quantum interference**, we recorded complete V-I curves at 11 discrete **flux biases spanning one period**.
  * overlay reveals a clear modulation of the critical switching current.
  * zero-voltage branch scales up and down, showing a maximum voltage modulation depth of $V_{\text{pp}} = 6.0\ \mu\text{V}$ near the critical bias.
  * This represents 8.4% of the peak voltage, providing direct evidence of the expected **cosine phase tuning of the critical current**.

---

### Divider: Part 4 — Shapiro Resonances & Advanced Quantum Metrology
* **Visual Action:**
  * Pause for 3 seconds. Project analytical depth.
* **Practice Bullet Points:**
  * We now move to Shapiro steps and advanced quantum metrology.

### Slide 12: Phase-Locking — AC Josephson Effect
* **Visual Action:**
  * Draw attention to the Shapiro quantization formula: $V_n = n \Phi_0 \nu$.
* **Practice Bullet Points:**
  * Under microwave irradiation, phase-locking produces constant-voltage plateaus in the V-I curve known as Shapiro steps.
  * When we apply an external microwave frequency $\nu$, the intrinsic Josephson oscillations at frequency $\nu_J = 2eV/h$ phase-lock to the drive harmonics: $\nu_J = n\nu$.
  * This restricts the junction voltage to quantized values: $V_n = n (h/2e) \nu = n \Phi_0 \nu$.
  * For our microwave drive frequency of 10 GHz, the expected fundamental step size is exactly $\Delta V_{\text{theory}} = 20.7\ \mu\text{V}$.
  * Because these steps lock voltage directly to frequency via fundamental constants, they serve as the international primary standard for the Volt, independent of temperature or material.

### Slide 13: Step Extraction Methodology — Gaussian LSCV-KDE
* **Visual Action:**
  * Point to the LSCV cost function formula on the slide.
* **Practice Bullet Points:**
  * Standard step extraction methods (such as fixed histograms or derivative thresholds) are highly fragile.
  * They rely on subjective, user-tuned parameters that produced 10 GHz step estimates ranging wildly from $13.3\ \mu\text{V}$ to $25.6\ \mu\text{V}$, introducing up to a 36% error.
  * eliminate this bias -> **parameter-free Gaussian Kernel Density Estimator**
  * optimized the **bandwidth** -> **Least-Squares Cross-Validation** (minimizes the **Mean Integrated Squared Error**)
  * LSCV correctly selected a bandwidth of $h = 1.5\ \mu\text{V}$ (well below Silverman's over-smoothed rule of $6.7\ \mu\text{V}$), successfully resolving the discrete plateaus.
  * also a**pplied a central 50% current slice to reject the normal ohmic branch**, isolating the phase-locked quantum transport.

### Slide 14: Shapiro Step Verification at 10 GHz (Task 4)
* **What this task is about:** Irradiating the SQUID at 10 GHz to observe quantized Shapiro steps at $\Delta V = 20.7\ \mu\text{V}$ and verifying them using parameter-free LSCV-KDE density peaks.
* **Visual Action:**
  * Point to the three panels of `task4_shapiro_10ghz_restored_kde_verification.png`: (1) V-I trace with green slice, (2) differential resistance, (3) continuous KDE probability density showing symmetric peaks.
* **Practice Bullet Points:**
  * This slide showcases our 10 GHz verification workflow using the LSCV-KDE extractor.
  * The top panel shows the raw V-I trace, where green shading isolates our central current slice.
  * The middle panel shows the smoothed $dV/dI$, and the bottom panel shows our optimized KDE density.
  * The continuous density resolves six highly symmetric peaks representing step indices from $n = -3$ to $n = +3$.
  * The extracted median step spacing is $\Delta V_{\text{KDE}} = 19.7\ \mu\text{V}$.
  * This corresponds to an exceptionally low error of only 4.8% relative to the theoretical $20.7\ \mu\text{V}$ value.

### Slide 15: Frequency Dependence & Bimodal Scattering (Task 5)
* **What this task is about:** Sweeping microwave frequency from 8 to 12 GHz to verify the linear relationship of step size with frequency and identifying standing-wave impedance mismatches.
* **Visual Action:**
  * Point to the linear fit on the right (`task5_frequency_dependence_kde.png`). Point to the bimodal clustering of data points.
* **Practice Bullet Points:**
  * We swept the microwave frequency from 8 to 12 GHz to verify the linear frequency dependence.
  * A linear fit through the origin yields a measured flux quantum of $\Phi_0^{\text{meas}} = 1.71 \times 10^{-15}\text{ Wb}$ (a 17.3% deviation from theory).
  * Crucially, the data points exhibit a striking bimodal clustering: lower frequencies (8--9.5 GHz) cluster at 12--$15\ \mu\text{V}$, while higher ones (11--12 GHz) cluster at 21--$23\ \mu\text{V}$.
  * This clustering is a physical waveguide coupling effect: standing wave resonance on our un-matched open SMA microwave line distorts power transfer, rather than a failure of our KDE extractor.
  * The KDE extractor successfully resolved clear symmetric peaks at each individual frequency, proving its mathematical robustness.

### Slide 16: Power Dependence & Harmonic Steps (Task 6)
* **What this task is about:** Sweeping microwave power to find the threshold for step formation ($0\text{ dBm}$) and observing higher-order harmonic Shapiro steps at high power.
* **Visual Action:**
  * Point to the power sweep plot on the left.
* **Practice Bullet Points:**
  * We swept microwave power across 28 discrete traces, standardizing the manual attenuator dial using a 3rd-order polynomial fit.
  * Our LSCV-KDE extractor reveals a clear power threshold: steps only emerge above $\sim 0\text{ dBm}$.
  * Below this threshold, microwave energy is smaller than the thermal noise floor at 77 K ($I_{\text{noise}} = 2e k_B T / \hbar$), completely washing out phase-locking.
  * At high power ($9.1\text{ dBm}$), we resolve a second-harmonic Shapiro step at $\Delta V = 41.7\ \mu\text{V} \approx 2 \Delta V_{\text{theory}}$, corresponding to higher-order $n=2$ phase-locking.

### Slide 17: Full Spatial Visualization (Task 6b)
* **What this task is about:** Constructing 2D colormaps of SQUID voltage and critical current suppression vs. microwave power to visually map the transition into phase-locking.
* **Visual Action:**
  * Point to the three panels (a, b, and c) of the colormap plot (`task6_colormap.png`). Point to the white dashed line showing the 0 dBm threshold.
* **Practice Bullet Points:**
  * These colormaps show the complete spatial evolution of the power sweep.
  * Panel (a) shows the transition broadening of the V-I curves as power increases.
  * Panel (b) shows the clear suppression of the critical switching current peaks.
  * Panel (c) displays the central region detail, where the emerging structure of Shapiro steps is clearly visible above the $0\text{ dBm}$ threshold, marked by the white dashed line.

---

### Divider: Part 5 — Conclusions & Outlook
* **Visual Action:**
  * Pause for 3 seconds. Look ready to summarize your contributions.
* **Practice Bullet Points:**
  * Finally, let's review our conclusions and future outlook.

### Slide 18: Conclusions
* **Visual Action:**
  * Deliver your final conclusions with structured, authoritative points.
* **Practice Bullet Points:**
  * We have successfully completed the cryogenic and quantum characterization of a YBCO DC SQUID at 77 K.
  * We extracted a single-junction critical current of $I_c = 82\ \mu\text{A}$ and a SQUID mutual inductance of $M = 24.9\text{ pH}$.
  * Under microwave irradiation, we verified the AC Josephson relation.
  * Our LSCV-KDE method successfully extracted Shapiro steps with a 4.8% error at 10 GHz...
  * ...while proving that it completely eliminates the subjective bias of standard ad-hoc peak-detection heuristics.

### Slide 19: Outlook & Systematic Challenges
* **Visual Action:**
  * Point to the PCB and SMA cable coupling on your slides.
* **Practice Bullet Points:**
  * Our systematic analysis shows that the dominant error source is the un-matched open SMA microwave antenna.
  * Its standing-wave resonances introduce frequency-dependent impedance mismatches, leading to our 17.3% deviation in the slope of $\Phi_0$.
  * Future work should integrate a matched coplanar waveguide coupler on the SQUID PCB.
  * We also recommend adding an active cryogenic temperature sensor on the sample holder to map the gap transition $\Delta(T)$.
  * Finally, we plan to propagate error bounds directly from the LSCV bandwidth selection.

### Slide 20: Acknowledgments
* **Visual Action:**
  * Make eye contact with your supervisors in the audience.
* **Practice Bullet Points:**
  * We sincerely thank our supervisors Oliver Kurtossy and Peter Makk, as well as Szabolcs Csonka and Andras Halbritter, for their physical guidance and sample support.
  * We also acknowledge the BME Nanoelectronics Laboratory and the Practice-Oriented Higher Education project framework.
  * Thank you very much for your attention. I am now open to any questions.

---

## Part 2: Practice Rehearsal Strategy

To perfect your delivery, use the following structured rehearsal strategy:
1. **Time Yourself:** Your presentation is strictly capped at 20 minutes. Spend approximately 1 minute per slide. If you spend too much time on Slide 4 (Josephson Effect theory), you will run out of time for Slide 14 (your actual 10 GHz data verification).
2. **Use the Pointer:** When discussing `task1_iv.png`, `task2_iv.png`, and `task4_shapiro_10ghz_restored_kde_verification.png`, always use your physical pointer to trace the axis labels. The committee will look at where you point, which anchors their attention to your physical arguments.
3. **Control Your Speed:** Under defense pressure, speakers naturally speed up. Practice pausing for exactly 3 seconds at each Part Divider slide to regain control of your breathing and rhythm.
