

# prices of groceries
book = dict()

book['apple'] =  0.67
book['milk'] = 1.49
book['avocado'] = 1.49

print(book)
if book.get('xx') == '':
    print('true')
    print('=======')


##  散列表，防止重复

voted = {}
def check_voter(name):
    if voted.get(name):
        print('kick them out')
    else:
        print('let them vote!')
        voted[name]= True


check_voter('tom')
check_voter('mike')
check_voter('mike')
print(voted)