# for loop with no initialization
for _ in range(5): # loops from 0 to 4
    print("Good morning!") # prints 5 times.

# append vs += with list
score_list = [10, 20]
score_list.append(30)
score_list.append([40, 50])
score_list += [60, 70]
score_list.extend([80, 90])
print(score_list)
# [10, 20, 30, [40, 50], 60, 70, 80, 90]

# sum of all list items
days = [5, 10, 35, 19]
print(sum(days)) # 69

prices = [12.5, 19.3, 3.25]
print(sum(prices)) # 30.05

order_count = 0

# global variable
def place_order():
    global order_count # needed because editing the global variable
    order_count += 1
    print(f"so far {order_count} orders are placed!")

def show_orders():
    #global order_count is not required here
    # because we are just reading the global variable
    print(f"so far {order_count} orders are placed!")


place_order()
show_orders()

