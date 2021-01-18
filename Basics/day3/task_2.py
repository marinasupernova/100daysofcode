nachos_friends = ['athletic', 'not athletic','older', 'athletic', 
'younger', 'athletic', 'not athletic', 
'older', 'athletic', 'older',
'athletic']

hula_hoops_by_swings = 0
hula_hoops_by_basketball_court = 0




for i in range(len(nachos_friends)):
    nachos_friend = nachos_friends[i]
    if nachos_friend == 'athletic' or nachos_friend == 'younger':
        hula_hoops_by_swings = hula_hoops_by_swings +1
    if nachos_friend == 'not athletic' or nachos_friend == 'older':
        hula_hoops_by_basketball_court = hula_hoops_by_basketball_court+1


print(hula_hoops_by_basketball_court)
