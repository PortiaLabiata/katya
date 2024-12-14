def make_exchange(money, coins):
    if coins == [] or money < 0:
        return 0
    if money == 0:
        return 1
    return make_exchange(money, coins[1:]) + make_exchange(money - coins[0], coins)
