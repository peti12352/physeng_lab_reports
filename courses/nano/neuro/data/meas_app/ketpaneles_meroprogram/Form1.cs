using Ivi.Visa;
using NationalInstruments.DAQmx;
using NationalInstruments.Visa;
using System;
using System.ComponentModel;
using System.Globalization;
using System.IO;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;


namespace ketpaneles_meroprogram
{
    public partial class Form1 : Form
    {
        bool Run = false;
        StreamWriter fileWriter;

        //Global variables
        private NationalInstruments.DAQmx.Task BiasOutTask;    // Task: DEVICE/ao0   
        private AnalogSingleChannelWriter writer;
        private NationalInstruments.DAQmx.Task V_MeasureInTask;    // Task: DEVICE/ai0
        private NationalInstruments.DAQmx.Task ResistanceMeasureTask;   // Task: DEVICE/dmm
        private AnalogMultiChannelReader V_MeasureReader;
        private AnalogSingleChannelReader ResistanceMeasureReader;

        double MinimumResistance = 700;
        double MaximumResistance = 1300;
        double Minimumvoltage = -10;
        double Maximumvoltage = 10;
        double SerialResValue;
        double MeasStartTime;
        double DriveVoltage = 0;

        // New sweep variables
        private double startVoltage, endVoltage, stepVoltage;
        // private bool peltierSweepingUp = true; // Removed duplicate declaration

        // New UI Elements
        private Label labelStartVoltage;
        private TextBox textBoxStartVoltage;
        private Label labelEndVoltage;
        private TextBox textBoxEndVoltage;
        private Label labelStepVoltage;
        private TextBox textBoxStepVoltage;
        private Label labelSeriesResistor;
        private TextBox textBoxSeriesResistor;
        private Label labelConstantDriveVoltage;
        private TextBox textBoxConstantDriveVoltage;
        private Label labelPeltierStartVoltage; // Moved declaration
        private TextBox textBoxPeltierStartVoltage; // Moved declaration
        private Label labelPeltierEndVoltage; // Moved declaration
        private TextBox textBoxPeltierEndVoltage; // Moved declaration
        private Label labelPeltierStepVoltage; // Moved declaration
        private TextBox textBoxPeltierStepVoltage; // Moved declaration
        private MessageBasedSession powerSupplySession; // New: VISA session for power supply
        private double peltierStartVoltage, peltierEndVoltage, peltierStepVoltage, peltierCurrentVoltage;
        private bool peltierSweepingUp = true;

        private Button buttonPeltierOn;
        private Button buttonPeltierOff;

        // Placeholder for VISA resource name - **USER TO UPDATE**
        private const string PeltierPowerSupplyVisaResource = "USB0::0xF4EC::0x1410::SPD13DCC8R0078::INSTR"; // Replaced XXXXXXXXXXXX with the actual serial number/resource name

