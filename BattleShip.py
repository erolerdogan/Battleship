import random
import string

class Ships:

    def __init__(self):

        row_alphabet = list(string.ascii_uppercase[0:10])
        dictionary = {row_alphabet[i]: i for i in range(10)}
        self.creating_matrix()

        counter = 0
        while True:
            finished = 1

            for x1 in range(0,10):
                for y1 in range(0,10):
                    if matrix[x1][y1] in range(1,5):
                        finished = 0


            if finished == 0:
                row_input = input("Row:").upper()
                column_input = int(input("Column:"))
                y = dictionary[row_input]

                if matrix[column_input-1][y] == " ":
                    print("You missed! Try again..")

                elif matrix[column_input - 1][y] != "X" and matrix[column_input - 1][y] != " ":
                    print("Congratulations. You hit {} points!".format(matrix[column_input-1][y]))
                    matrix[column_input - 1][y] = "X"

                else:
                    print("You have already hit here before!")
                counter += 1
            else:
                print("You finally finished {}. times".format(counter))
                break

    def creating_matrix(self):

        #To create 10x10 matrix, this comprehension didn't work for me interestingly
        #   row = [" " for i in range(10)]
        #   matrix = [row for j in range(10)]
        ships = [[1], [1], [1], [1], [2, 2], [2, 2], [2, 2], [3, 3, 3], [3, 3, 3], [4, 4, 4, 4]]

        #To create 10x10 matrix
        for i in range(10):
            row = []
            for j in range(10):
                row.append(" ")

            matrix.append(row)

        while len(ships) != 0:
            for num in ships:
                #To choose random location
                x = random.randrange(0, 9)
                y = random.randrange(0, 9)

                # To control the location whether it is free
                free = True
                if y + len(num) < 10:
                    for i in range(len(num)):
                        if matrix[x][y + i] != " ":
                            free = False
                    if free == True:
                        for w in range(len(num)):
                            matrix[x][y + w] = num[w]
                        ships.remove(num)

                elif y + len(num) > 10 > x + len(num):
                    for q in range(len(num)):
                        if matrix[x + q][y] != " ":
                            free = False
                    if free == True:
                        for e in range(len(num)):
                            matrix[x + e][y] = num[e]
                        ships.remove(num)
                else:
                    pass

        #to visualize the table of matrix
        for m in range(len(matrix)):
            print(str(m+1) + "  " + str(matrix[m]))

    def hitting(self, row, column):

        if matrix[row][column - 1] != " ":
            pass
        else:
            print("You hit the {}".format(1))


matrix = []
Ships()
