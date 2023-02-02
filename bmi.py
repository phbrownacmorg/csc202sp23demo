# Program to calculate BMI and classify it.

# Barack Obama: 6'2" (74"), 175 lbs. from a Google search on 'barack obama height weight'
# Donald Trump: 6'3" (75"), 243 lbs., same page as Pres. Obama
# Justin Bieber: 5'9" (69"), 154 lbs. https://starsunfolded.com/justin-bieber/
# Selena Gomez: 5'5" (65"), 130 lbs. https://celebhealthmagazine.com/selena-gomez-measurements/
# Dolly Parton: 5'0" (60"), 115 lbs. Google search on 'dolly parton height weight'
# Dawson Knox: 6'4" (76"), 254 lbs., Google search on 'dawson knox height weight'
# Ariana Grande: 5'0" (60"), 106 lbs. https://celebhealthmagazine.com/ariana-grande-measurements-size/
# Gigi Hadid: 5'11" (71"), 119 lbs. https://celebhealthmagazine.com/gigi-hadid-height-weight-age-body-statistics/

def classifyBMI(bmi: float) -> str:
    result: str = ''
    if bmi < 18.5:
        result = 'underweight'
    # No need to test the bottom end, because the "if" already did
    elif bmi < 25: # 18.5 <= bmi < 25
        result = 'normal'
    elif bmi < 30: # 25 <= bmi < 30
        result = 'overweight'
    else: # bmi >= 30
        result = 'obese'
    return result

def findBMI(height: float, weight: float) -> float:
    # Formula from https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html
    return (weight / (height**2)) * 703

def main(args: list[str]) -> int:
    height: float = float(input("Please enter a person's height in inches: "))
    weight: float = float(input("Please enter the person's weight in pounds: "))

    bmi: float = findBMI(height, weight)
    print("This person's BMI is {:.1f}.".format(bmi))
    print('This BMI is considered {}.'.format(classifyBMI(bmi)))

    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)