        public Form1()
        {
            InitializeComponent();

            // Manual UI components for sweep
            // Start Voltage
            this.labelStartVoltage = new Label();
            this.labelStartVoltage.AutoSize = true;
            this.labelStartVoltage.Location = new System.Drawing.Point(26, 125);
            this.labelStartVoltage.Name = "labelStartVoltage";
            this.labelStartVoltage.Text = "Start V (V)";
            this.Controls.Add(this.labelStartVoltage);

            this.textBoxStartVoltage = new TextBox();
            this.textBoxStartVoltage.Location = new System.Drawing.Point(30, 140);
            this.textBoxStartVoltage.Name = "textBoxStartVoltage";
            this.textBoxStartVoltage.Text = "-4";
            this.Controls.Add(this.textBoxStartVoltage);

            // End Voltage
            this.labelEndVoltage = new Label();
            this.labelEndVoltage.AutoSize = true;
            this.labelEndVoltage.Location = new System.Drawing.Point(26, 170);
            this.labelEndVoltage.Name = "labelEndVoltage";
            this.labelEndVoltage.Text = "End V (V)";
            this.Controls.Add(this.labelEndVoltage);

            this.textBoxEndVoltage = new TextBox();
            this.textBoxEndVoltage.Location = new System.Drawing.Point(30, 185);
            this.textBoxEndVoltage.Name = "textBoxEndVoltage";
            this.textBoxEndVoltage.Text = "4";
            this.Controls.Add(this.textBoxEndVoltage);

            // Step Voltage
            this.labelStepVoltage = new Label();
            this.labelStepVoltage.AutoSize = true;
            this.labelStepVoltage.Location = new System.Drawing.Point(26, 210);
            this.labelStepVoltage.Name = "labelStepVoltage";
            this.labelStepVoltage.Text = "Step V (V)";
            this.Controls.Add(this.labelStepVoltage);

            this.textBoxStepVoltage = new TextBox();
            this.textBoxStepVoltage.Location = new System.Drawing.Point(30, 225);
            this.textBoxStepVoltage.Name = "textBoxStepVoltage";
            this.textBoxStepVoltage.Text = "0.2";
            this.Controls.Add(this.textBoxStepVoltage);

            // Series Resistor
            this.labelSeriesResistor = new Label();
            this.labelSeriesResistor.AutoSize = true;
            this.labelSeriesResistor.Location = new System.Drawing.Point(26, 250);
            this.labelSeriesResistor.Name = "labelSeriesResistor";
            this.labelSeriesResistor.Text = "Series Resistor (Ohm)";
            this.Controls.Add(this.labelSeriesResistor);

            this.textBoxSeriesResistor = new TextBox();
            this.textBoxSeriesResistor.Location = new System.Drawing.Point(30, 265);
            this.textBoxSeriesResistor.Name = "textBoxSeriesResistor";
            this.textBoxSeriesResistor.Text = "2170";
            this.Controls.Add(this.textBoxSeriesResistor);

            // Constant Drive Voltage
            this.labelConstantDriveVoltage = new Label();
            this.labelConstantDriveVoltage.AutoSize = true;
            this.labelConstantDriveVoltage.Location = new System.Drawing.Point(26, 290);
            this.labelConstantDriveVoltage.Name = "labelConstantDriveVoltage";
            this.labelConstantDriveVoltage.Text = "Constant Drive V (V)";
            this.Controls.Add(this.labelConstantDriveVoltage);

            this.textBoxConstantDriveVoltage = new TextBox();
            this.textBoxConstantDriveVoltage.Location = new System.Drawing.Point(30, 305);
            this.textBoxConstantDriveVoltage.Name = "textBoxConstantDriveVoltage";
            this.textBoxConstantDriveVoltage.Text = "0"; // Default to 0V
            this.Controls.Add(this.textBoxConstantDriveVoltage);

            // Peltier Start Voltage
            this.labelPeltierStartVoltage = new Label();
            this.labelPeltierStartVoltage.AutoSize = true;
            this.labelPeltierStartVoltage.Location = new System.Drawing.Point(26, 330);
            this.labelPeltierStartVoltage.Name = "labelPeltierStartVoltage";
            this.labelPeltierStartVoltage.Text = "Peltier Start V (V)";
            this.Controls.Add(this.labelPeltierStartVoltage);

            this.textBoxPeltierStartVoltage = new TextBox();
            this.textBoxPeltierStartVoltage.Location = new System.Drawing.Point(30, 345);
            this.textBoxPeltierStartVoltage.Name = "textBoxPeltierStartVoltage";
            this.textBoxPeltierStartVoltage.Text = "0";
            this.Controls.Add(this.textBoxPeltierStartVoltage);

            // Peltier End Voltage
            this.labelPeltierEndVoltage = new Label();
            this.labelPeltierEndVoltage.AutoSize = true;
            this.labelPeltierEndVoltage.Location = new System.Drawing.Point(26, 370);
            this.labelPeltierEndVoltage.Name = "labelPeltierEndVoltage";
            this.labelPeltierEndVoltage.Text = "Peltier End V (V)";
            this.Controls.Add(this.labelPeltierEndVoltage);

            this.textBoxPeltierEndVoltage = new TextBox();
            this.textBoxPeltierEndVoltage.Location = new System.Drawing.Point(30, 385);
            this.textBoxPeltierEndVoltage.Name = "textBoxPeltierEndVoltage";
            this.textBoxPeltierEndVoltage.Text = "5";
            this.Controls.Add(this.textBoxPeltierEndVoltage);

            // Peltier Step Voltage
            this.labelPeltierStepVoltage = new Label();
            this.labelPeltierStepVoltage.AutoSize = true;
            this.labelPeltierStepVoltage.Location = new System.Drawing.Point(26, 410);
            this.labelPeltierStepVoltage.Name = "labelPeltierStepVoltage";
            this.labelPeltierStepVoltage.Text = "Peltier Step V (V)";
            this.Controls.Add(this.labelPeltierStepVoltage);

            this.textBoxPeltierStepVoltage = new TextBox();
            this.textBoxPeltierStepVoltage.Location = new System.Drawing.Point(30, 425);
            this.textBoxPeltierStepVoltage.Name = "textBoxPeltierStepVoltage";
            this.textBoxPeltierStepVoltage.Text = "0.1";
            this.Controls.Add(this.textBoxPeltierStepVoltage);

            // Peltier ON Button
            this.buttonPeltierOn = new Button();
            this.buttonPeltierOn.Location = new System.Drawing.Point(30, 460);
            this.buttonPeltierOn.Name = "buttonPeltierOn";
            this.buttonPeltierOn.Size = new System.Drawing.Size(100, 23);
            this.buttonPeltierOn.Text = "Peltier ON";
            this.buttonPeltierOn.UseVisualStyleBackColor = true;
            this.buttonPeltierOn.Click += new System.EventHandler(this.buttonPeltierOn_Click);
            this.Controls.Add(this.buttonPeltierOn);

            // Peltier OFF Button
            this.buttonPeltierOff = new Button();
            this.buttonPeltierOff.Location = new System.Drawing.Point(140, 460);
            this.buttonPeltierOff.Name = "buttonPeltierOff";
            this.buttonPeltierOff.Size = new System.Drawing.Size(100, 23);
            this.buttonPeltierOff.Text = "Peltier OFF";
            this.buttonPeltierOff.UseVisualStyleBackColor = true;
            this.buttonPeltierOff.Click += new System.EventHandler(this.buttonPeltierOff_Click);
            this.Controls.Add(this.buttonPeltierOff);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            chart1.ChartAreas[0].AxisX.Title = "Bias Voltage (V)"; // Corrected X-axis title
            chart1.ChartAreas[0].AxisY.Title = "Current (mA)";

            chart1.ChartAreas[0].AxisX.LabelStyle.Format = "0.##";
            chart1.ChartAreas[0].AxisY.LabelStyle.Format = "0.##";

            chart1.Legends[0].Docking = Docking.Top;

            chart1.Series[0].ChartType = SeriesChartType.Line;

            chart2.ChartAreas[0].AxisX.Title = "Temperature (C)"; // Corrected X-axis title for R(T) plot
            chart2.ChartAreas[0].AxisY.Title = "Sample Resistance (Ohm)";

            chart2.ChartAreas[0].AxisX.LabelStyle.Format = "0.##";
            chart2.ChartAreas[0].AxisY.LabelStyle.Format = "0.##";

            chart2.Legends[0].Docking = Docking.Top;

            chart2.Series[0].ChartType = SeriesChartType.Line;
        }

