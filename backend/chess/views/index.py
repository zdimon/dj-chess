from django.shortcuts import render
from django.conf import settings
import os
import json

def set_board(board):
    cnt = 0
    for line in board:

        if cnt == 0:
            board[cnt][0]["figure"] = "rook-white"
            board[cnt][1]["figure"] = "knite-white"
            board[cnt][2]["figure"] = "bishop-white"
            board[cnt][3]["figure"] = "queen-white"
            board[cnt][4]["figure"] = "king-white"
            board[cnt][5]["figure"] = "bishop-white"
            board[cnt][6]["figure"] = "knite-white"
            board[cnt][7]["figure"] = "rook-white"
        
        if cnt == 1:
            for index, value in enumerate(line):
                board[cnt][index]["figure"] = "pone-white"

        if cnt == 6:
            for index, value in enumerate(line):
                board[cnt][index]["figure"] = "pone-black"

        if cnt == 7:
            board[cnt][0]["figure"] = "rook-black"
            board[cnt][1]["figure"] = "knite-black"
            board[cnt][2]["figure"] = "bishop-black"
            board[cnt][3]["figure"] = "queen-black"
            board[cnt][4]["figure"] = "king-black"
            board[cnt][5]["figure"] = "bishop-black"
            board[cnt][6]["figure"] = "knite-black"
            board[cnt][7]["figure"] = "rook-black"

        cnt += 1
    return board


def make_board(x,y):
    board = []
    for x_item in range(0,x):
        tmp = [*range(0,y)]
        tmp_objs = []
        for t in tmp:
            if x_item%2 == 0:
                if t%2 == 0 :
                    cell_obj = {"color": "bg-black"}
                else:
                    cell_obj = {"color": "bg-white"}
            else:
                if t%2 == 0 :
                    cell_obj = {"color": "bg-white"}
                else:
                    cell_obj = {"color": "bg-black"}
            cell_obj["pos_x"] = t
            cell_obj["pos_y"] = x_item
            tmp_objs.append(cell_obj)
        board.append(tmp_objs)
    
    return board

DB_PATH = os.path.join(settings.BASE_DIR,'static','db.json')

def read_db():
    with open(DB_PATH, 'r') as f:
        return json.loads(f.read())

def write_db(board):
    with open(DB_PATH, 'w') as f:
        return f.write(json.dumps(board))

def create_board_db():
    if not os.path.isfile(DB_PATH):
        board = make_board(8,8)
        board = set_board(board)
        write_db(board)
    else:
        board = read_db()
    return board

def move_figure(from_x=0,from_y=0,to_x=1,to_y=1):
    board = read_db()
    figure = board[from_y][from_x]["figure"]
    board[from_y][from_x]["figure"] = None;
    board[to_y][to_x]["figure"] = figure;
    write_db(board)
    return board

from django.http import HttpResponse
from django.template.loader import render_to_string


def index(request): 
    board = create_board_db()
    tpl = render_to_string('index.html', {"board": board})
    tpl = tpl.replace('src="/static','src="/static/build/static')
    tpl = tpl.replace('href="/static','href="/static/build/static')
    tpl = tpl.replace('href="/manifest.json"','href="/static/build/manifest.json"')
    
    
    return HttpResponse(tpl)