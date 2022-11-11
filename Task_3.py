# Создайте программу для игры в ""Крестики-нолики"".


game = list(range(1,10))

def draw_board(board):

 for i in range(3):
     print ("|", game[0+i*3], "|", game[1+i*3], "|",game[2+i*3], "|")

def stavim_hod(b):
 valid = False
 while not valid:
     t = input("Введите номер клетки куда поставить значение " + b+"? ")
     otv = int(t)
     if otv >= 1 and otv <= 9:
         if (str(game[otv-1]) not in "XO"):
             game[otv-1] = b
             valid = True
         else:
             print ("Эта клетка занята")
def kto_viigral(k):
 pobeda = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
 for x in pobeda:
     if k[x[0]] == k[x[1]] == k[x[2]]:
         return k[x[0]]
 return False

def igra(d):
 count = 0
 win = False
 while not win:
     draw_board(d)
     if count % 2 == 0:
         stavim_hod("X")
     else:
         stavim_hod("O")
     count += 1
     if count > 4:
         m = kto_viigral(d)
         if m:
             print (m, "Победил!")
             win = True
             break
     if count == 9:
         print ("Ничья!")
         break
 draw_board(d)

igra(game)