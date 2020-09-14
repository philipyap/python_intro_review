In [1]: philip_y = "philip"

In [2]: print(philip_y)
philip

In [3]: age = 5

In [4]: print(age)
5

In [5]: isCool = True

In [6]: notCool = False

In [7]: print(isCool)
True

In [8]: print(notCool)
False

In [9]: this_is_none = None

In [10]: print(this_is_none)
None

In [11]: True and False
Out[11]: False

In [12]: True or False
Out[12]: True

In [13]: True > False
Out[13]: True

In [14]: True < False
Out[14]: False

In [15]: True and "0"
Out[15]: '0'

In [16]: True and 0
Out[16]: 0

In [17]: 2 ** 3
Out[17]: 8

In [18]: 2 ** 4
Out[18]: 16

In [19]: 2 / 2
Out[19]: 1.0

In [20]: 2 + 2
Out[20]: 4

In [25]: philip_yap = "philip yap"

In [26]: philip_yap
Out[26]: 'philip yap'

In [27]: philip_yap.split(' ')
Out[27]: ['philip', 'yap']

In [28]: philip_yap.index('p')
Out[28]: 0

In [29]: philip_yap.index('y')
Out[29]: 7

In [30]: philip_yap.upper()
Out[30]: 'PHILIP YAP'

In [31]: philip_yap.lower()
Out[31]: 'philip yap'

In [33]: philip_yap.replace('philip', 'phil')
Out[33]: 'phil yap'

In [34]: ace_of_spades = "Ace of Spades"

In [36]: "of" in ace_of_spades
Out[36]: True

In [37]: "spades" in ace_of_spades
Out[37]: False

In [38]: "Spades" in ace_of_spades
Out[38]: True

In [39]: len(ace_of_spades)
Out[39]: 13

In [40]: ace_of_spades[2]
Out[40]: 'e'

In [41]: ace_of_spades[-1]
Out[41]: 's'

In [42]: ace_of_spades[0]
Out[42]: 'A'

In [43]: ace_of_spades[-8]
Out[43]: 'f'

In [44]: ace_of_spades[-0]
Out[44]: 'A'

In [45]: ace_of_spades[1:4]
Out[45]: 'ce '

In [46]: ace_of_spades[:2]
Out[46]: 'Ac'

In [47]: ace_of_spades[2:]
Out[47]: 'e of Spades'

In [48]: ace_of_spades[5:]
Out[48]: 'f Spades'

In [49]: ace_of_spades[::-3]
Out[49]: 'sa  A'

In [50]: ace_of_spades[::-1]
Out[50]: 'sedapS fo ecA'

In [51]: 19%5
Out[51]: 4

In [52]: not False
Out[52]: True

In [53]: not True
Out[53]: False

In [54]: not True and not 1
Out[54]: False

In [55]: True and 1
Out[55]: 1

In [56]: not 1 and True
Out[56]: False

In [57]: not True and not 1
Out[57]: False

In [58]: not 1 and True
Out[58]: False

In [59]: not 1 or True
Out[59]: True

In [60]: 1 == 1
Out[60]: True

In [61]: 1 != 0
Out[61]: True

In [62]: nba_teams = ["Lakers", "Nuggets", "Celtics"]

In [63]: len(nba_teams)
Out[63]: 3

In [64]: nba_teams.append('Clippers')

In [65]: nba_teams
Out[65]: ['Lakers', 'Nuggets', 'Celtics', 'Clippers']

In [66]: len(nba_teams)
Out[66]: 4

In [68]: arr_of_numbers = [1] * 3

In [69]: arr_of_numbers
Out[69]: [1, 1, 1]

In [70]: nba_teams[0]
Out[70]: 'Lakers'

In [71]: nba_teams[3]
Out[71]: 'Clippers'

In [73]: nba_teams[-1]
Out[73]: 'Clippers'

In [74]: nba_teams[-2]
Out[74]: 'Celtics'

In [75]: nba_teams[-3]
Out[75]: 'Nuggets'

In [76]: nba_teams[-4]
Out[76]: 'Lakers'

In [77]: one_through_ten = list(range(10))

In [78]: one_through_ten
Out[78]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [79]: random_numbers = [9,6,4,2,3,5,8,1]

In [80]: random_numbers
Out[80]: [9, 6, 4, 2, 3, 5, 8, 1]

In [81]: random_numbers.sort()

In [82]: random_numbers
Out[82]: [1, 2, 3, 4, 5, 6, 8, 9]

In [83]: random_numbers[::-1]
Out[83]: [9, 8, 6, 5, 4, 3, 2, 1]

In [84]: random_numbers
Out[84]: [1, 2, 3, 4, 5, 6, 8, 9]

In [85]: random_numbers.pop()
Out[85]: 9