        private void buttonStart_Click(object sender, EventArgs e)
        {
            if (Run)
            {
                timer.Enabled = false;
                Run = false;
                buttonStart.Text = "Start";
                fileWriter.Close();
                //free up resources 
                BiasOutTask.Dispose();
                V_MeasureInTask.Dispose();
                ResistanceMeasureTask.Dispose();
                if (powerSupplySession != null)
                {
                    powerSupplySession.RawIO.Write("OUTPut CH1,OFF"); // Turn off power supply output
                    powerSupplySession.Dispose();
                }
            }
            else
            {
                saveFileDialog.ShowDialog();

                //Output
                MeasStartTime = DateTime.Now.ToOADate()*24*3600;
                BiasOutTask = new NationalInstruments.DAQmx.Task();  //Task constructor
                BiasOutTask.AOChannels.CreateVoltageChannel("myDAQ1/ao0", "",                        Minimumvoltage, Maximumvoltage,
                        AOVoltageUnits.Volts);//Creating the output channel
                writer = new AnalogSingleChannelWriter(BiasOutTask.Stream);
                
                // Initialize Power Supply Session for Peltier
                try
                {
                    powerSupplySession = (MessageBasedSession)new NationalInstruments.Visa.ResourceManager().Open(PeltierPowerSupplyVisaResource);
                    powerSupplySession.RawIO.ReadTimeout = 2000; // Set a read timeout for VISA operations
                    powerSupplySession.RawIO.WriteTimeout = 2000; // Set a write timeout for VISA operations
                    powerSupplySession.RawIO.Write("OUTPut CH1,ON"); // Turn on power supply output
                }
                catch (VisaException ex)
                {
                    MessageBox.Show("Error opening Peltier power supply session: " + ex.Message);
                    Run = false;
                    return;
                }
                catch (Exception ex)
                {
                    MessageBox.Show("General error with Peltier power supply: " + ex.Message);
                    Run = false;
                    return;
                }

                //Input
                V_MeasureInTask = new NationalInstruments.DAQmx.Task();  //Task constructor
                                      //Creating the input channel
                V_MeasureInTask.AIChannels.CreateVoltageChannel("myDAQ1/ai0:1", "",
                        AITerminalConfiguration.Differential, Minimumvoltage, Maximumvoltage,
                        AIVoltageUnits.Volts); //same type of measurements can be done in one task
                V_MeasureReader = new AnalogMultiChannelReader(V_MeasureInTask.Stream);

                //Resistance measurement
                ResistanceMeasureTask = new NationalInstruments.DAQmx.Task();
                ResistanceMeasureTask.AIChannels.CreateResistanceChannel("myDAQ1/dmm", "", MinimumResistance, MaximumResistance, AIResistanceConfiguration.TwoWire, AIExcitationSource.Internal, 1e-3, AIResistanceUnits.Ohms);
                // Current excitation must be set to 1e-3

                ResistanceMeasureReader = new AnalogSingleChannelReader(ResistanceMeasureTask.Stream);

                // Parse sweep parameters
                startVoltage = double.Parse(textBoxStartVoltage.Text, CultureInfo.InvariantCulture);
                endVoltage = double.Parse(textBoxEndVoltage.Text, CultureInfo.InvariantCulture);
                stepVoltage = double.Parse(textBoxStepVoltage.Text, CultureInfo.InvariantCulture);
                SerialResValue = double.Parse(textBoxSeriesResistor.Text, CultureInfo.InvariantCulture);
                
                // Parse Constant Drive Voltage for sample
                DriveVoltage = double.Parse(textBoxConstantDriveVoltage.Text, CultureInfo.InvariantCulture);

                // Parse Peltier sweep parameters
                peltierStartVoltage = double.Parse(textBoxPeltierStartVoltage.Text, CultureInfo.InvariantCulture);
                peltierEndVoltage = double.Parse(textBoxPeltierEndVoltage.Text, CultureInfo.InvariantCulture);
                peltierStepVoltage = double.Parse(textBoxPeltierStepVoltage.Text, CultureInfo.InvariantCulture);
                peltierCurrentVoltage = peltierStartVoltage; // Initialize current Peltier voltage
                peltierSweepingUp = true;

                // Set initial Peltier voltage
                try
                {
                    powerSupplySession.RawIO.Write($"SOURce:VOLTage {peltierCurrentVoltage.ToString(CultureInfo.InvariantCulture)}");
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error setting initial Peltier voltage: " + ex.Message);
                    Run = false;
                    return;
                }

            }
        }
        

