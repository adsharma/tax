#!/usr/bin/env python

import fed2012
import ca2012
import user

def table(tax_table, income):
    the_table = tax_table[user.status]
    tax = 0
    income_table = the_table[0]
    tax_rate_table = the_table[1]
    for i in range(1, len(income_table)):
        if (income <= income_table[i]):
            break
        tax += (income_table[i] - income_table[i-1]) * tax_rate_table[i-1]/100
        #print ">>", i, income_table[i], tax_rate_table[i-1], tax

    if (income > income_table[i]):
        tax += (income - income_table[i]) * tax_rate_table[i]/100
    else:
        tax += (income - income_table[i-1]) * tax_rate_table[i-1]/100
    #print ">>>", i, income, tax
    return tax

def compute_amt(income):
    """TBD"""
    return 0

def compute_normal(income):
    ca_tax = table(ca2012.tax, income)
    std_deduction = fed2012.std_deduction[user.status]
    social_sec_tax = min(fed2012.social_sec_max, income) * fed2012.social_sec_rate/100
    medicare_tax = income * fed2012.medicare_rate/100
    income = income - std_deduction - ca_tax
    income = max(income, 0)
    fed_tax = table(fed2012.tax, income)
    #print fed_tax, ca_tax
    return fed_tax + ca_tax + social_sec_tax + medicare_tax

def compute(income):
    return max(compute_normal(income), compute_amt(income))
       
if __name__ == '__main__':
    user = user.User()
    user.status = 'married filing jointly'
    #user.status = 'single'

    intervals = range(10000,100000, 10000) + \
                range(100000, 500000, 25000) + \
                range(500000, 2600000, 100000) + \
                range(1000000, 10000000, 1000000)

    print "%-7s\t%-7s\t%-6s" % ("Income", "Tax", "Effective Rate")
    for income in intervals:
        tax = compute(income)
        print "%07d\t%07d\t%3.2f" % (income, tax, tax * 100.0/income)
