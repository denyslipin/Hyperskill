class Matrix():

    def __init__(self):
        self.r = 0
        self.c = 0
        self.matrix = []

    def menu(self):
        print("1. Add matrices\n2. Multiply matrix by a constant")
        print("3. Multiply matrices\n4. Transpose matrix\n5. Calculate a determinant")
        print("6. Inverse matrix\n0. Exit")
        x = int(input("Your choice: "))
        print()
        if x == 1:
            return self.add_matrices()
        elif x == 2:
            return self.multiplication()
        elif x == 3:
            return self.multiply_matrices()
        elif x == 4:
            return self.transpose_matrix()
        elif x == 5:
            return self.calculate_determinant()
        elif x == 6:
            return self.inverse_matrix()
        elif x == 0:
            return 0
        else:
            print("ERROR")
    
    def create(self, r):
        self.matrix = []
        for i in range(r):
            self.matrix.append([int(x) if x.isdigit() else float(x) for x in input().split()])
        return self.matrix

    def add_matrices(self):
        r1, c1 = [int(x) for x in input("Enter size of first matrix: ").split()]
        print("Enter first matrix:")
        m1 = self.create(r1)
        r2, c2 = [int(x) for x in input("Enter size of second matrix: ").split()]
        print("Enter first matrix:")
        m2 = self.create(r2)
        if r1 == r2 and c1 == c2:
            new_matrix = [[0 for x in range(c1)] for x in range(r1)]
            print("The result is:")
            for i in range(r1):
                for j in range(c1):
                    new_matrix[i][j] = str(m1[i][j] + m2[i][j])
                print(" ".join(new_matrix[i]))
        else:
            print("The operation cannot be performed.")
        
    def multiplication(self):
        r3, c3 = [int(x) for x in input("Enter size of first matrix: ").split()]
        print("Enter first matrix:")
        m3 = self.create(r3)
        x = input("Enter constant: ")
        number = int(x) if x.isdigit() else float(x)
        new_matrix = [[0 for x in range(c3)] for x in range(r3)]
        print("The result is:")
        for i in range(r3):
            for j in range(c3):
                new_matrix[i][j] = str(m3[i][j] * number)
            print(" ".join(new_matrix[i]))

    def multiply_matrices(self):
        r1, c1 = [int(x) for x in input("Enter size of first matrix: ").split()]
        print("Enter first matrix:")
        m1 = self.create(r1)
        r2, c2 = [int(x) for x in input("Enter size of second matrix: ").split()]
        print("Enter first matrix:")
        m2 = self.create(r2)
        if c1 == r2:
            new_matrix = [[0 for x in range(c1)] for x in range(r1)]
            print("The result is:")
            for i in range(r1):
                new_matrix[i] = [sum([m1[i][z] * m2[z][y] for z in range(r2)]) for y in range(c2)]
                print(" ".join([str(x) for x in new_matrix[i]]))
        else:
            print("The operation cannot be performed.")
            
    def transpose_matrix(self):
        print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
        x = int(input("Your choice: "))
        r3, c3 = [int(x) for x in input("Enter matrix size: ").split()]
        print("Enter matrix:")
        m3 = self.create(r3)
        if x == 1:
            return list(map(print, *m3))
        elif x == 2:
            return list(map(print, *[row[::-1] for row in m3[::-1]]))
        elif x == 3:
            return list(map(lambda x: print(*x[::-1]), m3))
        elif x == 4:
            return list(map(lambda x: print(*x), m3[::-1]))
        else:
            print("ERROR")

    def calculate_determinant(self):
        r4, c4 = [int(x) for x in input("Enter matrix size: ").split()]
        print("Enter matrix:")
        m4 = self.create(r4)
        print("The result is:")
        print(self.determinant(m4))

    def determinant(self, a):
        if len(a) == 1:
            return a[0][0]
        return sum(a[i][0] * ((-1) ** i) *
                self.determinant([a[row][1:] for row in range(len(a)) if row != i])
                for i in range(len(a)))
                
    def inverse_matrix(self):
        r5, c5 = [int(x) for x in input("Enter matrix size: ").split()]
        print("Enter matrix:")
        m5 = self.create(r5)
        det = self.determinant(m5)
        if det == 0:
            print("This matrix doesn't have an inverse.")
        else:
            cofactors = [
                [
                    ((-1) ** (x + y)) * self.determinant([
                        [m5[col][row] for col in range(c5) if col != x]
                        for row in range(r5) if row != y
                    ]) for x in range(c5)
                ] for y in range(r5)
            ]
            print('The result is:')
            c = 1 / det
            for row in cofactors:
                s = [c * x for x in row]
                print(*s)

    def main(self):
        while self.menu() != 0:
            print()
            continue
        exit()

program = Matrix()
program.main()
