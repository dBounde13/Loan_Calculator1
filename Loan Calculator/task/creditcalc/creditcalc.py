import argparse
import math
import sys

parser = argparse.ArgumentParser()

parser.add_argument('--type', type=str)
parser.add_argument('--principal', type=float)
parser.add_argument('--payment', type=float)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)

args = parser.parse_args()

principal = args.principal
payment = args.payment
periods = args.periods
interest = args.interest
type = args.type

if len(sys.argv) < 4:
    print("Incorrect parameters")

elif type != "annuity" and type != "diff":
    print("Incorrect parameters")

elif type == "diff" and payment is not None:
    print("Incorrect parameters")

elif interest is None:
    print("Incorrect parameters")

elif type == "annuity":

    if periods is None:

        nominal_interest_rate = interest / (12 * 100)

        periods = round(math.log((payment / (payment - (nominal_interest_rate * principal))),
                     (1 + nominal_interest_rate)) + 0.5)

        years = periods // 12

        months = periods % 12

        if years == 1 and months == 0:
            print("You need " + str(years) + " year to repay this credit!")
        elif years > 1 and months == 0:
            print("You need " + str(years) + " years to repay this credit!")
        elif years == 0 and months == 1:
            print("You need " + str(months) + " month to repay this credit!")
        elif years == 0 and months > 1:
            print("You need " + str(months) + " months to repay this credit!")
        elif years == 1 and months == 1:
            print("You need " + str(years) + " year and " + str(months) + " month to repay this credit!")
        elif years == 1 and months > 1:
            print("You need " + str(years) + " year and " + str(months) + " months to repay this credit!")
        elif years > 1 and months == 1:
            print("You need " + str(years) + " years and " + str(months) + " month to repay this credit!")
        elif years > 1 and months > 1:
            print("You need " + str(years) + " years and " + str(months) + " months to repay this credit!")

    elif payment is None:

        nominal_interest_rate = interest / (12 * 100)
        payment = round(principal * ((
                nominal_interest_rate * math.pow((1 + nominal_interest_rate), periods) / (
                math.pow((1 + nominal_interest_rate), periods) - 1))) + 0.5)
        print("Your annuity payment = " + str(payment) + "!")

    elif principal is None:

        nominal_interest_rate = interest / (12 * 100)
        principal = round(payment / (
                (nominal_interest_rate * math.pow((1 + nominal_interest_rate), periods)) / (
                math.pow((1 + nominal_interest_rate), periods) - 1)))
        print("Your credit principal = " + str(principal) + "!")

    total = periods * payment

    print("Overpayment = " + str(round(total - principal)))

elif type == "diff":

    nominal_interest_rate = interest / (12 * 100)

    total = 0

    for m in range(1, int(periods) + 1):
        diff_payment = round((principal / periods) + nominal_interest_rate * (
                principal - ((principal * (m - 1)) / periods)) + 0.5)
        print("Month " + str(m) + ": paid out " + str(diff_payment))
        total += diff_payment

    print("Overpayment = " + str(round(total - principal)))
