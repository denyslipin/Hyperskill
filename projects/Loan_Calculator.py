import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--payment", type=float)
parser.add_argument("--interest", type=float)
args = parser.parse_args()

if args.type is None or (args.type != "annuity" and args.type != "diff") \
                     or len(vars(args)) < 4 \
                     or (args.type == "diff" and args.payment) \
                     or (args.interest is None or args.interest < 0):
    print("Incorrect parameters")
else:
    i = float(args.interest) / 1200
    if args.type == "annuity":
        if args.payment is None:
            principal = float(args.principal)
            periods = int(args.periods)
            payment = math.ceil(principal * ((i * pow(1 + i, periods))
                      / (pow(1 + i, periods) - 1)))
            print(f"Your monthly payment = {math.ceil(payment)}!")
            print(f"Overpayment = {int(payment * periods - principal)}")
        elif args.principal is None:
            payment = float(args.payment)
            periods = int(args.periods)
            principal = math.floor(payment * pow((i * pow(1 + i, periods))
                        / (pow(1 + i, periods) - 1), -1))
            print(f"Your loan principal = {principal}!")
            print(f"Overpayment = {int(payment * periods - principal)}")
        elif args.periods is None:
            principal = float(args.principal)
            payment = float(args.payment)
            periods = math.log(payment / (payment - i * principal), 1 + i)
            if math.ceil(periods) % 12 == 0:
                year = int(math.ceil(periods) / 12)
                print(f"It will take {year} years to repay this loan!")
            elif periods < 12:
                months = int(math.ceil(periods))
                print(f"It will take {months} months to repay this loan!")
            else:
                year = int(periods // 12)
                months = int(math.ceil(periods % 12))
                print(f"It will take {year} years \
                        and {months} months to repay this loan!")
            print(f"Overpayment = \
                   {int(payment * int(math.ceil(periods)) - principal)}")
    elif args.type == "diff" and args.payment is None:
        principal = float(args.principal)
        periods = int(args.periods)
        month = 0
        payments = list()
        while month < periods:
            month += 1
            payment = math.ceil(principal / periods + i
                      * (principal - principal * (month - 1) / periods))
            payments.append(payment)
            print(f"Month {month}: payment is {payment}")
        print(f"Overpayment = {int(sum(payments) - principal)}")
