# Assignment 2: Compound Interest

> [!IMPORTANT]
> This assignment is to be completed individually. It is not a team project.  You must document (using comments in your code) all resources (beyond our official textbook, Canvas, the class discussion forum, or the class website) that you used to help you complete this assignment. For example, if you referenced a code example from an online website such as Stackoverflow or github you could acknowledge it as follows: 
>
> ```
> # Next we print 'Hello, World' to the console.
> # Based on help from: https://stackoverflow.com/questions/826948/syntax-error-on-print-with-python-3
> print("Hello, world!")
> ```
>
> You must provide an attribution to any resource you consulted to complete this assignment except for our official textbook, Canvas, the class discussion forum, or the class website. Resources that require attribution include — but are not limited to — AI tools (even those built in to VS Code), websites, books, notes from other students, tutors, or help from other people (friends, classmates, etc.). Under no circumstances are you to look at or copy any material related to another person's solution for this assignment.
>
> To repeat, you must attribute any resource you consulted to complete this assignment other than our official textbook, Canvas, class discussion forum, or the class website. You must cite all AI technologies you used, if any, to complete this assignment. Failure to provide attribution is a violation of the honor code.

## Overview

Compound interest is an important financial concept that motivates saving early and often in your lifetime. Assuming no withdrawals from a savings account, the interest earned on your savings in one time period becomes part of the account balance and earns interest in future time periods. Therefore, even without any additional principal, an account earning compound interest will earn more and more interest in each subsequent year.

For a specific investment, we can calculate the amount of money in the account as: $P'=P(1+\frac{r}{n})^{nt}$

where:

* $P$ is the initial amount, commonly called the principal
* $r$ is the interest rate (e.g., 0.03 for 3%)
* $n$ is the number of compounding periods per year (e.g., 12 for monthly, 4 for quarterly, 1 for annually)
* $t$ is the number of years of interest
* $P'$ is the new balance for the account after earning interest for $t$ years

For this assignment, you'll need to write a program that gathers some of these variables from the user, calculates some figures using the above equation, and displays the results.

## Basic Requirements

> [!NOTE]
> Satisfying only the basic requirements perfectly, with no points deducted for any reason, would earn a maximum score of 8 out of 10 for this assignment.

You need to write a program that acts as a savings calculator. It should:

* Prompt the user to enter $P$, $r$, $n$, and $t$. Your prompts should be "user friendly" and should NOT require a user to know what, for example, $n$ represents. The prompts should make it obvious what the user should enter and what units are expected.
* Display the original principal ($P$), the amount of interest earned ($P'-P$), and the total value of the account at the end of the term ($P'$).
* Format all monetary values displayed with units (i.e. dollar signs), commas, and two decimal places. For example: $20,023.23.

The output produced by your program should be nearly identical to the sample output provided below. While the user's input will vary from run to run, the prompts and messages printed to the console when using your program should match those in the sample output to receive full credit.

## Advanced Requirements

> [!NOTE]
> Satisfying both the basic and advanced requirements perfectly, with no points deducted for any reason, will result in a full 10 out of 10 score for this assignment.

You need to write a program that acts as a savings calculator and comparison tool. In addition to performing the basic requirements outlined above, your program should provide the user with an option to enter an additional set of savings parameters ($P$, $r$, $n$, and $t$). For each of the two sets of savings parameters, you should display the results as outlined in the basic requirements. In addition, your program should say which of the options would result in the largest final value (largest $P'$). More specifically, your program should:

* Perform the basic requirements.
* Provide the user with an option to compare the first set of savings parameters they have entered with a second set of parameters.
* If the user declines, the program should end. If the user chooses to make a comparison, ask the user to enter a second set of parameters ($P$, $r$, $n$, and $t$) and display the same information as in the basic requirements (with the same formatting requirements: units, commas, and two decimal places).
* Finally, if the user has entered more than one set of parameters, tell the user which set of parameters produces the largest final account balance $P'$.
## Sample Output

An example of the output produced by my solution to this assignment can be found below:
```
Welcome to the Compound Interest Calculator.
Please enter the initial amount of your investment: 25000
Please enter the interest rate (e.g., '.03' for 3% interest): .04
Please enter the number of years for the investment: 10
Please enter the number of compounding periods per year: 12
Original Investment: $25,000.00
Interest Earned:     $12,270.82
Final Balance:       $37,270.82

Would you like to compare this to another savings option? (Y/N) Y
Please enter the initial amount of your investment: 25000
Please enter the interest rate (e.g., '.03' for 3% interest): .03
Please enter the number of years for the investment: 15
Please enter the number of compounding periods per year: 12
Original Investment: $25,000.00
Interest Earned:     $14,185.79
Final Balance:       $39,185.79

The second option will result in the largest final account balance.
```

## Grading Criteria

This assignment will be graded on a 10 point scale. Your grade for this assignment will be based on a combination of factors, including:

* Correct functionality (e.g., Does your Python code do what it is supposed to do as outlined in the basic and/or advanced requirements?)
* Clarity of your solution (e.g., Did you solve the problem directly and efficiently? Or is your answer excessively complex and/or inefficient?)
* Coding style (e.g., Is your code readable with comments, meaningful variable names, and good whitespace/indentation?)
* Meets submission requirements (see below)

## Seeking Help

For general questions about Python, please use the class forum on Piazza to seek assistance. For questions that are personal in nature or that would reveal a solution to the assignment, you ask for help by email or during office hours. However, please note that emailed questions will not receive an immediate response. It is likely that it will take 24-48 hours for me to respond.

## Submitting Your Solution

When you have completed your work on the assignment, it is time to submit your solution via Canvas.  You can submit your assignment by taking the following steps:
1. Be sure that all of your changes have been pushed to your GitHub repository for the assignment.
2. Go to the web page for your repository on github.com
3. Click the green button labeled "< > Code &#9660;" which should open a popup menu.
4. From the popup menu, click on "Download ZIP" which will download a zip file containing your entire project to your computer. 
5. Submit the zip file you just downloaded via Canvas as your solution for this assignment.


> [!WARNING]
> NOTE FOR MAC USERS: Mac users who use the Safari browser will notice that the browser will, by default, automatically unzip and delete zip files you download from the internet. To change this behavior, press and hold the Option key when clicking the "Download ZIP" menu item.  This will prevent Safari from automatically unzipping and deleting the Zip file. Instead, it will just download the Zip file as it is just as you would get on any other browser.  Only Safari users need to take this extra step.


## Due Date

The due date for this assignment can be found in the official class schedule and on Canvas.

