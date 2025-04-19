from auction_ascii_art import logo

def get_user_bid():
    name = input("What is your name? ")
    bid = float(input("What is your bid? "))
    bids[name] = bid

def show_highest_bidder():
    max_bid = 0.0
    bidder = ""
    for name in bids:
        if max_bid < bids[name]:
            max_bid = bids[name]
            bidder = name
    print(f"The winner of silent bid is {bidder} with amount {max_bid}")

def start_bidding():
    print(logo)
    print("Welcome to the secret auction program!")
    end_bidding = False

    while not end_bidding:
        get_user_bid()
        end_bidding = input("Are there any other bidders? type 'yes' or 'no': ").lower() == "no"
        if end_bidding is False:
            print("\n"*20) # print 20 empty lines
    show_highest_bidder()

bids = {}
start_bidding()


