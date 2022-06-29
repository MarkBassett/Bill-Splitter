import random
class BillSplitter:
    def __init__(self):
        self.number_of_friends = 0
        self.friends = {}
        self.amount = 0

    def add_friends(self):
        print('Enter the name of every friend (including you), each on a new line:')
        for friend in range(self.number_of_friends):
            name = input()
            self.friends[name] = 0

    def split_bill(self, n=0):
        bill = round(self.amount / (self.number_of_friends - n), 2)
        for friend in self.friends:
            self.friends[friend] = bill

    def lucky_one(self, lucky):
        print()
        if lucky == 'yes':
            lucky_friend = random.choice(list(self.friends.keys()))
            print(f'{lucky_friend} is the lucky one!')
            self.split_bill(1)
            self.friends[lucky_friend] = 0
        else:
            print('No one is going to be lucky')




bill_splitter = BillSplitter()
print('Enter the number of friends joining (including you):')
friends = int(input())
print()
if friends <= 0:
    print('No one is joining for the party')
else:
    bill_splitter.number_of_friends = friends
    bill_splitter.add_friends()
    print()
    bill_splitter.amount = int(input('Enter the total bill value:'))
    print()
    bill_splitter.split_bill()
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    bill_splitter.lucky_one(input().lower())
    print(bill_splitter.friends)