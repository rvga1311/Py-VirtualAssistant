using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Asistente_Virtual
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            switchPrincipal();
        }

        private void switchPrincipal()
        {
            principal_panel1.Show();
            principal_panel1.BringToFront();
        }

        private void principal_button_Click(object sender, EventArgs e)
        {
            switchPrincipal();
        }

        private void clearPanel(Panel.ControlCollection ControlCollection)
        {
            foreach (Control control in ControlCollection)
            {
                if (control is TextBox)
                {
                    control.Text = "";
                }
            }
        }
    }
}
