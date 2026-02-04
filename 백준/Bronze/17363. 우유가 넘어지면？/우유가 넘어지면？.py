input = open(0).readline

offset = {
    "." : ".",
    "O" : "O",
    "-" : "|",
    "|" : "-",
    "/" : "\\",
    "\\" : "/",
    "^" : "<",
    "<" : "v",
    "v" : ">",
    ">" : "^"
}

row, col = map(int, input().split())

data = [input().strip() for _ in range(row)]

for y in range(col):
    for x in range(row):
        print(offset[data[x][col-y-1]], end="")
    print()