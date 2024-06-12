# Primer Parcial Algoritmos y Estructuras de Datos

# 2. Dada una pila con los datos de dinosaurios resolver lo siguiente actividades:

#Lista

dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": "7000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": "6000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": "15 kg",
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": "56000 kg",
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": "5000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": "10000 kg",
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": "2000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": "23000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": "15000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": "6000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": "2500 kg",
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": "1500 kg",
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": "2700 kg",
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": "5000 kg",
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": "25 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": "200 kg",
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": "450 kg",
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": "15000 kg",
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },

  ]

#TDA

class Stack:

    def __init__(self):
        self.__elements = []

    def push(self, element):
        self.__elements.append(element)

    def pop(self):
        if len(self.__elements) > 0:
            return (
                self.__elements.pop()
            )  # Con el return devuelve el valor que se saca de la pila
        else:
            return None

    def on_top(self):
        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return None

    def size(self):
        return len(self.__elements)
    
pila = Stack()
pila_aux = Stack() 

# a) Contar cuantas especies hay;
print("")
print("PUNTO A")
def contadorespecies(dinosaurios):
    for dinosaurio in dinosaurios:
        pila.push(dinosaurio["especie"])

    especiesunicas = Stack()

    while pila.size() > 0:
        especie = pila.pop()
        if not existe(especiesunicas, especie):
            especiesunicas.push(especie)
    return especiesunicas.size()

def existe(pila1, elemento): 
    encontrado = False
    while pila1.size() > 0:
        dato = pila1.pop()
        if dato == elemento:
            encontrado = True
        pila_aux.push(dato)

    while pila_aux.size() > 0:
        pila1.push(pila_aux.pop())

    return encontrado

numerofinalespecies = contadorespecies(dinosaurios)
print(f"Número de especies: {numerofinalespecies}")

# b) Determinar cuantos descubridores distintos hay;
print("")
print("PUNTO B")
def contardescubridores(dinosaurios):


    for dinosaurio in dinosaurios:
        pila.push(dinosaurio['descubridor'])

    descubridoresunicos = Stack()

    while pila.size() > 0:
        descubridor = pila.pop()
        if not existe(descubridoresunicos,descubridor):
            descubridoresunicos.push(descubridor)
    return descubridoresunicos.size()

numdescrubridores = contardescubridores(dinosaurios)
print(f"Número de descubridores distintos: {numdescrubridores}")


# c) Mostrar todos los dinosaurios que empiecen con T;
print("")
print("PUNTO C")
def dinosauriosT(dinosaurios):
    dinosaurios_con_T = Stack()

    for dinosaurio in dinosaurios:
        if dinosaurio["nombre"].startswith("T"):
            dinosaurios_con_T.push(dinosaurio)

    return dinosaurios_con_T

dinosaurios_con_T = dinosauriosT(dinosaurios)

print("Dinosaurios que empiezan con T:")
while dinosaurios_con_T.size() > 0:
    dino = dinosaurios_con_T.pop()
    print(dino["nombre"])

# d) Mostrar todos los dinosaurios que pesen menos de 275 Kg
print("")
print("PUNTO D")
def dinosauriosmenos275kg(dinosaurios):
    dinos275 = Stack()

    for dinosaurio in dinosaurios:
        peso = int(dinosaurio["peso"].split()[0]) #Conversion del peso (De String a Entero)

        if peso < 275:
            dinos275.push(dinosaurio)

    return dinos275

dinos275 = dinosauriosmenos275kg(dinosaurios)

print("Dinosaurios que pesan menos de 275 kg:")

while dinos275.size() > 0:
    dino = dinos275.pop()
    print(f'{dino["nombre"]} - {dino["peso"]}')

# e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S;
print("")
print("PUNTO E")
def filtrodinos(dinosaurios):
    dinosauriosaparte = Stack()

    for dinosaurio in dinosaurios:
        nombre = dinosaurio["nombre"]
        primera_letra = nombre[0].upper()  # Primera letra en mayus, para comparar.
        if primera_letra in ["A", "Q", "S"]:
            dinosauriosaparte.push(dinosaurio)

    return dinosauriosaparte

dinosauriosaparte = filtrodinos(dinosaurios)

print("Dinosaurios cuyos nombres comienzan con A, Q o S:")
while dinosauriosaparte.size() > 0:
    dino = dinosauriosaparte.pop()
    print(dino["nombre"])

