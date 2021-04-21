from django.shortcuts import render

def make_board(x,y):
    board = []
    for x_item in range(0,x):
        tmp = [*range(0,y)]
        tmp_objs = []
        for t in tmp:
            if x_item%2 == 0:
                if t%2 == 0 :
                    tmp_objs.append({"color": "bg-black"})
                else:
                    tmp_objs.append({"color": "bg-white"})
            else:
                if t%2 == 0 :
                    tmp_objs.append({"color": "bg-white"})
                else:
                    tmp_objs.append({"color": "bg-black"})
        board.append(tmp_objs)
    return board


def index(request): 
    board = None
    if request.method  == 'POST':
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        board = make_board(x,y)
        print(board)
    return render(request, 'index.html', {"board": board})