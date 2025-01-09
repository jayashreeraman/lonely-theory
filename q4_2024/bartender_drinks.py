"""
At a popular bar, each customer has a set of favorite drinks, and will happily accept any drink among this set. 
For example, in the following situation, customer 0 will be satisfied with drinks 0, 1, 3, or 6.

preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}
A lazy bartender working at this bar is trying to reduce his effort by limiting the drink recipes 
he must memorize. Given a dictionary input such as the one above, return the fewest number of drinks 
he must learn in order to satisfy all customers.

For the input above, the answer would be 2, as drinks 1 and 5 will satisfy everyone.

"""


from configparser import MAX_INTERPOLATION_DEPTH


preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}



def minimize_drinks(drinks, remaining_drinks, remaining_customers, cust_by_drink):
    min_options = drinks

    if not remaining_customers:
        return drinks - remaining_drinks

    for drink in remaining_drinks:
        option = minimize_drinks(drinks, remaining_drinks - {drink},
                    remaining_customers-cust_by_drink[drink], cust_by_drink)
        
        if len(option) < len(min_options):
            min_options = option
    
    return min_options



def get_min_drinks(preferences):
    cust_by_drink = {}
    for key in preferences:
        for d in preferences[key]:
            if d not in cust_by_drink:
                cust_by_drink[d] = set()
            cust_by_drink[d].add(key)

    print(cust_by_drink)

    remaining_drinks = set(cust_by_drink.keys())
    #print(remaining_drinks)
    remaining_customers = set(preferences.keys())
    #print(remaining_customers)

    min_drinks = minimize_drinks(set(cust_by_drink.keys()), 
                                remaining_drinks=remaining_drinks, 
                                remaining_customers=remaining_customers, 
                                cust_by_drink=cust_by_drink)
    print(min_drinks)
    return len(min_drinks)


print(get_min_drinks(preferences))