        private void saveFileDialog_FileOk(object sender, CancelEventArgs e)
        {
            fileWriter = new StreamWriter(saveFileDialog.FileName);
            timer.Interval = Convert.ToInt32(numericInterval.Value);
            Run = true;
            buttonStart.Text = "Stop";
            timer.Enabled = true;
            fileWriter.WriteLine("Time (s)\tPeltier Voltage (V)\tPT1000 Resistance (Ohm)\tTemperature (C)\tDrive Voltage (V)\tResistor Voltage Drop (V)\tCurrent (A)\tSample Resistance (Ohm)\tRaw AO0 (V)\tRaw AI0 (V)\tRaw AI1 (V)"); 

        }

        private void timer_Tick(object sender, EventArgs e)
        {
            double CurrentTimeSeconds = DateTime.Now.ToOADate() * 24 * 3600 - MeasStartTime;

            // Set output voltage
            writer.WriteSingleSample(true, DriveVoltage);

            // measurement
            double[] data = V_MeasureReader.ReadSingleSample();
            double ai0 = data[0];
            double ai1 = data[1];

            double resistorVoltageDrop = ai1; // Corrected: ai1 is the series resistor voltage drop
            double current = resistorVoltageDrop / SerialResValue; // Corrected: current = V_RS / RS
            double biasVoltage = DriveVoltage - ai1; // Corrected: Vbias = Vdrive - V_RS

            double pt1000Resistance = 0.0; // Initialize PT1000 resistance
            try
            {
                pt1000Resistance = ResistanceMeasureReader.ReadSingleSample();
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error reading PT-1000 resistance: " + ex.Message);
                // Handle error, possibly stop the measurement
            }

            double sampleResistance = (current != 0) ? (biasVoltage / current) : 0; // Calculate sample resistance (Memristor Resistance)

            // PT1000 Resistance to Temperature Conversion (Callendar-Van Dusen equation)
            double R0 = 1000.0; // Resistance at 0°C for PT1000
            double A = 3.9083e-3;
            double B = -5.775e-7;
            double temperature = 0.0;

            // For T >= 0 °C (simple quadratic approximation)
            if (pt1000Resistance >= R0)
            {
                double deltaR = pt1000Resistance - R0;
                temperature = (-A + Math.Sqrt(A * A - 4 * B * deltaR)) / (2 * B);
            }
            // For T < 0 °C (more complex equation, but often not needed for Peltier heating)
            else
            {
                // This part can be refined if negative temperatures are expected and require higher accuracy
                // For simplicity, a linear approximation or the same quadratic can be used if accuracy allows
                // However, a more accurate formula for T < 0 C involves a C coefficient.
                // For now, using the same quadratic for estimation, but a warning is due.
                double deltaR = pt1000Resistance - R0;
                temperature = (-A + Math.Sqrt(A * A - 4 * B * deltaR)) / (2 * B);
            }

            //plotting data
            chart1.Series[0].Points.AddXY(biasVoltage, current * 1000); // Plot current in mA
            chart2.Series[0].Points.AddXY(temperature, sampleResistance); // Plot Sample Resistance vs Temperature

            //writing data to file
            fileWriter.WriteLine("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}", 
                CurrentTimeSeconds.ToString(CultureInfo.InvariantCulture),
                peltierCurrentVoltage.ToString(CultureInfo.InvariantCulture),
                pt1000Resistance.ToString(CultureInfo.InvariantCulture),
                temperature.ToString(CultureInfo.InvariantCulture),
                DriveVoltage.ToString(CultureInfo.InvariantCulture),
                resistorVoltageDrop.ToString(CultureInfo.InvariantCulture),
                current.ToString(CultureInfo.InvariantCulture),
                sampleResistance.ToString(CultureInfo.InvariantCulture),
                DriveVoltage.ToString(CultureInfo.InvariantCulture),
                ai0.ToString(CultureInfo.InvariantCulture),
                ai1.ToString(CultureInfo.InvariantCulture));

            // Update Peltier sweep voltage and control power supply
            if (powerSupplySession != null)
            {
                if (peltierSweepingUp)
                {
                    peltierCurrentVoltage += peltierStepVoltage;
                    if (peltierCurrentVoltage >= peltierEndVoltage)
                    {
                        peltierCurrentVoltage = peltierEndVoltage;
                        peltierSweepingUp = false;
                    }
                }
                else
                {
                    peltierCurrentVoltage -= peltierStepVoltage;
                    if (peltierCurrentVoltage <= peltierStartVoltage)
                    {
                        peltierCurrentVoltage = peltierStartVoltage;
                        peltierSweepingUp = true;
                    }
                }
                try
                {
                    powerSupplySession.RawIO.Write($"SOURce:VOLTage {peltierCurrentVoltage.ToString(CultureInfo.InvariantCulture)}");
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error setting Peltier voltage: " + ex.Message);
                    Run = false;
                    // Optionally, turn off the timer and dispose of resources here as well
                }
            }

            // The previous sweep logic for DriveVoltage is now removed as it should be constant.
            // DriveVoltage is now parsed once in buttonStart_Click from textBoxConstantDriveVoltage.
            // The sweep for DriveVoltage is no longer needed in timer_Tick.

         }

