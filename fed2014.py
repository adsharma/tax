"""
Update me. Copy of 2013 tables right now.
"""

tax = {
"single" : 
           [ [0, 8925, 36250, 87850, 183250, 398350, 400000 ],
             [10, 15, 25, 28, 33, 35, 39.6]
           ],

"married filing jointly" : 
           [ [ 0, 17850, 72500, 146400, 223050, 398350, 450000 ],
             [10, 15, 25, 28, 33, 35, 39.6 ]
           ],
}

std_deduction = {
    "single" : 6100,
    "married filing jointly" : 12200
}

exemption = {
    "single" : 3900,
    "married filing jointly" : 3900 * 2
}

social_sec_max = 113700
social_sec_rate = 6.2
medicare_rate = 1.45
