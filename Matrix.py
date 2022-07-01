if __name__ != '__main__':
    class Matrix:
        '''The matrix class is based on the standard list. 
        Designed for creating and processing matrices. 
        Contains overload methods:
            __init__(self, **kwargs)
            __setattr__(self, attr, value)
            __getitem__(self, row)
            __setitem__(self, row)
            __delitem__(self, row)
            __str__(self)
            __iter__(self)
            __add__(self, other, needToReturn=True), __radd__(self, other, needToReturn=True), __iadd__(self, other, needToReturn=True)
            __sub__(self, other, needToReturn=True), __rsub__(self, other, needToReturn=True), __isub__(self, other, needToReturn=True)
            __mul__(self, other, needToReturn=True), __rmul__(self, other, needToReturn=True), __imul__(self, other, needToReturn=True)
         and other methods:

            static:
                createMatrix(matrix)
                createZeroMatrix(rows, columns)
                readMatrixFromFile(nameOfFile)

            saveMatrixInFile(self, nameOfFile)

            getMatrix(self)
            getNumberOfRows(self)
            getNumberOfColumns(self)
            getRow(self, row)
            getColumn(self, column)
            getElement(self, row, column)

            setRow(self, row, value)
            setColumn(self, column, value)
            setElement(self, row, column, value)

            deleteRow(self, row)
            deleteColumn(self, column)

            swapRows(self, firstRow, secondRow)
            swapColumns(self, firstColumn, secondColumn)
            mulRowWithNumber(self, row, number)
            mulColumnWithNumber(self, column, number)
            mulRowWithNumberAndSumWithAnotherRow(self, rowForMul, number, rowForSum)
            mulColumnWithNumberAndSumWithAnotherColumn(self, columnForMul, number, columnForSum)
            addZeroRow(self, row)
            addZeroColumn(self, column)

            addWithNumber(self, other)
            addWithMatrix(self, other)

            subWithNumber(self, other)
            subWithMatrix(self, other)

            mulWithNumber(self, other)
            mulWithMatrix(self, other)

            findDeterminant(self)
            findMinor(self, row, column)
            findAlgebraicComplement(self, row, column)

            makeTransposeMatrix(self)
            makeAssociativeMatrix(self)
            makeInvertibleMatrix(self)

        Author: Vadim Karchagin
        '''


