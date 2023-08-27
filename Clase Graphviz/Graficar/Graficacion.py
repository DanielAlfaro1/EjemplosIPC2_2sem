import os

ElString = '''graph ""
    {
        fontname="Helvetica,Arial,sans-serif"
        node [fontname="Helvetica,Arial,sans-serif"]
        edge [fontname="Helvetica,Arial,sans-serif"]

        subgraph Prueba1 
        {
            n1 [label="EJEMPLO 1"];
        
            n2 [label="t=5"];
            n3 [label="A=4"];
            n1 -- n2;
            n1 -- n3;
            
            # Fila 1
            n4 [label="2"];
            n1 -- n4;
            n5 [label="3"];
            n1 -- n5;
            n6 [label="0"];
            n1 -- n6;
            n7 [label="4"];
            n1 -- n7;
            
            n8 [label="0"];
            n4 -- n8;
            n9 [label="0"];
            n5 -- n9;
            n10 [label="6"];
            n6 -- n10;
            n11 [label="3"];
            n7 -- n11;
            
            n12 [label="3"];
            n8 -- n12;
            n13 [label="4"];
            n9 -- n13;
            n14 [label="0"];
            n10 -- n14;
            n15 [label="2"];
            n11 -- n15;
            
            n16 [label="1"];
            n12 -- n16;
            n17 [label="0"];
            n13 -- n17;
            n18 [label="1"];
            n14 -- n18;
            n19 [label="5"];
            n15 -- n19;
            
            n20 [label="0"];
            n16 -- n20;
            n21 [label="0"];
            n17 -- n21;
            n22 [label="3"];
            n18 -- n22;
            n23 [label="1"];
            n19 -- n23;
        }
    }
'''

def CrearArchivo(Nombre, ElTexto):
    Ubicacion = "Clase Graphviz/Imagenes/"+Nombre+".dot"
    archivo = open(Ubicacion, "w")
    archivo.write(ElTexto)
    archivo.close()

#dot -Tsvg ElArchivo.dot > LaGrafica.svg

def CrearImagen(NombreArchivo, NombreImagen):
    Archivo = "\"Clase Graphviz/Imagenes/"+NombreArchivo+".dot\""
    Imagen = "\"Clase Graphviz/Imagenes/"+NombreImagen+".svg\""
    comando = "dot -Tsvg "+Archivo+" > "+Imagen
    os.system('cmd /c '+comando)

