import xml.etree.ElementTree as ET
class Diccionario:
    def __init__(self):
        self.PalabrasPositivas = []
        self.PalabrasNegativas = []
        direccion = "BaseDatos/Diccionario.xml"
        ArchivoXML = ET.parse(direccion)
        Raiz = ArchivoXML.getroot()
        self.CargarDiccionario(Raiz)
    
    def CargarDiccionario(self, ArbolXML):
        for Categoria in ArbolXML:
            if Categoria.tag == 'PalabrasChidas':
                for Palabra in Categoria:
                    self.PalabrasPositivas.append(Palabra.text)
            if Categoria.tag == 'PalabrasNoChidas':
                for Palabra in Categoria:
                    self.PalabrasNegativas.append(Palabra.text)

    def CargarNuevasPalabras(self, ArbolXML):
        for Sentimiento in ArbolXML:
            if Sentimiento.tag == 'sentimientos_positivos':
                for Palabra in Sentimiento:
                    self.PalabrasPositivas.append(Palabra.text)
            if Sentimiento.tag == 'sentimientos_negativos':
                for Palabra in Sentimiento:
                    self.PalabrasNegativas.append(Palabra.text)
        #self.OrdernarPalabras()

    def GuardarDiccionario(self):
        RaizDiccionario = ET.Element('Diccionario')
        PalbrasChidas = ET.SubElement(RaizDiccionario, 'PalabrasChidas')
        PalabrasNoChidas = ET.SubElement(RaizDiccionario, 'PalabrasNoChidas')
        for Palabra in self.PalabrasPositivas:
            TagPalabra = ET.SubElement(PalbrasChidas, 'Palabra')
            TagPalabra.text = Palabra
        for Palabra in self.PalabrasNegativas:
            TagPalabra = ET.SubElement(PalabrasNoChidas, 'Palabra')
            TagPalabra.text = Palabra
        Arbol = ET.ElementTree(RaizDiccionario)
        ET.indent(Arbol, space="\t", level=0)
        Arbol.write('BaseDatos/Diccionario.xml', encoding="utf-8")

    def ObtenerPalbrasJSON(self):
        SalidaJSON = {
            "PalabrasPositivas":[],
            "PalabrasNegativas": []
        }
        for Palabra in self.PalabrasPositivas:
            SalidaJSON['PalabrasPositivas'].append(Palabra)
        for Palabra in self.PalabrasNegativas:
            SalidaJSON['PalabrasNegativas'].append(Palabra)
        return SalidaJSON
    '''
    def OrdernarPalabras(self):
        Pandas.Sort(self.PalabrasPositivas)
        Pandas.Sort(self.PalabrasNegativas)
    '''
    def Reiniciar(self):
        RaizDiccionario = ET.Element('Diccionario')
        PalbrasChidas = ET.SubElement(RaizDiccionario, 'PalabrasChidas')
        PalabrasNoChidas = ET.SubElement(RaizDiccionario, 'PalabrasNoChidas')
        Arbol = ET.ElementTree(RaizDiccionario)
        ET.indent(Arbol, space="\t", level=0)
        Arbol.write('BaseDatos/Diccionario.xml', encoding="utf-8")