import random

if __name__ == '__main__':
    print("Enter the number of friends joining (including you):")
    number = int(input())
    if number <= 0:
        print("No one is joining for the party")
    else:
        print("Enter the name of every friend (including you), each on a new line:")
        friends = {}
        for i in range(number):
            name = input()
            friends.update({name: 0})
        print("Enter the total bill value:")
        total_bill = int(input())
        splitted_total_bill = total_bill / number
        for key in friends:
            friends.update({key: round(splitted_total_bill, 2)})
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        answer = input()
        if answer == "Yes":
            random.seed(3)
            lucky = random.randint(0, number)
            friends_list = list(friends)
            lucky_name = friends_list[lucky]
            print("{} is the lucky one!".format(lucky_name))
            new_splitted_total_bill = total_bill / (number - 1)
            for key in friends:
                if key == lucky_name:
                    friends.update({key: 0})
                else:
                    friends.update({key: new_splitted_total_bill})
        else:
            print("No one is going to be lucky")
        print(friends)
