namespace ketpaneles_meroprogram
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea3 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Legend legend3 = new System.Windows.Forms.DataVisualization.Charting.Legend();
            System.Windows.Forms.DataVisualization.Charting.Series series3 = new System.Windows.Forms.DataVisualization.Charting.Series();
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea4 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Legend legend4 = new System.Windows.Forms.DataVisualization.Charting.Legend();
            System.Windows.Forms.DataVisualization.Charting.Series series4 = new System.Windows.Forms.DataVisualization.Charting.Series();
            this.chart1 = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.chart2 = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.buttonStart = new System.Windows.Forms.Button();
            this.saveFileDialog = new System.Windows.Forms.SaveFileDialog();
            this.timer = new System.Windows.Forms.Timer(this.components);
            this.numericInterval = new System.Windows.Forms.NumericUpDown();
            this.label1 = new System.Windows.Forms.Label();
            this.numericChart1XMax = new System.Windows.Forms.NumericUpDown();
            this.numericChart1XMin = new System.Windows.Forms.NumericUpDown();
            this.numericChart1YMax = new System.Windows.Forms.NumericUpDown();
            this.numericChart1YMin = new System.Windows.Forms.NumericUpDown();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.Chart1AutoScale = new System.Windows.Forms.CheckBox();
            this.numericChart2XMax = new System.Windows.Forms.NumericUpDown();
            this.numericChart2XMin = new System.Windows.Forms.NumericUpDown();
            this.numericChart2YMax = new System.Windows.Forms.NumericUpDown();
            this.numericChart2YMin = new System.Windows.Forms.NumericUpDown();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.Chart2AutoScale = new System.Windows.Forms.CheckBox();
            this.buttonClear1 = new System.Windows.Forms.Button();
            this.buttonClear2 = new System.Windows.Forms.Button();
            this.button_QueryPowSuplName = new System.Windows.Forms.Button();
            this.label_QueryPowSuplName = new System.Windows.Forms.Label();
            this.textBox_QueryPowSuplName = new System.Windows.Forms.TextBox();
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.chart2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericInterval)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericChart1XMax)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericChart1XMin)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericChart1YMax)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericChart1YMin)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericChart2XMax)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericChart2XMin)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericChart2YMax)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericChart2YMin)).BeginInit();
            this.SuspendLayout();
            // 
            // chart1
            // 
            chartArea3.Name = "ChartArea1";
            this.chart1.ChartAreas.Add(chartArea3);
            legend3.Name = "Legend1";
            this.chart1.Legends.Add(legend3);
            this.chart1.Location = new System.Drawing.Point(284, 17);
            this.chart1.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.chart1.Name = "chart1";
            series3.ChartArea = "ChartArea1";
            series3.Legend = "Legend1";
            series3.Name = "Series1";
            this.chart1.Series.Add(series3);
            this.chart1.Size = new System.Drawing.Size(450, 463);
            this.chart1.TabIndex = 0;
            this.chart1.Text = "chart1";
            // 
            // chart2
            // 
            chartArea4.Name = "ChartArea1";
            this.chart2.ChartAreas.Add(chartArea4);
            legend4.Name = "Legend1";
            this.chart2.Legends.Add(legend4);
            this.chart2.Location = new System.Drawing.Point(856, 17);
            this.chart2.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.chart2.Name = "chart2";
            series4.ChartArea = "ChartArea1";
            series4.Legend = "Legend1";
            series4.Name = "Series1";
            this.chart2.Series.Add(series4);
            this.chart2.Size = new System.Drawing.Size(501, 463);
            this.chart2.TabIndex = 1;
            this.chart2.Text = "chart2";
            // 
            // buttonStart
            // 
            this.buttonStart.Location = new System.Drawing.Point(30, 46);
            this.buttonStart.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.buttonStart.Name = "buttonStart";
            this.buttonStart.Size = new System.Drawing.Size(112, 35);
            this.buttonStart.TabIndex = 2;
            this.buttonStart.Text = "Start";
            this.buttonStart.UseVisualStyleBackColor = true;
            this.buttonStart.Click += new System.EventHandler(this.buttonStart_Click);
            // 
            // saveFileDialog
            // 
            this.saveFileDialog.FileOk += new System.ComponentModel.CancelEventHandler(this.saveFileDialog_FileOk);
            // 
            // timer
            // 
            this.timer.Tick += new System.EventHandler(this.timer_Tick);
            // 
            // numericInterval
            // 
            this.numericInterval.Location = new System.Drawing.Point(32, 135);
            this.numericInterval.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.numericInterval.Name = "numericInterval";
            this.numericInterval.Size = new System.Drawing.Size(112, 26);
            this.numericInterval.TabIndex = 3;
            this.numericInterval.Value = new decimal(new int[] {
            100,
            0,
            0,
            0});
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(26, 108);
            this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(166, 20);
            this.label1.TabIndex = 4;
            this.label1.Text = "Sampling Interval (ms)";
            // 
            // numericChart1XMax
            // 
            this.numericChart1XMax.Location = new System.Drawing.Point(210, 369);
            this.numericChart1XMax.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.numericChart1XMax.Maximum = new decimal(new int[] {
            1215752192,
            23,
            0,
            0});
            this.numericChart1XMax.Minimum = new decimal(new int[] {
            1215752192,
            23,
            0,
            -2147483648});
            this.numericChart1XMax.Name = "numericChart1XMax";
            this.numericChart1XMax.Size = new System.Drawing.Size(64, 26);
            this.numericChart1XMax.TabIndex = 5;
            this.numericChart1XMax.Value = new decimal(new int[] {
            50,
            0,
            0,
            0});
            this.numericChart1XMax.ValueChanged += new System.EventHandler(this.Chart1ScaleChanged);
            // 
            // numericChart1XMin
            // 
            this.numericChart1XMin.Location = new System.Drawing.Point(210, 409);
            this.numericChart1XMin.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.numericChart1XMin.Maximum = new decimal(new int[] {
            1215752192,
            23,
            0,
            0});
            this.numericChart1XMin.Minimum = new decimal(new int[] {
            1215752192,
            23,
            0,
            -2147483648});
            this.numericChart1XMin.Name = "numericChart1XMin";
            this.numericChart1XMin.Size = new System.Drawing.Size(64, 26);
            this.numericChart1XMin.TabIndex = 5;
            this.numericChart1XMin.ValueChanged += new System.EventHandler(this.Chart1ScaleChanged);
            // 
            // numericChart1YMax
            // 
            this.numericChart1YMax.Location = new System.Drawing.Point(210, 240);
            this.numericChart1YMax.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.numericChart1YMax.Maximum = new decimal(new int[] {
            1215752192,
            23,
            0,
            0});
            this.numericChart1YMax.Minimum = new decimal(new int[] {
            1215752192,
            23,
            0,
            -2147483648});
            this.numericChart1YMax.Name = "numericChart1YMax";
            this.numericChart1YMax.Size = new System.Drawing.Size(64, 26);
            this.numericChart1YMax.TabIndex = 5;
            this.numericChart1YMax.Value = new decimal(new int[] {
            350,
            0,
            0,
            0});
            this.numericChart1YMax.ValueChanged += new System.EventHandler(this.Chart1ScaleChanged);
            // 
            // numericChart1YMin
            // 
            this.numericChart1YMin.Location = new System.Drawing.Point(210, 280);
            this.numericChart1YMin.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.numericChart1YMin.Maximum = new decimal(new int[] {
            1215752192,
            23,
            0,
            0});
            this.numericChart1YMin.Minimum = new decimal(new int[] {
            1215752192,
            23,
            0,
            -2147483648});
            this.numericChart1YMin.Name = "numericChart1YMin";
            this.numericChart1YMin.Size = new System.Drawing.Size(64, 26);
            this.numericChart1YMin.TabIndex = 5;
            this.numericChart1YMin.Value = new decimal(new int[] {
            300,
            0,
            0,
            0});
            this.numericChart1YMin.ValueChanged += new System.EventHandler(this.Chart1ScaleChanged);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(206, 215);
            this.label2.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(20, 20);
            this.label2.TabIndex = 6;
            this.label2.Text = "Y";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(206, 345);
            this.label3.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(20, 20);
            this.label3.TabIndex = 6;
            this.label3.Text = "X";
            // 
            // Chart1AutoScale
            // 
            this.Chart1AutoScale.AutoSize = true;
            this.Chart1AutoScale.Checked = true;
            this.Chart1AutoScale.CheckState = System.Windows.Forms.CheckState.Checked;
            this.Chart1AutoScale.Location = new System.Drawing.Point(202, 166);
            this.Chart1AutoScale.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.Chart1AutoScale.Name = "Chart1AutoScale";
            this.Chart1AutoScale.Size = new System.Drawing.Size(69, 24);
            this.Chart1AutoScale.TabIndex = 7;
            this.Chart1AutoScale.Text = "Auto";
            this.Chart1AutoScale.UseVisualStyleBackColor = true;
            this.Chart1AutoScale.CheckedChanged += new System.EventHandler(this.Chart1ScaleChanged);
            // 
            // numericChart2XMax
            // 
            this.numericChart2XMax.Location = new System.Drawing.Point(778, 369);
            this.numericChart2XMax.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.numericChart2XMax.Maximum = new decimal(new int[] {
            1215752192,
            23,
            0,
            0});
            this.numericChart2XMax.Minimum = new decimal(new int[] {
            1215752192,
            23,
            0,
            -2147483648});
            this.numericChart2XMax.Name = "numericChart2XMax";
            this.numericChart2XMax.Size = new System.Drawing.Size(64, 26);
            this.numericChart2XMax.TabIndex = 5;
            this.numericChart2XMax.Value = new decimal(new int[] {
            350,
            0,
            0,
            0});
            this.numericChart2XMax.ValueChanged += new System.EventHandler(this.Chart2ScaleChanged);
            // 
            // numericChart2XMin
            // 
            this.numericChart2XMin.Location = new System.Drawing.Point(778, 409);
            this.numericChart2XMin.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.numericChart2XMin.Maximum = new decimal(new int[] {
            1215752192,
            23,
            0,
            0});
            this.numericChart2XMin.Minimum = new decimal(new int[] {
            1215752192,
            23,
            0,
            -2147483648});
            this.numericChart2XMin.Name = "numericChart2XMin";
            this.numericChart2XMin.Size = new System.Drawing.Size(64, 26);
            this.numericChart2XMin.TabIndex = 5;
            this.numericChart2XMin.Value = new decimal(new int[] {
            270,
            0,
            0,
            0});
            this.numericChart2XMin.ValueChanged += new System.EventHandler(this.Chart2ScaleChanged);
            // 
            // numericChart2YMax
            // 
            this.numericChart2YMax.Location = new System.Drawing.Point(778, 240);
            this.numericChart2YMax.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.numericChart2YMax.Maximum = new decimal(new int[] {
            1215752192,
            23,
            0,
            0});
            this.numericChart2YMax.Minimum = new decimal(new int[] {
            1215752192,
            23,
            0,
            -2147483648});
            this.numericChart2YMax.Name = "numericChart2YMax";
            this.numericChart2YMax.Size = new System.Drawing.Size(64, 26);
            this.numericChart2YMax.TabIndex = 5;
            this.numericChart2YMax.Value = new decimal(new int[] {
            500,
            0,
            0,
            0});
            this.numericChart2YMax.ValueChanged += new System.EventHandler(this.Chart2ScaleChanged);
            // 
            // numericChart2YMin
            // 
            this.numericChart2YMin.Location = new System.Drawing.Point(778, 280);
            this.numericChart2YMin.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.numericChart2YMin.Maximum = new decimal(new int[] {
            1215752192,
            23,
            0,
            0});
            this.numericChart2YMin.Minimum = new decimal(new int[] {
            1215752192,
            23,
            0,
            -2147483648});
            this.numericChart2YMin.Name = "numericChart2YMin";
            this.numericChart2YMin.Size = new System.Drawing.Size(64, 26);
            this.numericChart2YMin.TabIndex = 5;
            this.numericChart2YMin.ValueChanged += new System.EventHandler(this.Chart2ScaleChanged);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(774, 215);
            this.label4.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(20, 20);
            this.label4.TabIndex = 6;
            this.label4.Text = "Y";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(774, 345);
            this.label5.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(20, 20);
            this.label5.TabIndex = 6;
            this.label5.Text = "X";
            // 
            // Chart2AutoScale
            // 
            this.Chart2AutoScale.AutoSize = true;
            this.Chart2AutoScale.Checked = true;
            this.Chart2AutoScale.CheckState = System.Windows.Forms.CheckState.Checked;
            this.Chart2AutoScale.Location = new System.Drawing.Point(771, 166);
            this.Chart2AutoScale.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.Chart2AutoScale.Name = "Chart2AutoScale";
            this.Chart2AutoScale.Size = new System.Drawing.Size(69, 24);
            this.Chart2AutoScale.TabIndex = 7;
            this.Chart2AutoScale.Text = "Auto";
            this.Chart2AutoScale.UseVisualStyleBackColor = true;
            this.Chart2AutoScale.CheckedChanged += new System.EventHandler(this.Chart2ScaleChanged);
            // 
            // buttonClear1
            // 
            this.buttonClear1.Location = new System.Drawing.Point(462, 491);
            this.buttonClear1.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.buttonClear1.Name = "buttonClear1";
            this.buttonClear1.Size = new System.Drawing.Size(112, 35);
            this.buttonClear1.TabIndex = 9;
            this.buttonClear1.Text = "Clear";
            this.buttonClear1.UseVisualStyleBackColor = true;
            this.buttonClear1.Click += new System.EventHandler(this.buttonClear1_Click);
            // 
            // buttonClear2
            // 
            this.buttonClear2.Location = new System.Drawing.Point(1245, 489);
            this.buttonClear2.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.buttonClear2.Name = "buttonClear2";
            this.buttonClear2.Size = new System.Drawing.Size(112, 35);
            this.buttonClear2.TabIndex = 9;
            this.buttonClear2.Text = "Clear";
            this.buttonClear2.UseVisualStyleBackColor = true;
            this.buttonClear2.Click += new System.EventHandler(this.buttonClear2_Click);
            // 
            // button_QueryPowSuplName
            // 
            this.button_QueryPowSuplName.Location = new System.Drawing.Point(4, 455);
            this.button_QueryPowSuplName.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.button_QueryPowSuplName.Name = "button_QueryPowSuplName";
            this.button_QueryPowSuplName.Size = new System.Drawing.Size(186, 35);
            this.button_QueryPowSuplName.TabIndex = 16;
            this.button_QueryPowSuplName.Text = "QueryPowSuplName";
            this.button_QueryPowSuplName.UseVisualStyleBackColor = true;
            this.button_QueryPowSuplName.Click += new System.EventHandler(this.button_QueryPowSuplName_Click);
            // 
            // label_QueryPowSuplName
            // 
            this.label_QueryPowSuplName.AutoSize = true;
            this.label_QueryPowSuplName.Location = new System.Drawing.Point(200, 529);
            this.label_QueryPowSuplName.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label_QueryPowSuplName.Name = "label_QueryPowSuplName";
            this.label_QueryPowSuplName.Size = new System.Drawing.Size(134, 20);
            this.label_QueryPowSuplName.TabIndex = 17;
            this.label_QueryPowSuplName.Text = "Supply Response";
            // 
            // textBox_QueryPowSuplName
            // 
            this.textBox_QueryPowSuplName.Location = new System.Drawing.Point(204, 494);
            this.textBox_QueryPowSuplName.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.textBox_QueryPowSuplName.Name = "textBox_QueryPowSuplName";
            this.textBox_QueryPowSuplName.Size = new System.Drawing.Size(403, 26);
            this.textBox_QueryPowSuplName.TabIndex = 18;
            this.textBox_QueryPowSuplName.Text = "USB0::0xF4EC::0x1410::SPD1XECC800032::INSTR";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1390, 706);
            this.Controls.Add(this.textBox_QueryPowSuplName);
            this.Controls.Add(this.label_QueryPowSuplName);
            this.Controls.Add(this.button_QueryPowSuplName);
            this.Controls.Add(this.buttonClear2);
            this.Controls.Add(this.buttonClear1);
            this.Controls.Add(this.Chart2AutoScale);
            this.Controls.Add(this.Chart1AutoScale);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.numericChart2YMin);
            this.Controls.Add(this.numericChart1YMin);
            this.Controls.Add(this.numericChart2YMax);
            this.Controls.Add(this.numericChart1YMax);
            this.Controls.Add(this.numericChart2XMin);
            this.Controls.Add(this.numericChart2XMax);
            this.Controls.Add(this.numericChart1XMin);
            this.Controls.Add(this.numericChart1XMax);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.numericInterval);
            this.Controls.Add(this.buttonStart);
            this.Controls.Add(this.chart2);
            this.Controls.Add(this.chart1);
            this.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.chart2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericInterval)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericChart1XMax)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericChart1XMin)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericChart1YMax)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericChart1YMin)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericChart2XMax)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericChart2XMin)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericChart2YMax)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericChart2YMin)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataVisualization.Charting.Chart chart1;
        private System.Windows.Forms.DataVisualization.Charting.Chart chart2;
        private System.Windows.Forms.Button buttonStart;
        private System.Windows.Forms.SaveFileDialog saveFileDialog;
        private System.Windows.Forms.Timer timer;
        private System.Windows.Forms.NumericUpDown numericInterval;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.NumericUpDown numericChart1XMax;
        private System.Windows.Forms.NumericUpDown numericChart1XMin;
        private System.Windows.Forms.NumericUpDown numericChart1YMax;
        private System.Windows.Forms.NumericUpDown numericChart1YMin;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.CheckBox Chart1AutoScale;
        private System.Windows.Forms.NumericUpDown numericChart2XMax;
        private System.Windows.Forms.NumericUpDown numericChart2XMin;
        private System.Windows.Forms.NumericUpDown numericChart2YMax;
        private System.Windows.Forms.NumericUpDown numericChart2YMin;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.CheckBox Chart2AutoScale;
        private System.Windows.Forms.Button buttonClear1;
        private System.Windows.Forms.Button buttonClear2;
        private System.Windows.Forms.Button button_QueryPowSuplName;
        private System.Windows.Forms.Label label_QueryPowSuplName;
        private System.Windows.Forms.TextBox textBox_QueryPowSuplName;
    }
}

