import requests
from bs4 import BeautifulSoup



sudoku_page = requests.get("http://west.websudoku.com/")
soup = BeautifulSoup(sudoku_page.content, 'html.parser')

print(soup)
board = [[0 for element in range(9)] for row in range(9)] # pravi matricu nula

for i in range(9):
    for j in range(9):
        cell_id = f"f{i}{j}"
        cell = soup.find("input", id=cell_id)
        if cell and "readonly" in cell.attrs:
            board[i][j] = int(cell["value"])
        else:
            board[i][j] = 0

print(board)
