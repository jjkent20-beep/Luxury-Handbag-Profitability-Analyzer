print("==================================================")
print("     Luxury Handbag Profitability Analysis")
print("==================================================\n")
# ----------------------------------
# Luxury Handbag Profitability Analyzer
# Created by Jamie Kent
# ----------------------------------
# Scenario:
# This project analyzes the profitability of three luxury handbags
# using hypothetical financial assumptions inspired by luxury fashion
# brands. It compares revenue, costs, profit margins, and break-even
# points to determine which handbag performs the best.

print("\n================================================")
print("Bag Information")
print("==================================================")
# Neverfull MM
neverfull_price = 2030
neverfull_units_sold = 12000
print(f"Neverfull MM Price: ${neverfull_price:,.2f}")
print(f"Neverfull MM Units Sold: {neverfull_units_sold:,}")

# Speedy 25 
speedy_price = 1820
speedy_units_sold = 9500
print(f"\nSpeedy 25 Price: ${speedy_price:,.2f}")
print(f"Speedy 25 Units Sold: {speedy_units_sold:,}")

# Alma BB
alma_price = 2100
alma_units_sold = 7800
print(f"\nAlma BB Price: ${alma_price:,.2f}")
print(f"Alma BB Units Sold: {alma_units_sold:,}")

print("\n================================================")
print("Manufacturing Costs")
print("==================================================")
# Neverfull MM Cost
neverfull_cost = 520
# Speedy 25 Cost
speedy_cost = 470
# Alma BB Cost
alma_cost = 610

print(f"Neverfull MM Cost: ${neverfull_cost:,.2f}")
print(f"Speedy 25 Cost: ${speedy_cost:,.2f}")
print(f"Alma BB Cost: ${alma_cost:,.2f}")

print("\n================================================")
print("Revenue")
print("==================================================")
# Neverfull MM Revenue
neverfull_revenue = neverfull_price * neverfull_units_sold
print(f"Neverfull MM Revenue: ${neverfull_revenue:,.2f}")
# Speedy 25 Revenue
speedy_revenue = speedy_price * speedy_units_sold
print(f"Speedy 25 Revenue: ${speedy_revenue:,.2f}")
# Alma BB Revenue
alma_revenue = alma_price * alma_units_sold
print(f"Alma BB Revenue: ${alma_revenue:,.2f}")

print("\n================================================")
print("Gross Profit")
print("==================================================")
# Neverfull Gross Profit
neverfull_gross_profit = (neverfull_price - neverfull_cost) * neverfull_units_sold
print(f"Neverfull Gross Profit: ${neverfull_gross_profit:,.2f}")
# Speedy 25 Gross Profit
speedy_gross_profit = (speedy_price - speedy_cost) * speedy_units_sold
print(f"Speedy 25 Gross Profit: ${speedy_gross_profit:,.2f}")
# Alma BB Gross Profit
alma_gross_profit = (alma_price - alma_cost) * alma_units_sold
print(f"Alma Gross Profit: ${alma_gross_profit:,.2f}")

print("\n================================================")
print("Profit Margin")
print("==================================================")
# Neverfull Profit Margin
neverfull_profit_margin = (neverfull_gross_profit / neverfull_revenue) * 100
print("Neverfull Profit Margin: ", round(neverfull_profit_margin, 2), "%")
# Speedy 25 Profit Margin
speedy_profit_margin = (speedy_gross_profit / speedy_revenue) * 100
print("Speedy 25 Profit Margin: ", round(speedy_profit_margin, 2), "%")
# Alma BB Profit Margin
alma_profit_margin = (alma_gross_profit / alma_revenue) * 100
print("Alma BB Profit Margin: ", round(alma_profit_margin, 2), "%")

print("\n================================================")
print("Break-Even Analysis")
print("==================================================")
# Neverfull Break-Even Units
neverfull_break_even = neverfull_cost / (neverfull_price - neverfull_cost)
print("Neverfull MM Break-Even Units:", round(neverfull_break_even, 2))
# Speedy 25 Break-Even Units
speedy_break_even = speedy_cost / (speedy_price - speedy_cost)
print("Speedy 25 Break-Even Units:", round(speedy_break_even, 2))
# Alma BB Break-Even Units
alma_break_even = alma_cost / (alma_price - alma_cost)
print("Alma BB Break-Even Units:", round(alma_break_even, 2))

print("\n================================================")
print("Product Comparison")
print("==================================================")
# Revenue Comparison
revenues = {
    "Neverfull MM": neverfull_revenue,
    "Speedy 25": speedy_revenue,
    "Alma BB": alma_revenue
}
highest_revenue = max(revenues, key=revenues.get)
print("\nHighest Revenue:", highest_revenue)
# Gross Profit Comparison
gross_profits = {
    "Neverfull MM": neverfull_gross_profit,
    "Speedy 25": speedy_gross_profit,
    "Alma BB": alma_gross_profit
}
highest_gross_profit = max(gross_profits, key=gross_profits.get)
print("Highest Gross Profit:", highest_gross_profit)
# Profit Margin Comparison
profit_margin = {
    "Neverfull MM": neverfull_profit_margin,
    "Speedy 25": speedy_profit_margin,
    "Alma BB": alma_profit_margin
}
highest_profit_margin = max(profit_margin, key=profit_margin.get)
print("Highest Profit Margin:", highest_profit_margin)
# ----------------------------------