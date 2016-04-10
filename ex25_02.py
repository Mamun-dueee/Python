def break_w(ws):
    words = ws.split(' ')
    return words

def sort(ws):
    return sorted(ws)

def print_first(ws):
    word = ws.pop(0)
    print word
    
def print_last(ws):
    word = ws.pop(-1)
    print word