#---Methods for initialization as instance and setting attributes---

        def __init__(self, **kwargs):
            '''Initialize an instance.

            In argument can be "matrix=" or "rows" and "columns"
            Which matrix will be created depends on the arguments: 
                if "matrix=" is specified, the transferred matrix will be created
                    (the matrix argument must contain a list in the list. For example: [[1, 2, 4], [4, 9, 3]])
                if "rows=" and "columns=" are specified, a zero matrix of a given size will be created
                    (quantity of rows and columns must be positive integer)

            Returns Matrix. Type Matrix
            '''
   
            if 'matrix' in kwargs:
                self.__matrix = kwargs['matrix']
                self.__rows = len(kwargs['matrix'])
                self.__columns = len(kwargs['matrix'][0])
            elif 'rows' in kwargs and 'columns' in kwargs:
                self.__matrix = [[0.0 for i in range(kwargs['columns'])] for j in range(kwargs['rows'])]
                self.__rows = kwargs['rows']
                self.__columns = kwargs['columns']
            else:
                raise AttributeError('Invalid arguments. The matrix may have "matrix=" or "rows=" and "columns="')
        

        @staticmethod
        def createMatrix(matrix):
            '''Static method for initialize an instance.

            Argument must contain a list in the list. For example: [[1, 2, 4], [4, 9, 3]]

            Returns Matrix. Type Matrix
            '''

            return Matrix(matrix=matrix)


        @staticmethod
        def createZeroMatrix(rows, columns):
            '''Static method for initialize an instance.

            Quantity of rows and columns must be positive integer

            Returns Matrix. Type Matrix
            '''

            return Matrix(rows=rows, columns=columns)


        @staticmethod
        def readMatrixFromFile(nameOfFile):
            '''Static method for initialize an instance. 

            The file must be in the same directory as the program.
            The matrix should be in the file in the format where the separators are spaces and line breaks.
            For example:
                3 2 1
                4 5 6
                6 1 4

            Argument must be string(name of file) with extension. For example: data.txt

            Returns Matrix. Type Matrix
            '''

            f = open(nameOfFile)
            matrix = f.read()
            f.close()

            matrix = matrix.split('\n')
            rows = len(matrix)
            for i in range(rows):
                matrix[i] = matrix[i].split(' ')

            return Matrix(matrix=matrix)
            

        def __setattr__(self, attr, value):
            '''Overload method for setting matrix attributes'''

            if attr == '_Matrix__matrix':
                if type(value) == list and type(value[0]) == list:
                    quantityOfRows = len(value)
                    lengthOfRow = len(value[0])
                    for i in range(0, quantityOfRows):
                        if len(value[i]) != lengthOfRow:
                            raise ValueError('Invalid list. The number of elements in the columns is not the same')
                        for j in range(0, lengthOfRow):
                            if type(value[i][j]) == float:
                                pass
                            elif type(value[i][j]) != float and (type(value[i][j]) == int or type(value[i][j]) == str and value[i][j].isdigit()):
                                value[i][j] = float(value[i][j])
                            else:
                                raise TypeError('Invalid list. Matrix elements must be a number, delimiter must be a dot')
                    self.__dict__[attr] = value
                    self.__dict__['_Matrix__rows'] = quantityOfRows
                    self.__dict__['_Matrix__columns'] = lengthOfRow
                else:
                    raise TypeError('Invalid matrix argument. The matrix argument must contain a list in the list. For example: [[1, 2, 4], [4, 9, 3]]')
            elif attr == '_Matrix__rows' or attr == '_Matrix__columns':
                if type(value) == int and value > 0:
                    self.__dict__[attr] = value
                else:
                    raise ValueError(f'Invalid quantity of {attr}. Quantity of {attr} should be positive integer')
            else:
                raise AttributeError(f'The matrix does not have the attribute {attr}')

#-------------------------------------------------------------------

    
        def saveMatrixInFile(self, nameOfFile):
            '''Method for saving Matrix in file with name nameOfFile
            
            The file will be created in the same directory where the program is located.
            If a file with the same name already exists, it will be overwritten.

            Argument must be string(name of file) with extension. For example: data.txt
   
            Returns a record confirmation if recording is successful.
            '''

            matrix = self.__matrix
            for i in range(self.__rows):
                for j in range(self.__columns):
                    matrix[i][j] = str(matrix[i][j])

            data = ''
            for row in matrix:
                data += ' '.join(row)
                data += '\n'

            f = open(nameOfFile, 'w')
            data = f.write(data[0:-1])
            f.close()

            return (f'Saving to file "{nameOfFile}" was successful')


