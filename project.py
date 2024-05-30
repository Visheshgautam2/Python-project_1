def ConstBoard(board):
    print("Current Status of Board:\n\n");
    for i in range(0,9):
        if ((i>0) and (i%3==0)):
            print("\n");
        if (board[i]==0):
            print("_", end=" ");
        if (board[i]==-1):
            print("X", end=" ");
        if (board[i]==1):
            print("O", end=" ");
    print("\n\n");

def User1turn(board):
    pos = int(input("Enter the postion from [1,2,3,...,9]:"));
    if board[pos-1] != 0:
        print("Wrong Move");
        exit(0);
    board[pos-1]=-1;

def User2turn(board):
    pos = int(input("Enter the postion from [1,2,3,...,9]:"));
    if board[pos-1] != 0:
        print("Wrong Move");
        exit(0);
    board[pos-1]= 1;

def minmax(board, Player):
    x= anlyzeboard(board);
    if x!=0:
        return (x*Player);
    pos = -1;
    value = -2;
    for i in range(0,9):
        if board[i]==0:
            board[i]=Player;
            score=-minmax(board, Player*-1);
            board[i] = 0;
            if score>value:
                value=score;
                pos=i;            
    if(pos==-1):
        return 0;
    return value;


def Compturn(board):
    pos = -1;
    value = -2;
    for i in range(0,9):
        if board[i]==0:
            board[i]=1;
            score=-minmax(board, -1);
            board[i] = 0;
            if score>value:
                value=score;
                pos=i;            
    board[pos]=1
 
def anlyzeboard(board):
    cb = [[0,1,2] , [3,4,5] , [6,7,8] , [0,3,6] , [1,4,7] , [2,5,8] , [0,4,8] , [2,4,6]];

    for i in range(0,8):
        if ( board[ cb[i][0]]!=0 and
             board[cb[i][0]]==board[cb[i][1]]and
             board[cb[i][0]]==board[cb[i][2]]):
             return board[cb[i][0]];

    return 0;



def main():
    choice = int(input("Enter 1 for Single Player, 2 for Multiplayer: "));
    board=[0,0,0,0,0,0,0,0,0]
    if choice == 1:
        print ("Computer: O Vs You: X");
        Player = int(input("Enter to play 1(st) or 2(nd)"));
        for i in range(0,9):
            if(anlyzeboard(board) != 0):
                break;
            if ((i+Player)%2 == 0):
                Compturn(board);
            else:
                ConstBoard(board);
                User1turn(board);
    else:
        print ("Computer: O Vs You: X");
        Player = int(input("Enter to play 1(st) or 2(nd)"));
        for i in range(0,9):
            if(anlyzeboard(board) != 0):
                break;
            if ((i+Player)%2 == 0):
                User2turn(board);
            else:
                ConstBoard(board);
                User1turn(board);
    

    x = anlyzeboard(board);
    if (x==0):
        ConstBoard(board);
        print("Draw");
    if (x==-1):
        ConstBoard(board);
        print("Player X has won!!!! O Looses!");
    if (x==1):
        ConstBoard(board);
        print("Player O has won!!!! X Looses!");


main()