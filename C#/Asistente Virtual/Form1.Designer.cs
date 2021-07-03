
namespace Asistente_Virtual
{
    partial class Form1
    {
        /// <summary>
        /// Variable del diseñador necesaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpiar los recursos que se estén usando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben desechar; false en caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código generado por el Diseñador de Windows Forms

        /// <summary>
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido de este método con el editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.panel1 = new System.Windows.Forms.Panel();
            this.principal_button = new System.Windows.Forms.Button();
            this.principal_panel1 = new Asistente_Virtual.principal_panel();
            this.panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // panel1
            // 
            this.panel1.BackColor = System.Drawing.SystemColors.ControlLight;
            this.panel1.Controls.Add(this.principal_button);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Left;
            this.panel1.Location = new System.Drawing.Point(0, 0);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(250, 639);
            this.panel1.TabIndex = 0;
            // 
            // principal_button
            // 
            this.principal_button.BackColor = System.Drawing.Color.LightCyan;
            this.principal_button.Location = new System.Drawing.Point(61, 120);
            this.principal_button.Name = "principal_button";
            this.principal_button.Size = new System.Drawing.Size(104, 44);
            this.principal_button.TabIndex = 0;
            this.principal_button.Text = "button1";
            this.principal_button.UseVisualStyleBackColor = false;
            this.principal_button.Click += new System.EventHandler(this.principal_button_Click);
            // 
            // principal_panel1
            // 
            this.principal_panel1.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.principal_panel1.Location = new System.Drawing.Point(256, 0);
            this.principal_panel1.Name = "principal_panel1";
            this.principal_panel1.Size = new System.Drawing.Size(806, 636);
            this.principal_panel1.TabIndex = 1;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1064, 639);
            this.Controls.Add(this.principal_panel1);
            this.Controls.Add(this.panel1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.panel1.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Button principal_button;
        private principal_panel principal_panel1;
    }
}

