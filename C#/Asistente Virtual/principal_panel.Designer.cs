
namespace Asistente_Virtual
{
    partial class principal_panel
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

        #region Código generado por el Diseñador de componentes

        /// <summary> 
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido de este método con el editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(principal_panel));
            this.record_button = new System.Windows.Forms.Button();
            this.recordTxt_txtBox = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // record_button
            // 
            this.record_button.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.record_button.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("record_button.BackgroundImage")));
            this.record_button.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.record_button.Location = new System.Drawing.Point(332, 164);
            this.record_button.Name = "record_button";
            this.record_button.Size = new System.Drawing.Size(132, 166);
            this.record_button.TabIndex = 0;
            this.record_button.UseVisualStyleBackColor = false;
            this.record_button.Click += new System.EventHandler(this.button1_Click);
            // 
            // recordTxt_txtBox
            // 
            this.recordTxt_txtBox.Font = new System.Drawing.Font("Segoe Print", 16.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.recordTxt_txtBox.Location = new System.Drawing.Point(248, 336);
            this.recordTxt_txtBox.Multiline = true;
            this.recordTxt_txtBox.Name = "recordTxt_txtBox";
            this.recordTxt_txtBox.Size = new System.Drawing.Size(310, 130);
            this.recordTxt_txtBox.TabIndex = 1;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Viner Hand ITC", 48F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(71, 15);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(698, 129);
            this.label1.TabIndex = 2;
            this.label1.Text = "Asistente Virtual";
            // 
            // principal_panel
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.Controls.Add(this.label1);
            this.Controls.Add(this.recordTxt_txtBox);
            this.Controls.Add(this.record_button);
            this.Name = "principal_panel";
            this.Size = new System.Drawing.Size(806, 636);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button record_button;
        private System.Windows.Forms.TextBox recordTxt_txtBox;
        private System.Windows.Forms.Label label1;
    }
}
