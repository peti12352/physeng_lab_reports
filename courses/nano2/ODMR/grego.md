Task 2: Photoluminescence Signal Maximization

No specific plot file (signal levels are noted in the notebook, not plotted).
Task 3: CW Sequence Implementation and Optimization

Plots of CW sweeps (zero field, initial ODMR spectrum):

CW_Sweep_analysis.png
CW_SweepREDO_analysis.png
CW_Sweep_magnet_analysis.png
CW_Sweep_magnet2_analysis.png
(Multiple files: each corresponds to a different measurement or repeat.)

Task 4: ODMR Frequency Sweep (Zero Magnetic Field)

CW_Sweep_analysis.png

CW_SweepREDO_analysis.png

(Use the one that matches your measurement run.)

Task 5: ODMR Frequency Sweep (With Magnetic Field)

CW_Sweep_magnet_analysis.png

CW_Sweep_magnet2_analysis.png

CW_Sweep_magnetFOCUS_analysis.png

CW_Sweep_magnetREDO_analysis.png

CW_Sweep_magnetREDO2_analysis.png

(Multiple files: each is a different sweep or focus region.)

Task 6: Rabi Oscillation Measurement

Rabi_Corrected_analysis.png

Rabi_tau1_analysis.png

(Multiple files: different runs or power levels.)

Task 7: T1 Relaxation Measurement

T1_Sweep_analysis.png

T1_Sweep2_analysis.png

T1_relaxation_for_fit_analysis.png

(Multiple files: different sweeps or data processing variants.)


Figures for CW, Rabi, and T1 experiments are generated and saved (see the results/analysis/plots/ directory).
The code in analyze_all_results.py covers:
Peak finding and resonance extraction for CW/ODMR spectra.
Nonlinear curve fitting for Rabi oscillations (damped cosine) and T1 relaxation (exponential decay).
Extraction of all key parameters (D, E, T1, Rabi frequency, contrast, etc.).
Automated summary tables and coverage checks.