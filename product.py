class Product:
    def __init__(self, id, type, name, cost):
        self.id = id
        self.type = type
        self.name = name
        self.cost = cost


class Receipt(Product):  # create of subclass for receipt
    def __init__(self, id, type, name, cost, quantity):
        Product.__init__(self, id, type, name, cost)
        self.quantity = quantity  # quantity of each product user buys


filename = "goodsList.csv"
fileobject = open(filename,"r")
filelines = fileobject.readlines()
productlist = {}
for line in filelines:
    productline = line.split(',')
    tempproduct = Product(int(productline[0]),productline[1],productline[2],float(productline[3].replace('\n','')))
    productlist[int(productline[0])] = tempproduct