#---Methods for getting data---

        def getMatrix(self):
            '''Method for getting matrix

            Returns list in the list. Type list
            '''

            return self.__matrix


        def getNumberOfRows(self):
            '''Method for getting the number of matrix rows
            
            Returns number of rows. Type int
            '''

            return self.__rows


        def getNumberOfColumns(self):
            '''Method for getting the number of matrix columns
            
            Returns number of columns. Type int
            '''

            return self.__columns


        def __getitem__(self, row):
            '''Overload method for getting a row of matrix

            Argument must be positive integer

            Returns a row. Type list

            !I do not recommend using Matrix[i][j] to get an element,
            because in this method row indices start at 1, and column indices start at 0.
            To get an element of a matrix use Matrix.getElement
            '''

            if type(row) == int:
                row -= 1
                if 0 <= row < self.__rows:
                    return self.__matrix[row]
                else:
                    raise IndexError('Invalid index. Row with such number does not exist')
            else:
                raise TypeError('Invalid index. The row number should be a positive integer')


        def getRow(self, row):
            '''Method for getting a row of matrix
            
            Argument must be positive integer

            Returns a row. Type list
            '''

            return self.__getitem__(row)


        def getColumn(self, column):
            '''Method for getting a column of matrix
            
            Argument must be positive integer

            Returns a column. Type list
            '''

            if type(column) == int:
                column -= 1
                if 0 <= column < self.__columns:
                    elements = []
                    for row in self.__matrix:
                        elements.append(row[column])
                    return elements
                else:
                    raise IndexError('Invalid index. Column with such number does not exist')
            else:
                raise TypeError('Invalid index. The column number should be a positive integer')


        def getElement(self, row, column):
            '''Method for getting an element of matrix
            
            Arguments must be positive integers

            Returns an element with indexes row and column. Type int or float
            '''

            if type(row) == int and type(column) == int:
                row -= 1
                column -= 1
                if 0 <= row < self.__rows and 0 <= column < self.__columns:
                    return self.__matrix[row][column]
                else:
                    raise IndexError('Invalid index. Row or column with such number does not exist')
            else:
                raise TypeError('Invalid index. The row or column number should be a positive integer')

#------------------------------


#---Methods for setting data---

        def __setitem__(self, row, value):
            '''Overload method for setting a row of matrix
            
            Argument index must be positive integer, argument value must be a list of the same dimension as the matrix

            !I do not recommend using Matrix[i][j] to set an element,
            because in this method row indices start at 1, and column indices start at 0.
            To set an element of a matrix use Matrix.setElement
            '''

            if type(value) == list and len(value) == self.__rows:
                if type(row) == int:
                    if 0 < row <= self.__rows:
                        lengthValue = len(value)
                        for i in range(lengthValue):
                            if type(value[i]) == float:
                                pass
                            elif type(value[i]) != float and (type(value[i]) == int or type(value[i]) == str and value[i].isdigit()):
                                value[i] = float(value[i])
                            else:
                                raise ValueError("Invalid value. Elements must be a number, delimiter must be a dot")
                        self.__matrix[row-1] = value
                    else:
                        raise IndexError('Invalid index. Row with such number does not exist')
                else:
                    raise TypeError('Invalid index. The row number should be a positive integer')
            else:
                raise ValueError("Invalid value. The value must be a list of the same dimension as the matrix. For example: [1, 3, 4]")
                

        def setRow(self, row, value):
            '''Method for setting a row of matrix
            
            Argument index must be positive integer, argument value must be a list of the same dimension as the matrix
            '''

            self.__setitem__(row, value)

        
        def setColumn(self, column, value):
            '''Method for setting a column of matrix
            
            Argument index must be positive integer, argument value must be a list of the same dimension as the matrix
            '''

            if type(value) == list and len(value) == self.__columns:
                lengthValue = len(value)
                for i in range(lengthValue):
                    if type(value[i]) == float:
                        pass
                    elif type(value[i]) != float and (type(value[i]) == int or type(value[i]) == str and value[i].isdigit()):
                        value[i] = float(value[i])
                    else:
                        raise ValueError("Invalid value. Elements must be a number, delimiter must be a dot")
            else:
                raise ValueError("Invalid value. The value must be a list of the same dimension as the matrix. For example: [1, 3, 4]")
            if type(column) == int:
                column -= 1
                if 0 <= column < self.__columns:
                    for i in range(self.__rows):
                        self.__matrix[i][column] = value[i]
                else:
                    raise IndexError('Invalid index. Column with such number does not exist')
            else:
                raise TypeError('Invalid index. The column number should be a positive integer')
            

        def setElement(self, row, column, value):
            '''Method for setting an element of matrix
            
            Arguments index must be positive integers, argument value must be of the same type as the elements of the matrix
            '''

            if type(value) == float:
                pass
            elif type(value) != float and (type(value) == int or type(value) == str and value.isdigit()):
                value = float(value)
            else:
                raise ValueError("Invalid value. Elements must be a number, delimiter must be a dot")

            if type(row) == int and type(column) == int:
                if 0 < row <= self.__rows and 0 < column <= self.__columns:
                    self.__matrix[row-1][column-1] = value
                else:
                    raise IndexError('Invalid index. Row or column with such number does not exist')
            else:
                raise TypeError('Invalid index. The row or column number should be a positive integer')

