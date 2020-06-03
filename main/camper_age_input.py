
#Program: camper_age_input
#Author: Terry Pope
#Last date modified: 06/03/2020

#The purpose of this program is to accept input of age and convert it to months,
#then output the results.

def convert_to_months(years):
    return years*12

if __name__ == '__main__':
    years = (int(input("Enter age between 1 and 5:")))
    convert_to_months(years)
    ageInMonths = convert_to_months(int(years))
    print(years, "years is",ageInMonths, "months." )

