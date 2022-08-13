# Matrix

Designed for creating and processing matrices.
*The subtleties of the operation of individual functions can be found in the comments to them.*

This is my old course project, so the module will not be updated (uploaded just for my github).

**Author: VadimKarch (JustCircle).**

                The matrix class is based on the standard list. 
                
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
                
                others:
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