#------------------------------


#---Methods for deleting data---

        def __delitem__(self, row):
            '''Overload method for deleting a row of matrix
            
            Argument index must be positive integer
            '''
            if self.__rows > 1:
                if type(row) == int:
                    if 0 < row <= self.__rows:
                        self.__matrix.pop(row-1)
                        self.__rows -= 1
                    else:
                        raise IndexError('Invalid index. Row with such number does not exist')
                else:
                    raise TypeError('Invalid index. The row number should be a positive integer')
            else:
                raise Warning('Сannot delete a row because matrix has 1 row')

            
        def deleteRow(self, row):
            '''Method for deleting a row of matrix
            
            Argument index must be positive integer
            '''

            self.__delitem__(row)

        
        def deleteColumn(self, column):
            '''Method for deleting a column of matrix
            
            Argument index must be positive integer
            '''

            if self.__columns > 1:
                if type(column) == int:
                    column -= 1
                    if 0 <= column < self.__columns:
                        for i in range(self.__rows):
                            self.__matrix[i].pop(column)
                        self.__columns -= 1
                    else:
                        raise IndexError('Invalid index. Column with such number does not exist')
                else:
                    raise TypeError('Invalid index. The column number should be a positive integer')
            else:
                raise Warning('Сannot delete a column because matrix has 1 row')

#-------------------------------

        def __str__(self):
            '''Overload method for transformation the matrix in string
            
            This is necessary when using the "str" operator
            '''

            string = ''
            for row in self.__matrix:
                string += '['
                for element in row:
                    string += str(element) + ', '
                string = string[:-2] + ']\n'
            return string[0:-1]


        def __iter__(self):
            '''Overload method for transformation the matrix in string
            
            This is necessary when using in the "for" cycle
            '''

            return iter(self.__matrix)


