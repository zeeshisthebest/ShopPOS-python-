from generatereceipt import GenerateReceipt as gR


def main():
    invoice_number = 12345
    receipt = gR(invoice_number)

    # Customer info
    customer = input("Enter the name of customer: ")
    cell_number = input("Cell Number (11-digits): ")
    # Checking phone number
    while True:

        if cell_number == "":
            break
        elif (not cell_number.isnumeric()) or (len(cell_number) != 11):
            print("The phone number is not valid!: ")
            cell_number = input("Enter Again: ")
        else:
            break

    receipt.set_customer_name(customer, cell_number)
    # /Customer

    #   Item info.
    items_list_to_pass = []
    total = 0
    while True:
        item = input("Enter chemical and unit price(separated by space). -1 to exit: ")

        if item == "-1":
            break

        item = item.rsplit(sep=" ", maxsplit=1)

        unit_price = float(item[1])

        chem = item[0].rstrip()

        while True:
            try:
                quantity = float(input("Enter the Quantity: "))
                break
            except ValueError:
                print("You didn't enter the valid quantity: please enter again")
                continue

        item_total = unit_price * quantity
        item_row = [chem, unit_price, quantity]
        total += item_total
        items_list_to_pass.append(item_row)

    receipt.print_list(items_list_to_pass)
    receipt.print_to_pdf()


if __name__ == '__main__':
    main()
