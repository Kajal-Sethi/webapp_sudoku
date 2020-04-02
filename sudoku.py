from flask import Flask, render_template,request
app=Flask(__name__)

def FindUnassignedLocation(grid,l):
    for row in range(0,9):
        for col in range(0,9):
            if grid[row][col]==0:
                l[0]=row
                l[1]=col
                return (True)
    return(False)

def InRow(grid,row,num):
    for i in range(9):
        if grid[row][i]==num:
            return(True)
    return(False)

def InCol(grid,col,num):
    for j in range(9):
        if grid[j][col]==num:
            return(True)
    return(False)

def InBox(grid,startrow,startcol,num):
    for i in range(3):
        for j in range(3):
            if grid[startrow+i][startcol+j]==num:
                return(True)
    return(False)

def IsSafe(grid,row,col,num):
    return not InRow(grid,row,num) and not InCol(grid,col,num) and not InBox(grid,row-row%3,col-col%3,num)

def solve_sudoku(grid):
    l=[0,0]
    if not FindUnassignedLocation(grid,l):
        return (True)

    row=l[0]
    col=l[1]
    for num in range(1,10):
        if IsSafe(grid,row,col,num):
            grid[row][col]=num

            if solve_sudoku(grid):
                return(True)
            grid[row][col]=0
    return(False)



@app.route("/")
def index():
    return render_template('first.html')

@app.route("/result",methods=['POST','GET'])
def result():
    if request.method=='POST':
        grid_o=request.form
        grid=[[0 for i in range(9)]for j in range(9)]
        count=0;
        for i in range(0,9):
            for j in range(0,9):
                grid[i][j]=int(grid_o['cell-'+str(count)])
                count+=1
        solve_sudoku(grid)
        print(grid)

        return render_template('result.html',grid=grid)

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)