#---Elementary row or column conversions---

        def swapRows(self, firstRow, secondRow):
            '''Method for swapping rows

            Arguments are indices in the matrix, must be positive integers
            '''

            if firstRow != secondRow:
                self[secondRow], self[firstRow] = self[firstRow], self[secondRow]
            else:
                raise Warning('Rows cannot have the same index')


        def swapColumns(self, firstColumn, secondColumn):
            '''Method for swapping columns
            
            Arguments are the row numbers in the matrix.
            '''
            if firstColumn != secondColumn:
                temp = self.getColumn(firstColumn)
                self.setColumn(firstColumn, self.getColumn(secondColumn))
                self.setColumn(secondColumn, temp)
            else:
                raise Warning('Columns cannot have the same index')


        def mulRowWithNumber(self, row, number):
            '''Method for multiplying a row with a number

            Row argument must be positive integer, number argument must be a number, not zero
            '''

            if type(number) == int or type(number) == float:
                if number != 0:
                    for i in range(self.__rows):
                        self[row][i] = round(self[row][i] * number, 4)
                else:
                    raise ValueError('The number cannot be zero')
            else:
                raise TypeError('The number invalid, must be of type int or float')


        def mulColumnWithNumber(self, column, number):
            '''Method for multiplying a column with a number

            Row argument must be positive integer, number argument must be a number, not zero
            '''

            if type(number) == int or type(number) == float:
                if type(column) == int:
                    column -= 1
                    if 0 <= column < self.__columns:
                        if number != 0:
                            for i in range(1, self.__rows + 1):
                                self[i][column] = round(self[i][column] * number, 4)
                        else:
                            raise ValueError('The number cannot be zero')
                    else:
                        raise IndexError('Invalid index. Column with such number does not exist')
                else:
                    raise TypeError('Invalid index. The column number should be a positive integer')
            else:
                raise TypeError('The number invalid, must be of type int or float')

        
        def mulRowWithNumberAndSumWithAnotherRow(self, rowForMul, number, rowForSum):
            '''Method for multiplying rowForMul with number (this row remains unchanged) 
            then the resulting rowForMul is added to the rowForSum

            Can be used to add a row to another row if you specify the argument number 1

            Arguments rowForMul, rowForSum must be positive integer, number argument must be a number, not zero
            '''

            if rowForMul == rowForSum:
                raise Warning('Rows cannot have the same index')

            if type(number) == int or type(number) == float:
                if number != 0:
                    for i in range(1, self.__columns + 1):
                        self.setElement(rowForSum, i, round(self.getElement(rowForMul, i) * number + self.getElement(rowForSum, i), 4))
                else:
                    raise ValueError('The number cannot be zero')
            else:
                raise TypeError('The number invalid, must be of type int or float')


        def mulColumnWithNumberAndSumWithAnotherColumn(self, columnForMul, number, columnForSum):
            '''Method for multiplying columnForMul with number (this column remains unchanged) 
            then the resulting columnForMul is added to the columnForSum

            Can be used to add a column to another column if you specify the argument number 1

            Arguments columnForMul, columnForSum must be positive integer, number argument must be a number, not zero
            '''

            if columnForMul == columnForSum:
                raise Warning('Columns cannot have the same index')

            if type(number) == int or type(number) == float:
                if number != 0:
                    for i in range(1, self.__rows + 1):
                        self.setElement(i, columnForSum, round(self.getElement(i, columnForMul) * number + self.getElement(i, columnForSum), 4))  
                else:
                    raise ValueError('The number cannot be zero')
            else:
                raise TypeError('The number invalid, must be of type int or float')


        def addZeroRow(self, row):
            '''Method for adding zero row
            
            The argument row is the index where you want to insert zero row, must be positive integer
            '''

            if type(row) == int:
                if 0 < row <= self.__rows + 1:
                    self.__matrix.insert(row - 1, [0.0 for i in range(self.__columns)])
                    self.__rows += 1
                else:
                    raise IndexError('Invalid index. row with such number does not exist')
            else:
                raise TypeError('Invalid index. The row number should be a positive integer')


        def addZeroColumn(self, column):
            '''Method for adding zero row
            
            The argument column is the index where you want to insert zero column, must be positive integer
            '''

            if type(column) == int:
                if 0 < column <= self.__columns + 1:
                    for i in range(self.__rows):
                        self.__matrix[i].insert(column - 1, 0.0)
                    self.__columns += 1
                else:
                    raise IndexError('Invalid index. Column with such number does not exist')
            else:
                raise TypeError('Invalid index. The column number should be a positive integer')

#-------------------------------------------


