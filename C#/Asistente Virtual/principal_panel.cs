using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Speech.Recognition;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Threading;
using System.Globalization;

namespace Asistente_Virtual
{
    public partial class principal_panel : UserControl
    {
        SpeechRecognitionEngine voiceRecog = new SpeechRecognitionEngine();

        public principal_panel()
        {
            InitializeComponent();
        }

        private void recVoice() 
        {

            voiceRecog.LoadGrammar(Gramatica.loadGrammarWeb());

            voiceRecog.SetInputToDefaultAudioDevice();
            voiceRecog.SpeechRecognized += voiceRecog_SpeechRecognized;
            voiceRecog.RecognizeAsync(RecognizeMode.Multiple);
            
        }

        private void voiceRecog_SpeechRecognized(object sender, SpeechRecognizedEventArgs e)
        {
            recordTxt_txtBox.Text = e.Result.Text;
            if (e.Result.Semantics.ContainsKey("browser")) 
                webBrowser(e.Result.Text, e.Result.Semantics["browser"].Value.ToString());
        }

        private void webBrowser(string speech, string browser)
        {
            string endPhrase = speech.Remove(0, 7);
            int start = endPhrase.IndexOf(browser);
            endPhrase = endPhrase.Remove(start - 3, browser.Length + 3);

            System.Diagnostics.Process.Start("https://www.google.com/search?client=opera-gx&q="+endPhrase.Trim());
        }

        private void button1_Click(object sender, EventArgs e)
        {
            List<RecognizerInfo> engines = SpeechRecognitionEngine.InstalledRecognizers().ToList();

            for (int i = 0; i < engines.Count; i++)
            {
                Console.WriteLine(engines[i].Culture);
            }
            //recVoice();
        }

    }
}