        //Some function that handles the voltage sweep for I(V) [myDaq] and R(T) [PowerSupply]


        private void Chart1ScaleChanged(object sender, EventArgs e)
        {
            if (Chart1AutoScale.Checked)
            {
                chart1.ChartAreas[0].AxisX.Minimum = Double.NaN;
                chart1.ChartAreas[0].AxisX.Maximum = Double.NaN;
                chart1.ChartAreas[0].AxisY.Minimum = Double.NaN;
                chart1.ChartAreas[0].AxisY.Maximum = Double.NaN;
            }
            else
            {
                chart1.ChartAreas[0].AxisX.Minimum = Convert.ToDouble(numericChart1XMin.Value);
                chart1.ChartAreas[0].AxisX.Maximum = Convert.ToDouble(numericChart1XMax.Value);
                chart1.ChartAreas[0].AxisY.Minimum = Convert.ToDouble(numericChart1YMin.Value);
                chart1.ChartAreas[0].AxisY.Maximum = Convert.ToDouble(numericChart1YMax.Value);
            }
        }

        private void Chart2ScaleChanged(object sender, EventArgs e)
        {
            if (Chart2AutoScale.Checked)
            {
                chart2.ChartAreas[0].AxisX.Minimum = Double.NaN;
                chart2.ChartAreas[0].AxisX.Maximum = Double.NaN;
                chart2.ChartAreas[0].AxisY.Minimum = Double.NaN;
                chart2.ChartAreas[0].AxisY.Maximum = Double.NaN;
            }
            else
            {
                chart2.ChartAreas[0].AxisX.Minimum = Convert.ToDouble(numericChart2XMin.Value);
                chart2.ChartAreas[0].AxisX.Maximum = Convert.ToDouble(numericChart2XMax.Value);
                chart2.ChartAreas[0].AxisY.Minimum = Convert.ToDouble(numericChart2YMin.Value);
                chart2.ChartAreas[0].AxisY.Maximum = Convert.ToDouble(numericChart2YMax.Value);
            }
        }