#---Addition methods---

        def __add__(self, other, needToReturn=True):
            '''Overload method for addition with another operand, which is on the right

            Argument must be Matrix or int or float

            Returns the result of adding a matrix to a number or another matrix. Type Matrix
            '''

            if needToReturn:
                if type(other) == int or type(other) == float:
                    newMatrix = Matrix(rows=self.__rows, columns=self.__columns)
                    for i in range(self.__rows):
                        for j in range(self.__columns):
                            newMatrix[i+1][j] = round(self.__matrix[i][j] + other, 4)
                    return newMatrix
                elif type(other) == Matrix and type(other[1]) == list and self.__rows == other.getNumberOfRows() and self.__columns == other.getNumberOfColumns():
                    newMatrix = Matrix(rows=self.__rows, columns=self.__columns)
                    for i in range(self.__rows):
                        for j in range(self.__columns):
                            newMatrix[i+1][j] = round(self.__matrix[i][j] + other.getElement(i+1, j+1), 4)
                    return newMatrix
                else:
                    raise TypeError('The other operand invalid. The other operand must be of type Matrix, int or float')
            else:
                if type(other) == int or type(other) == float:
                    for i in range(self.__rows):
                        for j in range(self.__columns):
                            self.__matrix[i][j] = round(self.__matrix[i][j] + other, 4)
                elif type(other) == Matrix and type(other[1]) == list and self.__rows == other.getNumberOfRows() and self.__columns == other.getNumberOfColumns():
                    for i in range(self.__rows):
                        for j in range(self.__columns):
                            self.__matrix[i][j] = round(self.__matrix[i][j] + other.getElement(i+1, j+1), 4)
                else:
                    raise TypeError('The other operand invalid. The other operand must be of type Matrix, int or float')
        

        def __radd__(self, other):
            '''Overload method for addition with another operand, which is on the left

            Argument must be Matrix or int or float

            Returns the result of adding a matrix to a number or another matrix. Type Matrix
            '''

            return self.__add__(other)


        def __iadd__(self, other):
            '''Overload method for addition with another operand, which is after "+="

            Argument must be Matrix or int or float

            Returns the result of adding a matrix to a number or another matrix. Type Matrix
            '''

            return self.__add__(other)


        def addWithNumber(self, other):
            '''Method for addition with a number

            Argument must be int or float
            '''

            if type(other) == float or type(other) == int:
                self.__add__(other, False)
            else:
                raise TypeError('The other operand invalid. The other operand must be of type int or float')


        def addWithMatrix(self, other):
            '''Method for addition with another matrix

            Argument must be Matrix
            '''

            if type(other) == Matrix:
                self.__add__(other, False)
            else:
                raise TypeError('The other operand invalid. The other operand must be of type Matrix')
            
#----------------------


#---Subtraction methods---

        def __sub__(self, other, needToReturn=True):
            '''Overload method for subtracting with another operand, which is on the right

            Argument must be Matrix or int or float

            Returns the result of subtracting a matrix to a number or another matrix. Type Matrix
            '''
            
            if needToReturn:
                if type(other) == int or type(other) == float:
                    newMatrix = Matrix(rows=self.__rows, columns=self.__columns)
                    for i in range(self.__rows):
                        for j in range(self.__columns):
                            newMatrix[i+1][j] = round(self.__matrix[i][j] - other, 4)
                    return newMatrix
                elif type(other) == Matrix and type(other[1]) == list and self.__rows == other.getNumberOfRows() and self.__columns == other.getNumberOfColumns():
                    newMatrix = Matrix(rows=self.__rows, columns=self.__columns)
                    for i in range(self.__rows):
                        for j in range(self.__columns):
                            newMatrix[i+1][j] = round(self.__matrix[i][j] - other.getElement(i+1, j+1), 4)
                    return newMatrix
                else:
                    raise TypeError('The other operand invalid. The other operand must be of type Matrix, int or float')
            else:
                if type(other) == int or type(other) == float:
                    for i in range(self.__rows):
                        for j in range(self.__columns):
                            self.__matrix[i][j] = round(self.__matrix[i][j] - other, 4)
                elif type(other) == Matrix and type(other[1]) == list and self.__rows == other.getNumberOfRows() and self.__columns == other.getNumberOfColumns():
                    for i in range(self.__rows):
                        for j in range(self.__columns):
                            self.__matrix[i][j] = round(self.__matrix[i][j] - other.getElement(i+1, j+1), 4)
                else:
                    raise TypeError('The other operand invalid. The other operand must be of type Matrix, int or float')


        def __rsub__(self, other):
            '''Overload method for subtracting with another operand, which is on the left

            Argument must be Matrix or int or float

            Returns the result of subtracting a matrix to a number or another matrix. Type Matrix
            '''

            return self.__sub__(other)


        def __isub__(self, other):
            '''Overload method for subtracting with another operand, which is after "-="

            Argument must be Matrix or int or float

            Returns the result of subtracting a matrix to a number or another matrix. Type Matrix
            '''

            return self.__sub__(other)


        def subWithNumber(self, other):
            '''Method for subtracting with a number

            Argument must be int or float
            '''

            if type(other) == float or type(other) == int:
                self.__sub__(other, False)
            else:
                raise TypeError('The other operand invalid. The other operand must be of type int or float')


        def subWithMatrix(self, other):
            '''Method for subtracting with another matrix

            Argument must be Matrix
            '''
            
            if type(other) == Matrix:
                self.__sub__(other, False)
            else:
                raise TypeError('The other operand invalid. The other operand must be of type Matrix')

