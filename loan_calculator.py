def calculate_loan_payment(principal, interest_rate,
                           term_years):
    monthly_rate = interest_rate / 100 / 12

    term_months = term_years * 12

    if monthly_rate == 0:
        monthly_payment = principal / term_months
    else:
        monthly_payment = principal * \
        (monthly_rate * (1 + monthly_rate) ** term_months) / \
        ((1+monthly_rate) ** term_months - 1)
    
    total_payment = monthly_payment * term_months
    total_interest = total_payment - principal

    return monthly_payment, total_payment, total_interest

def get_valid_input(i, input_type, validation_func=None):
    while True:
        try:
            value = input_type(input(i))

            if validation_func and not validation_func(value):
                print("Error: Invalid Input.")
                continue
            return value
        except ValueError:
            print(f"Error: Please enter a valid \
                  {input_type.__name__}")
        except KeyboardInterrupt:
            print("\n Calculator stopped.")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

def is_positive(value):
    return value > 0

def main():
    print("\n----- Simple Loan Calculator -----\n")

    try:
        principal = get_valid_input("Loan amount (INR. ): ",
                                    float, is_positive)
        interest_rate = get_valid_input("Annual Interest "\
        "rate (%): ", float, is_positive)
        term_years = get_valid_input("Loan tern (years): ",
                                     int, is_positive)
        
        # loan calculation
        monthly_payment, total_payment, total_interest = \
        calculate_loan_payment(principal, interest_rate,
                               term_years)
        
        # results display
        print("\n----- Loan Summary -----")
        print(f"Loan amount: INR. {principal:,.2f}")
        print(f"Interest rate: {interest_rate:.2f}%")
        print(f"Loan term: {term_years} years " \
              f"({term_years * 12} months)")
        print(f"\nMonthly payment: " \
              f"INR. {monthly_payment:,.2f}")
        print(f"Total payment: INR. {total_payment:,.2f}")
        print(f"Total interest paid: " \
              f"INR. {total_interest:,.2f}")
    
    except KeyboardInterrupt:
        print("\nCalculator stopped.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()