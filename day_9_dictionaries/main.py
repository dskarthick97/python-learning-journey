logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the secret auction program!")

secret_auction = list()
def add_bider(name, bid):
    bidders_info = dict()
    bidders_info["name"] = name
    bidders_info["bid"] = bid
    secret_auction.append(bidders_info)


is_proceed = True
while is_proceed:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    add_bider(name, bid)

    any_bidder = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if any_bidder == 'no':
        is_proceed = False


def get_winner(bidder_list):
    highest_bid = 0
    winner = ""

    for lst in bidder_list:
        bid_value = lst["bid"]
        if bid_value > highest_bid:
            highest_bid = bid_value
            winner = lst['name']

    return f'The winner is {winner} with a bid of ${highest_bid}'


print(get_winner(secret_auction))
