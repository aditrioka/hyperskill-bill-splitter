# write your code here
import random


def bill_splitter():
    num_of_friends = int(input('Enter the number of friends joining (including you): '))

    if num_of_friends > 0:
        dict_of_friends = dict()
        list_of_friends = []
        print('Enter the name of every friend (including you), each on a new line:')

        for i in range(0, num_of_friends):
            name_of_friend = input()
            dict_of_friends[name_of_friend] = 0
            list_of_friends.append(name_of_friend)

        print('Enter to total bill value:')
        total_bill = int(input())

        bill_each_friend = round(total_bill / len(dict_of_friends), 2)

        for friend in dict_of_friends:
            dict_of_friends[friend] = bill_each_friend

        is_who_is_lucky_enabled = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')

        if is_who_is_lucky_enabled == "Yes":
            lucky_index = random.randint(0, num_of_friends-1)
            lucky_one = list_of_friends[lucky_index]

            print(lucky_one, 'is the lucky one!')

            bill_each_friend = round(total_bill / (len(dict_of_friends)-1), 2)

            for item in dict_of_friends:
                if item == lucky_one:
                    dict_of_friends[item] = 0
                else:
                    dict_of_friends[item] = bill_each_friend

            print(dict_of_friends)
        else:
            print('No one is going to be lucky')
            print(dict_of_friends)
    else:
        print('No one is joining for the party')

bill_splitter()