#-------------------------


#---Multiplication methods---

        def __mul__(self, other, needToReturn=True):
            '''Overload method for multiplying with another operand, which is on the right

            Argument must be Matrix or int or float

            Returns the result of multiplying a matrix to a number or another matrix. Type Matrix
            '''

            if needToReturn:
                if type(other) == int or type(other) == float:
                    newMatrix = Matrix(rows=self.__rows, columns=self.__columns)
                    for i in range(self.__rows):
                        for j in range(self.__columns):
                            newMatrix[i+1][j] = round(self.__matrix[i][j] * other, 4)
                    return newMatrix
                elif type(other) == Matrix and type(other[1]) == list:
                    # Mnemonic rule
                    if self.__rows == other.getNumberOfColumns():
                        newMatrix = Matrix(rows=self.__rows, columns=other.getNumberOfColumns())
                        for i in range(self.__rows):
                            for j in range(other.getNumberOfColumns()):
                                element = 0
                                for k in range(self.__columns):
                                    element += self.__matrix[i][k] * other.getElement(k+1, j+1)
                                newMatrix[i+1][j] = round(element, 4)
                        return newMatrix
                    else: 
                        raise ValueError('You cannot multiply these matrices. Because the number of columns in the first matrix is not equal to the number of rows in the second matrix')
                else:
                    raise TypeError('The other operand invalid. The other operand must be of type Matrix, int or float')
            else:
                if type(other) == int or type(other) == float:
                    for i in range(self.__rows):
                        for j in range(self.__columns):
                            self.__matrix[i][j] = round(self.__matrix[i][j] * other, 4)
                elif type(other) == Matrix and type(other[1]) == list:
                    # Mnemonic rule
                    if self.__rows == other.getNumberOfColumns():
                        newMatrix = Matrix(rows=self.__rows, columns=other.getNumberOfColumns())
                        for i in range(self.__rows):
                            for j in range(other.getNumberOfColumns()):
                                element = 0
                                for k in range(self.__columns):
                                    element += self.__matrix[i][k] * other.getElement(k+1, j+1)
                                newMatrix[i+1][j] = round(element, 4)
                        self.__matrix = newMatrix.getMatrix()
                    else: 
                        raise ValueError('You cannot multiply these matrices. Because the number of columns in the first matrix is not equal to the number of rows in the second matrix')
                else:
                    raise TypeError('The other operand invalid. The other operand must be of type Matrix, int or float')


        def __rmul__(self, other):
            '''Overload method for multiplying with another operand, which is on the left

            Argument must be Matrix or int or float

            Returns the result of multiplying a matrix to a number or another matrix. Type Matrix
            '''

            return self.__mul__(other)


        def __imul__(self, other):
            '''Overload method for multiplying with another operand, which is after "*="

            Argument must be Matrix or int or float

            Returns the result of multiplying a matrix to a number or another matrix. Type Matrix
            '''

            return self.__mul__(other)


        def mulWithNumber(self, other):
            '''Method for multiplying with a number

            Argument must be int or float

            Returns the result of multiplying a matrix to a number. Type Matrix
            '''
            if type(other) == float or type(other) == int:
                self.__mul__(other, False)
            else:
                raise TypeError('The other operand invalid. The other operand must be of type int or float')


        def mulWithMatrix(self, other):
            '''Method for multiplying with another matrix

            Argument must be Matrix
            '''

            if type(other) == Matrix:
                self.__mul__(other, False)
            else:
                raise TypeError('The other operand invalid. The other operand must be of type Matrix')