In [86]: random_numbers
Out[86]: [1, 2, 3, 4, 5, 6, 8]

In [88]: random_numbers.pop(6)
Out[88]: 8

In [89]: random_numbers
Out[89]: [1, 2, 3, 4, 5, 6]

In [90]: random_numbers.pop(0)
Out[90]: 1

In [91]: random_numbers
Out[91]: [2, 3, 4, 5, 6]

In [92]: print(random_numbers)
[2, 3, 4, 5, 6]

In [95]: dog = {
    ...: "name": "King",
    ...: "age": "3",
    ...: "location": "Los Angeles"
    ...: }

In [96]: dog["name"]
Out[96]: 'King'

In [97]: dog["age"]
Out[97]: '3'

In [98]: dog["sleep_alot"] = True

In [99]: dog
Out[99]: {'name': 'King', 'age': '3', 'location': 'Los Angeles', 'sleep_alot': True}

In [100]: int("5")
Out[100]: 5

In [101]: str(5)
Out[101]: '5'

In [102]: float(99)
Out[102]: 99.0

In [103]: bool("philip")
Out[103]: True

In [104]: bool(0)
Out[104]: False

In [105]: bool("0")
Out[105]: True

In [106]: my_message = f"{dog['name']}lives in {dog['location']}."

In [107]: my_message
Out[107]: 'Kinglives in Los Angeles.'

In [108]: my_message = f"{dog['name']} lives in {dog['location']}."

In [109]:

In [109]: my_message
Out[109]: 'King lives in Los Angeles.'

In [110]: print(my_message)
King lives in Los Angeles.

In [112]: anohter_message = f"I predict the {nba_teams[0]} to win it all."
In [114]: anohter_message
Out[114]: 'I predict the Lakers to win it all.'
In [116]: "I predict the {} to win it all".format(nba_teams[0])
Out[116]: 'I predict the Lakers to win it all'

In [117]: "I predict the {} and {} to win it all".format(nba_teams[0], nba_teams
     ...: [3])
Out[117]: 'I predict the Lakers and Clippers to win it all'

In [118]: def add_numbers(num1, num2):
     ...:     result = num1 + num2
     ...:     return result
In [120]: add_numbers(5,5)
Out[120]: 10

In [121]: def print_this():
     ...:     print("Hello, my name is ...")
     ...:

In [122]: print_this()
Hello, my name is ...    

In [124]: def legal_age(age):
     ...:     if(age<21):
     ...:         return "sorry you are too you"
     ...:     elif(age== 21) :
     ...:         return "you made it."
     ...:     else:
     ...:         return "you are free to pass"
     ...:

In [125]: legal_age(30)
Out[125]: 'you are free to pass'
In [127]: legal_age(21)
Out[127]: 'you made it.'

In [128]: legal_age(20)
Out[128]: 'sorry you are too you'

In [129]: vip = True

In [130]: food_place = "busy"
In [132]: def the_spot(vip, food_place, location = "bay area"):
     ...:     if(food_place == "full" and not vip):
     ...:         print("sorry, no room at {} location".format(location))
     ...:     elif(food_place == "busy" and not vip):
     ...:         print("please wait 30 mins for table at {} location".format(lo
     ...: cation))
     ...:     else:
     ...:         print("welcome")
     ...:

In [133]: the_spot(vip, food_place)
welcome
In [135]: the_spot(False, food_place)
please wait 30 mins for table at bay area location

In [136]: the_spot(False, food_place, "san frnacisco")
please wait 30 mins for table at san frnacisco location

In [137]: number = 0

In [138]: while number < 10:
     ...:     number +=1
     ...:

In [139]: number = 1

In [140]:

In [140]: print(number)
1

In [141]: while number < 10:
     ...:     print(number)
     ...:     number +=1
     ...:
1
2
3
4
5
6
7
8
9

In [142]: for i in range(0,15):
     ...:     print(i)
     ...:
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14

In [143]: for i in range(len(nba_teams)):
     ...:     each_team = nba_teams[i]
     ...:     print(each_team)
     ...:
Lakers
Nuggets
Celtics
Clippers

In [144]: teams = ("Patriots", "Dolphins", "Falcons")

In [145]: teams
Out[145]: ('Patriots', 'Dolphins', 'Falcons')

In [146]: teams[0]
Out[146]: 'Patriots'
In [148]: new_england, miami, atlanta = teams

In [149]: teams
Out[149]: ('Patriots', 'Dolphins', 'Falcons')

In [150]: new_england
Out[150]: 'Patriots'

In [151]: miami
Out[151]: 'Dolphins'

In [152]: atlanta
Out[152]: 'Falcons'

In [153]: sales_tax = (0.13, 0.12, 0.11)

In [154]: california, illinois, alabama = sales_tax

In [155]: california
Out[155]: 0.13