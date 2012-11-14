"""
http://www.fivecentnickel.com/2011/09/28/2012-federal-income-tax-brackets-irs-tax-rates/
"""

tax = {
"single" : 
           [ [0, 8700, 35350, 85650, 178650, 388350],
             [10, 15, 25, 28, 33, 35]
           ],

"married filing jointly" : 
           [ [ 0, 17400, 70700, 142700, 217450, 388350 ],
             [10, 15, 25, 28, 33, 35]
           ],
}

# includes exemption
std_deduction = {
    "single" : 9750,  # 5950 + 3800 (exemption)
    "married filing jointly" : 19500 # 11900 +  2 * 3800 (exemption)
}

social_sec_max = 110100
social_sec_rate = 4.2
medicare_rate = 1.45
