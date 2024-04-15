from cell import Cell
from world import World
from life import Life


'''def test1():
    print('----Cell Tests----')
    c1 = Cell(1,3)
    print(c1)
    assert c1.get_living() == False
    assert c1.__str__() == Cell.deadChar
    c1.set_living(True)
    assert c1.get_living() == True
    assert c1.__str__() == Cell.liveChar
    assert c1._Cell__neighbors == []

def test2():
    print('----World Tests----')

    w1 = World(3,4)
    print(w1)
    assert w1.__str__() == '....\n....\n....\n'
    w1.set_cell(0,0,True)
    w1.set_cell(0,3,True)
    w1.set_cell(2,0,True)
    w1.set_cell(2,3,True)
    print(w1)
    assert w1.__str__() == 'X..X\n....\nX..X\n'
    assert w1._World__rows == 3
    assert w1._World__columns == 4

def test3():
    """This is a visual test, because I didn't have time to automate it."""
    print('----Neighbors Test----')
    w1 = World(3,4)
    w1.set_cell(0,1,True)
    w1.set_cell(1,1,True)
    w1.set_cell(2,1,True)
    print(w1)

    w1._World__grid[0][0].debug()
    w1._World__grid[1][0].debug()
    w1._World__grid[2][2].debug()

def test4():

    print('----Next Generation Tests----')
    w1 = World(3,4)
    print(w1)
    w1.set_cell(0,1,True)
    w1.set_cell(1,1,True)
    w1.set_cell(2,1,True)
    print(w1)
    assert w1.__str__() == '.X..\n.X..\n.X..\n'
    w1.next_generation()
    print(w1)
    assert w1.__str__() == '....\nXXX.\n....\n'
    w1.next_generation()
    print(w1)
    assert w1.__str__() == '.X..\n.X..\n.X..\n'
    w1.next_generation()
    print(w1)
    assert w1.__str__() == '....\nXXX.\n....\n'

def test5():

    print('---Randomize Test---')
    w1 = World(40, 30)
    print(w1)
    w1.randomize()
    print(w1)
    for generation in range(10):
        print(f'{generation}')
        print(w1)
        w1.next_generation()'''



if __name__ == '__main__':
    '''test1() #Cell
    test2() #World
    test3() #Neighbors
    test4() #Next Generation
    test5() #Randomize'''

life = Life()
life.main()