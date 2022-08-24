transactions = []
balances = {}
max_transaction = ('X', 'Y', float('-Inf'))

def transfer(sender, receiver, amount):
    global max_transaction
    if amount > max_transaction[2]:
        max_transaction = (sender, receiver, amount)
    transactions.append((sender, receiver, amount))
    if not sender in balances:
        balances[sender] = 0
    if not receiver in balances:
        balances[receiver] = 0
    balances[sender] -= amount
    balances[receiver] += amount

def get_balance(user):
    return balances[user]

transfer('Alice', 'Bob', 2000)
transfer('Bob', 'Carl', 4000)
transfer('Alice', 'Carl', 2000)

print('Balance Alice: ' + str(get_balance('Alice')))
print('Balance Bob: ' + str(get_balance('Bob')))
print('Balance Carl: ' + str(get_balance('Carl')))

print('Max Transaction: ' + str(max_transaction))

transfer('Alice', 'Bob', 1000)
transfer('Carl', 'Alice', 8000)

print('Balance Alice: ' + str(get_balance('Alice')))
print('Balance Bob: ' + str(get_balance('Bob')))
print('Balance Carl: ' + str(get_balance('Carl')))

print('Max Transaction: ' + str(max_transaction))