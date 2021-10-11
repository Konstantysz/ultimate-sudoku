from src.Cell import Cell
import numpy as np
from src.GameConsts import BOARDFILEPATH

class BoardController:
    # default constructor
    def __init__(self, boardSize):
        print("Board {}x{} created!".format(boardSize.value, boardSize.value))

        self._horizontalNumbers = np.zeros((boardSize.value, boardSize.value), dtype=int)
        self._verticalNumbers = np.zeros((boardSize.value, boardSize.value), dtype=int)

        self._board = np.array([
            [Cell(True), Cell(True), Cell(True), Cell(True), Cell(True)], 
            [Cell(False), Cell(False), Cell(False), Cell(False), Cell(False)], 
            [Cell(True), Cell(True), Cell(True), Cell(True), Cell(True)], 
            [Cell(False), Cell(False), Cell(False), Cell(False), Cell(False)], 
            [Cell(True), Cell(True), Cell(True), Cell(True), Cell(True)]
        ])

    def import_board_image(self):
        # Bogdan algorithm to import image from BOARDFILEPATH
        return

    def calculate_info_numbers(self):
        return
