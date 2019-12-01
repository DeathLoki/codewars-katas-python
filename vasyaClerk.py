people = [25, 25, 50]

""" Function to sell tickets to every single person in this line 

Keyword arguments:
register : hold the values to be checked
ans      : return the Answer
money    : the amount each person has 
change   : amount of money to be returned to the person buying the tickets 

"""

def tickets(people):
    register = []  # list to hold the money 
    ans = 'YES'
    for money in people:
        change = money - 25 
        register.append(0)
        if change == 0:
            register.append(money)
        elif change == 25:
            if 25 in register:
                register.append(money)
                register.remove(25)  
            else:
                ans = 'NO'
                break
        elif change == 50:
            if 50 in register:
                register.append(money)
                register.remove(50)
            else:
                ans = 'NO'
            break
        elif change == 75:
            if (25 in register and 50 in register):    
                register.append(money)
                register.remove(25)
                register.remove(50)
            elif register.count(25) == 3:
                register.append(money)
                for i in range(3):
                    register.remove(25)
            else:
                ans = 'NO'
                break
    return ans

                
       