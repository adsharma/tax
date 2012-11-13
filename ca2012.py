""" 
https://www.ftb.ca.gov/forms/2012_California_Tax_Rates_and_Exemptions.shtml
Includes prop 30. Includes 1% mental health tax for income > 1mm.
"""

tax = {
"single" : 
           [ [0, 7455, 17676, 27897, 38726, 48942, 250000, 30000, 500000, 1000000],
             [1, 2, 4, 6, 8, 9.3, 10.3, 11.3, 12.3, 13.3 ]
           ],

"married filing jointly" : 
           [ [ 0, 14910, 35352, 55794, 77452, 97884, 500e3, 600e3, 1e6],
             [ 1, 2, 4, 6, 8, 9.3, 10.3, 11.3, 13.3 ]
           ],
}
