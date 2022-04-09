decision_Sam = input()
decision_Bob = input()

if decision_Sam == 'betrayal' and decision_Bob == 'betrayal':
    print('2 2')
elif decision_Sam == 'betrayal' or decision_Bob == 'silence':
    print('3 0')
elif decision_Sam == 'silence' or decision_Bob == 'betrayal':
    print('0 3')
elif decision_Sam == 'silence' and decision_Bob == 'silence':
    print('1 1')

'''
#Alternative Solution

decision_Sam = input()
decision_Bob = input()

if decision_Sam == 'silence'
    if decision_Bob == 'betrayal'
        print('3 0')
    elif decision_Bob == 'silence'
        print('1 1')

if decision_Bob == 'betrayal'
    if decision_Sam == 'silence'
        print('0 3')
    elif decision_Bob == 'betrayal'
        print('2 2')
'''