#----------------------------


        def findDeterminant(self):
            '''Method for finding the determinant of a matrix

            Returns the determinant of a matrix. Type float or int
            '''

            if self.__rows == self.__columns:
                if self.__rows == 1:
                    return self.__matrix[0][0]
                elif self.__rows == 2:
                    return (self.__matrix[0][0] * self.__matrix[1][1] - self.__matrix[0][1] * self.__matrix[1][0])
                elif self.__rows >= 3:
                    tempMatrix = Matrix(rows=self.__rows - 1, columns=self.__columns - 1)
                    determinant = 0
                    for i in range(self.__columns):
                        a = 0
                        for j in range(1, self.__rows):
                            b = 0
                            for k in range(self.__columns):
                                if k != i:
                                    tempMatrix[a+1][b] = self.__matrix[j][k]
                                    b += 1
                            a += 1
                        determinant += (-1) ** (i + 2) * self.__matrix[0][i] * tempMatrix.findDeterminant()
                    return round(determinant, 4)
                else:
                    raise ValueError("Invalid matrix")
            else:
                raise ValueError("Invalid matrix. The matrix must be square")


        def findMinor(self, row, column):
            '''Method for finding the minor of a matrix

            Arguments mast be positive integers

            Returns the minor of a matrix with indexes row and column. Type float or int
            '''

            if type(row) == int and type(column) == int:
                if self.__rows >= 2:
                    if 0 < row <= self.__rows and 0 < column <= self.__columns:
                        row -= 1
                        column -= 1
                        newMatrix = Matrix(rows=self.__rows-1, columns=self.__columns-1)
                        a = 0
                        for i in range(self.__rows):
                            b = 0
                            if row != i:
                                for j in range(self.__columns):
                                    if column != j:
                                        newMatrix[a+1][b] = self.__matrix[i][j]
                                        b += 1
                                a += 1
                        return newMatrix.findDeterminant()
                    else:
                        raise IndexError('Invalid index. Row or column with such number does not exist')
                else:
                    raise TypeError('Invalid matrix. The dimension of the matrix must be greater than or equal to 2')
            else:
                raise TypeError('Invalid index. The row or column number should be a positive integer')          


        def findAlgebraicComplement(self, row, column):
            '''Method for finding the algebraic complement of a matrix
            
            Arguments must be positive integers

            Returns the algebraic complement of a matrix with indexes row and column. Type float or int
            '''

            return round(self.findMinor(row, column) * (-1) ** (row + column), 4)


        def makeTransposeMatrix(self):
            '''Method for making transpose matrix to the matrix'''

            newMatrix = Matrix(rows=self.__rows, columns=self.__columns)
            for i in range(1, self.__rows + 1):
                newMatrix.setRow(i, self.getColumn(i))
            self.__matrix = newMatrix.getMatrix()


        def makeAssociativeMatrix(self):
            '''Method for making associative matrix to the matrix'''

            newMatrix = Matrix(rows=self.__rows, columns=self.__columns)
            for i in range(self.__rows):
                for j in range(self.__columns):
                    newMatrix[j+1][i] = self.findAlgebraicComplement(i+1, j+1)
            self.__matrix = newMatrix.getMatrix()


        def makeInvertibleMatrix(self):
            '''Method for making invertible matrix to the matrix'''

            determinant = self.findDeterminant()
            if determinant != 0:
                newMatrix = Matrix(rows=self.__rows, columns=self.__columns)
                self.makeAssociativeMatrix()
                newMatrix = self * round(1 / determinant, 4)
                self.__matrix = newMatrix.getMatrix()
            else:
                raise ValueError('Invalid matrix. This matrix is ​​not invertible because its determinant is 0')
else:
    print("The module was run as an executable file")