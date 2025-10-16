using Ivi.Visa;
using NationalInstruments.Visa;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO.Ports;
using System.Linq;
using System.Resources;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace ketpaneles_meroprogram
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {

            


        
            
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1());


        }
    }
}

/*
 try
            {
                // Create a resource manager
                var resourceManager = new ResourceManager();

                // Connect to the instrument (replace with your instrument's VISA address)
                using (var session = resourceManager.Open("TCPIP0::192.168.1.100::INSTR") as IMessageBasedSession)
                {
                    // Send a SCPI command
                    session.FormattedIO.WriteLine("*IDN?");

                    // Read the response
                    string response = session.FormattedIO.ReadLine();
                    Console.WriteLine("Instrument ID: " + response);
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
            }
 */