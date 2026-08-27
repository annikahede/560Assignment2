#Greet the user
print("Hello! Welcome to the investment calculator.")
print("input the following to get started on calculating your investment earnings: ")
#Obtain inputs:
    #Obtain the investment price/P 
investment_p = int(input("Enter initial investment amount: "))
    #Obtain the interest rate/r 
percentage_r = int(input("Enter the annual interest rate as whole number (e.g., 4% would be entered as 4): "))
rate_r = percentage_r / 100
    #Obtain the frequency of compounding/n 
frequency_n = int(input("Enter the amount that the interest is compounded per year: "))
    #Obtain the period of time in years/t 
time_t = int(input("Enter the number of years: "))
#Display Original investment
print(f"Your original investment was: ${investment_p:,.2f}")
#Calculate total value of account currently
new_balance = (investment_p*(1+(rate_r/frequency_n))**(frequency_n*time_t))
#Calculate interest earned (P'-P)
interest_earned = new_balance - investment_p
#Display interest earned
print(f"Interest earned over {time_t} years: ${interest_earned:,.2f}")
#Display total value of account
print(f"Total value of account after {time_t} years: ${new_balance:,.2f}")
#prompt if user wants to compare savings parameters with another set
inquiry = input("Would you like to compare this data with another possible scenario? (Y/N): ")
#If yes, continue with repeated questions for new set of parameters
if inquiry == "Y" or inquiry == "y" or inquiry == "Yes" or inquiry == "yes":
    print("Please enter the investment information for the second scenario: ")
    investment_p2 = int(input("Enter initial investment amount: "))
    percentage_r2 = int(input("Enter the annual interest rate as whole number (e.g., 4% would be entered as 4): "))
    rate_r2 = percentage_r2 / 100
    frequency_n2 = int(input("Enter the amount that the interest is compounded per year: "))
    time_t2 = int(input("Enter the number of years: "))
    #calculate and interest earned and total value
    new_balance2 = (investment_p2*(1+(rate_r2/frequency_n2))**(frequency_n2*time_t2))
    interest_earned2 = new_balance2 - investment_p2
    #calculate and display interest and total value from hypothetical
    print(f"Interest earned over {time_t2} years: ${interest_earned2:,.2f}")
    print(f"Total value of account after {time_t2} years: ${new_balance2:,.2f}")
    #Inform the user which set of parameters has the highest yield or if neither does
    if interest_earned == interest_earned2:
        print("Both scenarios have the same yield.")
    elif interest_earned > interest_earned2:
        print(f"The first scenario has the highest yield by ${interest_earned - interest_earned2:,.2f}.")
    else:
        print(f"The second scenario has the highest yield by ${interest_earned2 - interest_earned:,.2f}.")
    #Prompt end message
    print("Thank you for using the investment calculator. I hope you have found the calculations that you needed. If not, come back soon!")
#If the user wishes to leave:
elif inquiry == "N" or inquiry == "n" or inquiry == "No" or inquiry == "no":
    print("I hope you have found the calculations that you needed. If not, come back soon!")
#Further instructions for invalid input:
else:
    print("Invalid input. Please reset the program andenter 'Y' for yes or 'N' for no.")