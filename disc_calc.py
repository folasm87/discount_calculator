import sys

def calc_discount(total, discount, discount_type):
    if (discount_type == "dollar"):
        return total - discount
    elif (discount_type == "percent"):
        return total - (total * (discount/100))
def main(argv = sys.argv):
    try:
        total = float(raw_input("Total in shopping cart ($): "))
        discount = float(raw_input("Discount in shopping cart ($ or %): "))
        discount_type = raw_input("What type of discount. Please type 'dollar' or 'percent': ").lower()
    except ValueError:
        print "Sorry, you have to provide a number for the shopping cart total and discount and then indicate what type of discount by entering 'dollar' or 'percent'"
        total = float(raw_input("Total in shopping cart ($): "))
        discount = float(raw_input("Discount in shopping cart ($ or %): "))
        discount_type = raw_input("What type of discount. Please type 'dollar' or 'percent': ").lower()
        
    final_discount = calc_discount(total, discount, discount_type)
    print "The final discount of ${0:.2f} is ${1:.2f}".format(total, final_discount)
    
if __name__ == '__main__':  
   main()