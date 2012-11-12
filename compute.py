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
        if (income < income_table[i]):
            break
        tax += (income_table[i] - income_table[i-1]) * tax_rate_table[i-1]/100
        #print i, income_table[i], tax_rate_table[i], tax
    tax += (income - income_table[i-1]) * tax_rate_table[i-1]/100
    return tax

def compute(user, income):
    ca_tax = table(ca2012.tax, income)
    fed_tax = table(fed2012.tax, income - ca_tax)
    #print fed_tax, ca_tax
    return fed_tax + ca_tax
       
if __name__ == '__main__':
    user = user.User()
    user.status = 'married filing jointly'

    intervals = range(10000,100000, 10000) + \
                range(100000, 500000, 25000) + \
                range(500000, 1600000, 100000)

    print "%-7s\t%-7s\t%-6s" % ("Income", "Tax", "Effective Rate")
    for income in intervals:
        tax = compute(user, income)
        print "%07d\t%07d\t%3.2d" % (income, tax, tax * 100/income)