        private void buttonClear1_Click(object sender, EventArgs e)
        {
            chart1.Series[0].Points.Clear();
        }

        private void buttonClear2_Click(object sender, EventArgs e)
        {
            chart2.Series[0].Points.Clear();
        }

        private void button_QueryPowSuplName_Click(object sender, EventArgs e)
        {

            string resourceName = textBox_QueryPowSuplName.Text;
                 // Replace with your instrument's resource name
            string command = "*IDN?"; // SCPI command to query the instrument's identity

            try
            {
                // Open a session to the instrument
                //new NationalInstruments.Visa.ResourceManager().Open(resourceName);
                using (MessageBasedSession session = new NationalInstruments.Visa.ResourceManager().Open(resourceName) as MessageBasedSession)
                {
                    if (session == null)
                    {
                        label_QueryPowSuplName.Text = "Failed to open session.";
                        return;
                    }

                    // Write a command to the instrument
                    session.RawIO.Write(command);
                    // Read the response from the instrument
                    string response = session.RawIO.ReadString();
                    label_QueryPowSuplName.Text = response;
                    session.RawIO.Write("OUTPut CH1,OFF");

                }
            }
            catch (VisaException ex)
            {
                label_QueryPowSuplName.Text = ex.Message;
                
            }
            catch (Exception ex)
            {
                label_QueryPowSuplName.Text = ex.Message;
            }
        }

        private void buttonPeltierOn_Click(object sender, EventArgs e)
        {
            try
            {
                if (powerSupplySession == null)
                {
                    powerSupplySession = (MessageBasedSession)new NationalInstruments.Visa.ResourceManager().Open(PeltierPowerSupplyVisaResource);
                    powerSupplySession.RawIO.ReadTimeout = 2000; // Set a read timeout for VISA operations
                    powerSupplySession.RawIO.WriteTimeout = 2000; // Set a write timeout for VISA operations
                }
                powerSupplySession.RawIO.Write("OUTPut CH1,ON");
            }
            catch (VisaException ex)
            {
                MessageBox.Show("Error turning Peltier ON: " + ex.Message);
            }
            catch (Exception ex)
            {
                MessageBox.Show("General error turning Peltier ON: " + ex.Message);
            }
        }

        private void buttonPeltierOff_Click(object sender, EventArgs e)
        {
            try
            {
                if (powerSupplySession != null)
                {
                    powerSupplySession.RawIO.Write("OUTPut CH1,OFF");
                }
            }
            catch (VisaException ex)
            {
                MessageBox.Show("Error turning Peltier OFF: " + ex.Message);
            }
            catch (Exception ex)
            {
                MessageBox.Show("General error turning Peltier OFF: " + ex.Message);
            }
        }

    }
}