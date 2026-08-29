#Greet the user
print("Hello! Welcome to the compound interest calculator.")
#Obtain inputs:
    #Obtain the investment price/P 
investment_p = float(input("Please enter initial investment amount of your investment: "))
    #Obtain the interest rate/r 
rate_r = float(input("Please enter the interest rate (e.g., '0.03' for 3% interest): "))
    #Obtain the period of time in years/t 
time_t = int(input("Please enter the number of years for the investment: "))
    #Obtain the frequency of compounding/n
frequency_n = int(input("Please enter the number of compounding periods per year: "))
#Display Original investment
print(f"Your original investment was: ${investment_p:,.2f}")
#Calculate total value of account currently
new_balance = (investment_p*(1+(rate_r/frequency_n))**(frequency_n*time_t))
#Calculate interest earned (P'-P)
interest_earned = new_balance - investment_p
#Display original investment
print(f"Original Investment: ${investment_p:,.2f}")    
#Display interest earned
print(f"Interest Earned: ${interest_earned:,.2f}")
#Display total value of account
print(f"Final Balance: ${new_balance:,.2f}")
#prompt if user wants to compare savings parameters with another set
inquiry = input("Would you like to compare this to another savings option? (Y/N): ")
#If yes, continue with repeated questions to find new set of parameters
if inquiry == "Y" or inquiry == "y" or inquiry == "Yes" or inquiry == "yes":
    investment_p2 = float(input("Please enter the initial amount of your investment: "))
    rate_r2 = float(input("Please enter the interest rate (e.g., '0.03' for 3% interest): "))
    time_t2 = int(input("Please enter the number of years for the investment: "))
    frequency_n2 = int(input("Please enter the number of compounding periods per year: "))
    #calculate interest earned and total value
    new_balance2 = (investment_p2*(1+(rate_r2/frequency_n2))**(frequency_n2*time_t2))
    interest_earned2 = new_balance2 - investment_p2
    #display original, interest, and total current value from new hypothetical
    print(f"Original Investment: ${investment_p2:,.2f}")
    print(f"Interest Earned: ${interest_earned2:,.2f}")
    print(f"Final Balance: ${new_balance2:,.2f}")
    #Inform the user which set of parameters has the highest yield or if neither does
    if interest_earned == interest_earned2:
        print("Both scenarios have the same yield.")
    elif interest_earned > interest_earned2:
        print(f"The first option will result in the largest final account balance by ${interest_earned - interest_earned2:,.2f}.")
    else:
        print(f"The second option will result in the largest final account balance by ${interest_earned2 - interest_earned:,.2f}.")
    #Prompt end message
    print("Thank you for using the compound interest calculator. I hope you have found the calculations that you needed.")
#If the user wishes to leave:
elif inquiry == "N" or inquiry == "n" or inquiry == "No" or inquiry == "no":
    print("Thank you for using the compound interest calculator. I hope you have found the calculations that you needed.")
#Further instructions for invalid input:
else:
    print("Invalid input. Please reset the program and enter 'Y' for yes or 'N' for no.")