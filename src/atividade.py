class ThisIsTriangle:
    def verificaTriangulo(x, y, z):
        print(x, y, z)
        if x == 0 and y == 0 and z == 0:
            return False
        elif (x + y > z and x + z > y and z + y > x or x == z):
            return True
        else:
            return False

if __name__ == '__main__':
    x = input('Insira o comprimento da reta: ')
    y = input('Insira o comprimento da reta: ')
    z = input('Insira o comprimento da reta: ')
    print(ThisIsTriangle.verificaTriangulo(x,y,z))
