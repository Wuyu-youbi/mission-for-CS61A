def make_withdraw_list(balance):
    b = [balance]
    def withdraw(amount):
        if amount > b[0]:
            return 'insufficient fund'
        b[0] -= amount
        return b[0]
    return withdraw
'''first try for mutable function, which can be used as bank system (maybe it can be used in game system)'''