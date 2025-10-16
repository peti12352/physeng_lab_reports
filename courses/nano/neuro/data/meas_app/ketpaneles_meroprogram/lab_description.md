1
Physicist-Engineer Nanotechnology and Quantum Applications
Specialization Laboratory Measurement 1:
Neuromorphic Electronics
Abstract. According to an analysis, by 2030, information technology will account for
more than 20% of the world’s total energy consumption due to the rapid growth
in stored and processed data and the rise of artificial intelligence. To prevent data
centers from consuming the world’s electricity production, in addition to developing
artificial intelligence algorithms, new energy-efficient hardware devices are also needed
that better follow the structure of neural networks and even handle data storage
and computing in one place. This measurement session provides insight into the
emerging field of research known as neuromorphic electronics. The measurement
description presents the basics of the field, introducing new types of memories, known
as memristors, which can behave as artificial synapses or artificial neurons. During
the measurement task, you will examine volatile vanadium dioxide (VO2) memristors,
which can be used to create oscillatory circuits or even oscillating neural networks or
artificial neurons.
Warning. During the measurement, you will study the temperature-dependent phase
transition of the samples under investigation, during which you must not touch the
hot surfaces. In addition, you will be working with measuring systems that operate
at low voltages, which pose a greater risk to the samples under investigation than
to the persons performing the measurements. In order to protect the nanofabricated
circuits studied during the measurement, it is very important to check the drive
signal shapes before the actual measurement, as signal shapes with inappropriate
amplitude or duration can cause damage to the device under test. Discharges caused
by electrostatically charged bodies can also cause damage to the devices, so ESD
(electrostatic discharge) protection must be used.
As a general rule, always ensure the safety of yourself and others during measurements.
If you are unsure about anything, ask the lab supervisors for help and always follow
their warnings and instructions.
1
Introduction 2
IIntroduction
1 Need for Novel Hardware Architectures in Information
Technologies
In general, it can be stated that artificial neural networks, which form the basis of artificial
intelligence, are capable of solving very complex tasks, but running them on traditional
digital computers requires enormous computing power, as a very large number of neural
output values and synaptic weights must be multiplied and added together. In addition,
data storage and operations are performed in physically separate units, which means that
data transfer between memory and processor also becomes a bottleneck.
With its 175 million parameters ChatGPT claims that it needs to perform 10-20 trillion
(billion times billion) calculations to answer a single question. This computational demand
is also significant in terms of energy consumption. According to a prediction, by 2030,
Figure I.1.1. Left: illustration of biological neurons. In a biological neural network, a
neuron collects information from other neurons through its various synapses, with the synaptic
connections having different strengths (different synaptic weights). The information arriving via
the synapses is added up, and if the total strength of the input neural pulses exceeds an activation
threshold, the neuron emits an output pulse. Learning schemes are associated with changes in
synaptic weights, according to the relevance of the actual piece of information. Right: illustra-
tion of artificial neural networks. In the most common artificial neural networks a neuron
also collects information from its inputs, which are usually the output values of other neurons
(xi). These are multiplied by the synaptic weights, and added together also using an offset value,∑
i xiwi + x0. Finally a nonlinear activation function, f(.) is applied, which outputs a certain
value (like −1) if the sum is well below a threshold, and changes to another value (like +1) if the
summed information exceeds the activation threshold. The simplest feed-forward neural networks
(bottom) contain an input layer and an output layer (left and right yellow circles), as well as
additional hidden neural layers (red and blue circles). All neurons between two neighboring layers
(e.g. red and blue) are connected by artificial synapses. Here, the learning scheme is also related
to the change in weights via the so-called backpropagation algorithm.
Introduction 3
more than 20% of the world’s total energy consumption will be required by information
technology based on artificial intelligence [1]. For this reason, it is not enough to develop
algorithms and device networks capable of solving more and more complex tasks in order to
further advance artificial intelligence. It is at least as important to be able to perform the
underlying calculations quickly and energy-efficiently with new types of hardware devices
that are better aligned with the structure of neural networks and can handle data storage
and computation in one place.
The biological nervous system provides inspiration for the development of this new,
so-called neuromorphic hardware. Just think about how incredibly efficient the human
brain is, consuming only about 30 W of energy! Fig. I.1.1 briefly summarizes how artificial
neural networks are inspired by the biological nervous system. Such neural networks are
already easy to implement in software, but neuromorphic electronics aims to implement
artificial neural networks in energy-efficient hardware.
2 Non-volatile memristors as artificial synapses Figure I.2.1. Memristors as
artifical synapses. (a) Illustra-
tive I(V ) curve of a Ta2O5 mem-
ristor. At a positive threshold
the high resistance state (HRS)
is switched to a low resistance
state (LRS) due to the removal
of oxygen ions from the active fil-
amentary region, while at oppo-
site polarity backswitching occurs
(see the illustrations in the in-
sets). (b) A memristor is an ar-
tificial synapse, as the slope of its
low-voltage I(V ) curve can be ad-
justed almost arbitrarily with the
appropriate voltage manipulation.
(c) This property can be used
in neural networks for the hard-
ware implementation of synaptic
weights.
The possible building blocks of such neuromorphic hardware are so-called memristors, i.e.,
resistors with memory. These are physical systems whose resistance can be tuned with
high voltage and read without information loss at low voltage. Physically, a memristor is
implemented by placing a special, originally insulating layer between two metal electrodes.
In many applications this insulating layer is a metal oxide, like Ta2O5 or HfOx. With suffi-
ciently high electrical voltage, we can move oxygen ions out of a certain region, thus turning
this oxygen-deficient region into a conductor (see the illustration in the bottom inset of
Fig. I.2.1a). With this process we can form a well-conducting metallic filament between
the two electrodes. At opposite voltage polarity, however, the oxygen ions return to this
filamentary region (see the illustration in the top inset of Fig. I.2.1a) thus blocking conduc-
tion through the filament. This reproducible process is illustrated by the current-voltage
(I(V )) characteristic of a Ta2O5 memristor shown in Fig. I.2.1a. Here, switching occurs
between a certain low resistance state (LRS) and a certain high resistance state (HRS), but
the actual resistance of the HRS and LRS, i.e., the corresponding filament diameter, can
be adjusted by the amplitude and duration of the applied voltage signal. Furthermore, at
sufficiently low voltages (below the positive and negative switching thresholds), the system
maintains its state, which means that the memristor behaves as a constant resistance RM
with an almost linear I(V ) curve, I = V/RM . In this low voltage range, the resistance
state can be read without changing the resistance. Such memristors are analog memories
whose low-voltage I(V ) curve slope can be adjusted practically to arbitrary values (see
Fig. I.2.1b). Accordingly, their conductance GM = 1/RM can be used efficiently for the
hardware implementation of synaptic weights in artificial neural networks.
In order to use memristors in information technology, they must be arranged in a net-
work. This is surprisingly easy to achieve: all that is needed is to place an insulating layer
suitable for forming memristors between the blue bottom and red top metal electrodes, as
illustrated in Fig. I.2.2. When voltage is applied between the top electrode i and the bot-
tom electrode j, a memristor contact can be formed at the crosspoint of these electrodes,
whose conductance Gji can be set to the desired value. These memristor contacts are rep-
resented by the brown filaments in Fig. I.2.2. It should be noted that once the conductance
matrix Gji has been programmed into this so-called crossbar memristor array, the voltage
vector Vi applied to the upper electrodes results in a current output vector Ij at the lower
electrodes, which is simply the matrix-vector product of the input voltage vector and the
memristor conductance matrix, Ij = ∑
i Gji ·Vi. It should be noted that in a neural net-
Introduction 4
work, such as the one shown in Fig. I.1.1, the input vector of the blue neural layer ij is
given by: ij = ∑
i wji ·xi, where xi is the output vector of the red neural layer and wji is
the weight matrix of the gray synaptic connections between the two layers. If there are N
neurons in both layers, evaluating this input vector requires N2 multiplication operations
in the software. However, if the synaptic connections are implemented in hardware using
a memristive crossbar array, this matrix-vector multiplication calculation is performed by
the memristive hardware in a single step. This is a significant advantage in terms of energy
efficiency and computational speed. Non-volatile memristors, which function as artificial
synapses, have numerous applications in the field of neuromorphic computing, but the
hardware-level single-step matrix-vector multiplication presented here is undoubtedly one
of their most promising applications. Nowadays, this is no longer just a theoretical concept,
but with the construction of networks of tens of millions of memristors, it is possible to
build artificial neural networks that are capable of performing complex image recognition
or other computational tasks with high accuracy and astonishing energy efficiency [2, 3].
Figure I.2.2. Memristive
crossbar arrays. The brown
memristor contacts are formed at
the intersection of the upper red
and lower blue electrodes. Such a
crossbar array implements synap-
tic connections between two adja-
cent layers of a neural network.
The memristor conductance ma-
trix, Gji, is programmed during
the training of the neural net-
work. Subsequently, during in-
ference, the synaptic weights are
fixed, and the memristive cross-
bar array performs matrix-vector
multiplication in a single hardware
operation according to Ohm’s law
and Kirchoff’s rules.
3 Volatile memristors as artificial neurons
In the above example, non-volatile memristors functioned as artificial synapses and essen-
tially served as hardware accelerators for matrix-vector multiplication calculations. How-
ever, other types of memristors can also behave as artificial neurons. Such memristors
are generally volatile, which means that at a given voltage they switch from their original
high-resistance state to a low-resistance state, but at the same voltage polarity they switch
back to their original high-resistance state with a hysteresis once the voltage is lowered.
Accordingly, at zero bias, always the high-resistance state is realized.
This operation can be performed, for example, with vanadium dioxide (VO2) memris-
tors, which are also the candidates for this measurement session. VO2 is a special material
system that exhibits an insulator-metal transition at a temperature around T = 68 ◦C, as
shown by its temperature-dependent resistance in Fig. I.3.1a. The same insulator-metal
transition can also be triggered by voltage when applied to a nanodevice in which two metal
electrodes are connected by a narrow VO2 region (Fig. I.3.1b). In this case, the phase
transition is primarily caused by self-heating due to the voltage, but nonlinear conduction
phenomena may also play a role [4]. This voltage-induced resistance switching is illustrated
by the I(V ) curves in Fig. I.3.1c. In this case, the driving voltage Vdrive is ramped by a
Figure I.3.1. Characteristic traits of VO2 nanogap memristors. Temperature-dependent
resistance of a nanogap memristor taken from Ref. 4. (b) Top: Scanning electron microscopy
(SEM) image of the active region of a representative memristor studied in this laboratory exercise.
Scale bar: 500 nm. Bottom: schematic material structure of the investigated memristors. (c)
Drive voltage (gray) and bias voltage (red) -dependent I(V ) characteristics of a VO2 memristor.
Introduction 5
voltage generator, and this signal is fed to the VO2 device and a series-connected resistor
RS . Fig. I.3.1 shows the I(V ) curve as a function of both Vdrive (gray curve) and the bias
voltage, Vbias = Vdrive −I ·RS , which drops across the VO2 device itself (red curve). The
latter curve shows the so-called set voltage, where the VO2 device switches from HRS to
LRS, and the reset voltage, where it switches back from LRS to HRS. It should be noted
that when the switching occurs, the resistance of the VO2 device changes, and therefore
Vbias also changes due to the voltage division with the series-connected resistor. Such I(V )
curves (like Fig. I.3.1c) and temperature dependent resistance curves (like Fig. I.3.1a) will
be investigated during the first part of the measurement session.
Circuits containing as few as two VO2 memristors are capable of reproducing various
types of biological neural spiking patterns [5]. Fig. I.3.2 shows the simplest case: an
artificial neuron circuit that emits a single neural spike when the input exceeds the proper
threshold value.
Figure I.3.2. Bio-inspired circuits. (a) Schematics of an artificial neuronal circuit made of a
pair of VO2 memristors, several R, C elements and additional DC voltage sources. The background
color figure illustrates that this artificial neural circuit perfomrs similar operation to the Na+ and
K+ channels in a biological neural cell. (b) Artificial neuronal waveform (spike) emitted by the
circuit in panel (a). Taken from Ref. 5.
Figure I.3.3. Concept of VO2
oscillator circuits. (a) A con-
stant V0 voltage is applied on the
VO2 device and the resistor in se-
ries. (b) At sufficiently large RS
the load line does not cross the
I(V) curve, i.e. instead of a sta-
ble state a repetitive back and
forth switching, i.e. an oscillat-
ing behavior is established. (c)
The characteristic time of the os-
cillation is adjustable by a parallel
capacitor C. (d) Typical voltage
(blue) and current (black) signal
of a VO2 oscillator circuit.
An even simpler arrangement using a single VO2 device can be used to create an
oscillator circuit. The principle of this is demonstrated in Fig. I.3.3. Take a single VO2
device, connect it in series with a suitably large resistor, and apply a constant voltage
Vdrive = V0 (Fig. I.3.3a). According to Fig. I.3.3b, we can plot the illustrative I(Vbias)
curve of the VO2 device (red-blue curve) and the I = (V0 −Vbias)/RS load line (gray
dashed line). The latter specifies how much current flows through the circuit at a given
Vbias. We can see that the load line intersects the memristor’s I(Vbias curve in unstable
states, i.e., before reaching the intersection of the load line with the HRS’s I(V ) curve (red
circle on the red dotted line) , the system switches to LRS at the Vset voltage. At this point,
the voltage division with RS causes Vbias to decrease, but before the other intersection with
the load line would be established in the LRS (blue circle), the system switches back to
HRS at Vreset. As a result, the memristor will switch back and forth between the HRS and
LRS in response to a constant V0 drive voltage. If we connect a capacitor C in parallel with
the memristor (Fig. I.3.3c), we can set the time-scale of the periodic switching between the
two states. The such obtained oscillating voltage and current waveform is demonstrated in
Fig. I.3.3d. Such oscillator circuit will be established and studied during the second part
of the measurement session.
As an interesting application, VO2 oscillating circuits can be assembled to so-called
oscillating neural networks (ONNs), which can solve computational problems through their
physical operation, i.e. through the synchronization of the phases. Fig. I.3.4 illustrates this
scheme through a recent publication of the researchers of IBM Zürich [6]. The computa-
tional problem is map coloring: the countries of South America should be colored such
Introduction 6
that the minimal number of colors are used, but neighbor countries have different colors
(Fig. I.3.4a). The map can be represented by a graph whose nodes represent countries,
while the connections represent the neighboring positions of countries (Fig. I.3.4b). This
graph can be implemented by an oscillating neural network, where the nodes are VO2
oscillator circuits, and the connections are established by capacitive coupling between the
individual oscillator circuits (Fig. I.3.4c). In this network of oscillating circuits the phases
of the individual oscillators synchronize such that the phase difference is maximized be-
tween neighbor (coupled) nodes. Finally, the phases stabilize around four distinct values:
oscillators 1, 2, 3, 6 have fundamentally different phases, while oscillators 4 and 5 have sim-
ilar phase as oscillator 2 (Fig. I.3.4d). This figure tells us the solution of the map coloring
problem, which is illustrated by purple, blue, pink and green colors in Figs. I.3.4a,b.
Figure I.3.4. Solving graph
coloring problem with the
synchronization of a coupled
oscillator network. (a) Illus-
tration of the problem: the coun-
tries of South Africa should be col-
ored such that the minimal num-
ber of colors are used, but neigh-
bor countries have different colors.
(b) Graph representation of the
problem: counties are represented
by nodes, neighbor countries are
connected by edges. (c) Mapping
of the problem to a network of os-
cillators. (d) Oscillators synchro-
nize to four different phases cor-
responding to the solution. Taken
from Ref. 6.
The above example demonstrates an elegant approach in which physics itself pro-
vides the solution through the synchronization of coupled oscillators. It is evident that
the exponentially growing computational demands of our time cannot be managed by
von Neumann-type computers alone; conventional computing must be complemented with
highly energy-efficient application-specific hardware and accelerators. These may operate
even at the edge of a network, directly at the origin of data, enabling low-cost, ultra-
low-power data analysis. Given the remarkable progress in this field, we can expect that
new forms of neuromorphic hardware will soon become part of our everyday devices. As
oscillator-based neural networks may emerge as key players in this technological evolution,
we should not forget that John von Neumann himself made fundamental contributions to
the idea of oscillator networks, which could potentially overcome the limitations of von
Neumann architectures [7, 8].
