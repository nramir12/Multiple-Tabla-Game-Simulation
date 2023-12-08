import random

random_draw_list = random.sample(range(1, 55), 54)


def create_tabla():
    #for loop? YES User input?
    made_tablas = []
    for t in range(100):
        tabla = []
        # pick 16 for tabla
        nums = random.sample(range(1, 55), 16)
        # fill tabla
        tabla.insert(0, nums[0:4])
        tabla.insert(1, nums[4:8])
        tabla.insert(2, nums[8:12])
        tabla.insert(3, nums[12:16])
        t += 1
        made_tablas.append(tabla)
    return made_tablas
    #print(all_tablas)

def check(made_tablas):
    all_tablas = []
    duplist = []
    for i in made_tablas:
        if i not in all_tablas:
            all_tablas.append(i)
        else:
            duplist.append(i)

    #print("List of Dups", duplist)
    #print("Unique Item List", all_tablas)

    if len(all_tablas) != 1:
        create_tabla()

    return all_tablas

ball_list = []


def call_ball():
    number_drawn = random_draw_list.pop()
    # print(number_drawn)

    ball_list.append(number_drawn)

    return number_drawn


def mark(all_tablas):
    # number_called = random.randint(19, 21)  # call a random number from 1-54 so 1-55
    # print(number_called)

    ball = call_ball()
    # print(ball)

    for q in all_tablas:  # check if list has number replace number with x
        for i in range(len(q)):
            for j in range(len(q)):
                if q[i][j] == ball:
                    q[i][j] = 'X'

    # print(*all_cards, sep='\n')


card_num = []
lot_type = []#delete


def check_win(all_tablas):
    win = False
    for q in all_tablas:
        # col
        if q[0][0] == 'X' and q[1][0] == 'X' and q[2][0] == 'X' and q[3][0] == 'X':
            win = True
            #print("WINNER col0")
            index = all_tablas.index(q)
            card_num.append(index + 1)
            type = 'Col0'
            lot_type.append(type)
            #print(q)
        elif q[0][1] == 'X' and q[1][1] == 'X' and q[2][1] == 'X' and q[3][1] == 'X':
            win = True
            #print("WINNER col1")
            index = all_tablas.index(q)
            card_num.append(index + 1)
            type = 'Col1'
            lot_type.append(type)
            #print(q)
        elif q[0][2] == 'X' and q[1][2] == 'X' and q[2][2] == 'X' and q[3][2] == 'X':
            win = True
            #print("WINNER col2")
            index = all_tablas.index(q)
            card_num.append(index + 1)
            type = 'Col2'
            lot_type.append(type)
            #print(q)
        elif q[0][3] == 'X' and q[1][3] == 'X' and q[2][3] == 'X' and q[3][3] == 'X':
            win = True
            #print("WINNER col3")
            index = all_tablas.index(q)
            card_num.append(index + 1)
            type = 'Col3'
            lot_type.append(type)
            #print(q)
        # row
        elif q[0][0] == 'X' and q[0][1] == 'X' and q[0][2] == 'X' and q[0][3] == 'X':
            win = True
            #print("WINNER row0")
            index = all_tablas.index(q)
            card_num.append(index + 1)
            type = 'Row0'
            lot_type.append(type)
            #print(q)
        elif q[1][0] == 'X' and q[1][1] == 'X' and q[1][2] == 'X' and q[1][3] == 'X':
            win = True
            #print("WINNER row1")
            index = all_tablas.index(q)
            card_num.append(index + 1)
            type = 'Row1'
            lot_type.append(type)
            #print(q)
        elif q[2][0] == 'X' and q[2][1] == 'X' and q[2][2] == 'X' and q[2][3] == 'X':
            win = True
            #print("WINNER row2")
            index = all_tablas.index(q)
            card_num.append(index + 1)
            type = 'Row2'
            lot_type.append(type)
            #print(q)
        elif q[3][0] == 'X' and q[3][1] == 'X' and q[3][2] == 'X' and q[3][3] == 'X':
            win = True
            #print("WINNER row3")
            index = all_tablas.index(q)
            card_num.append(index + 1)
            type = 'Row3'
            lot_type.append(type)
            #print(q)
        # diag
        elif q[0][0] == 'X' and q[1][1] == 'X' and q[2][2] == 'X' and q[3][3] == 'X':
            win = True
            #print("WINNER diag1")
            index = all_tablas.index(q)
            card_num.append(index + 1)
            type = 'diag1'
            lot_type.append(type)
            #print(q)
        elif q[0][3] == 'X' and q[1][2] == 'X' and q[2][1] == 'X' and q[3][0] == 'X':
            win = True
            #print("WINNER diag2")
            index = all_tablas.index(q)
            card_num.append(index + 1)
            type = 'diag2'
            lot_type.append(type)
            #print(q)
        # four corners
        elif q[0][0] == 'X' and q[3][0] == 'X' and q[0][3] == 'X' and q[3][3] == 'X':
            win = True
            #print("WINNER outside4")
            index = all_tablas.index(q)
            card_num.append(index + 1)
            type = 'outside4'
            lot_type.append(type)
            #print(q)
        elif q[1][1] == 'X' and q[1][2] == 'X' and q[2][1] == 'X' and q[2][2] == 'X':
            win = True
            #print("WINNER inside4")
            index = all_tablas.index(q)
            card_num.append(index + 1)
            type = 'inside4'
            lot_type.append(type)
            #print(q)
    return win


def game():
    # print("Let's play bingo!")
    cards = create_tabla()
    checkedcards = check(cards)
    # add start game please

    win = check_win(checkedcards)
    balls_till_win = 0

    while win == False:
        mark(cards)
        balls_till_win += 1

        win = check_win(checkedcards)

    if win == True:
        print(f"\nCard Winner: {card_num}")
        # print(len(card_num))
        #print(f"\nNumbers drawn: {ball_list}") #delete
        # print(len(ball_list))
        print(f"\nBINGO! Total balls to win: {balls_till_win}")
        #s = ' '.join(str(x) for x in card_num)
        # print(s)
        #t = ' '.join(str(y) for y in ball_list)#delete
        # print(t)
        u = ' '.join(str(x) for x in lot_type)#delete

        #cardfile = open('rem_cardwinner.txt', 'a')
        #ballfile = open('rem_balls_drawn.txt', 'a')#delete
        typefile = open('100tab_lot_type.txt', 'a')#delete
        #numfile = open('1tab_avgnum.txt', 'a')
        #cardfile.write(s + '\n')
        #ballfile.write(t + '\n')#delete
        typefile.write(u + '\n')#delete
        #numfile.write(str(balls_till_win) + '\n')
        #cardfile.close()
        #ballfile.close()#delete
        typefile.close()#delete
        #numfile.close()
        print("____________________________________________________________________")

    else:
        print("Goodbye! Thanks for playing")

    reset_game()


def reset_game():
    # print(random_draw_list)
    random_draw_list.extend(ball_list)
    # print(random_draw_list)
    random.shuffle(random_draw_list)
    # print(random_draw_list)

    ball_list.clear()
    card_num.clear()
    lot_type.clear()#delete

    number_drawn = random_draw_list.pop()  # removes last element of list
    # print(number_drawn)

    ball_list.append(number_drawn)


def main():
    for g in range(1000000):
        print(f"GAME: {g + 1}")
        game()


main()
