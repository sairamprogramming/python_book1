# Stock Transaction Program

# Stock purchase section

BROKER_COMMISION = 0.03

number_shares_purchased = 2000
each_stock_cost = 40.00

total_cost_price = number_shares_purchased * each_stock_cost
purchase_commision = total_cost_price * BROKER_COMMISION

# Stock sell section

number_shares_sold = 2000
each_stock_sold = 42.75

total_sell_price = number_shares_sold * each_stock_sold
sell_commision = total_sell_price * BROKER_COMMISION

# Display of all values and check if profit or loss

total_transaction = total_sell_price - total_cost_price - sell_commision - purchase_commision

print("Total stock cost:", format(total_cost_price, ',.2f'))
print("Purchase Commision:", format(total_sell_price, ',.2f'))
print("Total stock sold:", format(total_sell_price, ',.2f'))
print("Selling Commision:", format(sell_commision, ',.2f'))
print("Total Transaction:", format(total_transaction, ',.2f'))