# Monthly Sales Tax

SALES_TAX_PERCENT = 0.05
COUNTY_SALES_TAX_PERCENT = 0.025

def main():
    total_sales_monthly = get_monthly_sales()

    sales_tax = tax_sales(total_sales_monthly)
    county_sales_tax = tax_county_sales(total_sales_monthly)

    total_tax = tax_total(sales_tax, county_sales_tax)

    print('The sales tax is $', format(sales_tax, ',.2f'), sep = '')
    print('The county sales tax is $', format(county_sales_tax, ',.2f'), sep = '')
    print('The total tax is $', format(total_tax, ',.2f'), sep = '')

def get_monthly_sales():
    monthly_sales = float(input("Enter the monthly sales: "))

    while monthly_sales < 0:
        print("ERROR!, monthly sales cannot be negative.")
        monthly_sales = float(input("Enter the monthly sales: "))
    
    return monthly_sales

def tax_sales(monthly_sales):
    return monthly_sales * SALES_TAX_PERCENT

def tax_county_sales(monthly_sales):
    return monthly_sales * COUNTY_SALES_TAX_PERCENT

def tax_total(sales_tax, county_sales_tax):
    return sales_tax + county_sales_tax

main()
