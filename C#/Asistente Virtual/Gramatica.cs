using System;
using System.Collections.Generic;
using System.Linq;
using System.Speech.Recognition;
using System.Text;
using System.Threading.Tasks;

namespace Asistente_Virtual
{
    public class Gramatica
    {

        public Gramatica()
        {

        }

        static public Grammar loadGrammarWeb() //gramatica para busqueda web por voz
        {
            Choices webs = new Choices(new string[] { "google", "youtube", "wikipedia" });
            GrammarBuilder webPhrases = new GrammarBuilder("buscar");
            webPhrases.AppendDictation();
            webPhrases.Append("en");
            webPhrases.Append(new SemanticResultKey("browser", webs)); //etiqueta para frases de esta manera

            Grammar webGrammar = new Grammar(webPhrases);

            return webGrammar;

        }
    }
}
