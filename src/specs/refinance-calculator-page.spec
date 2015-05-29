========================================================
RefinancingForm 	id			mortgageRefinancingForm
CalculatorText		id			calculator-text-head
MoneyRows			css			.money-row	
CatFish				css 		.stickybox
AffordabilityButton	id			check-affordability-button
SummaryBox			css			.money-row.summary

LoanRepayment		id 			current_loan_repayments-currency
LoanTenure			id 			remaining_loan_term
NewLoanAmount 		id 			new_loan_amount-currency
NewLoanTenure		id 			new_loan_term
NewInterestRate		id 			new_interest_rate
========================================================


@desktop
RefinancingForm
    contains: CatFish, SummaryBox, CalculatorText

CalculatorText
    text is: Update the details below to calculate your repayments when you refinance your home loan.

CatFish
    width: 320px
    contains: AffordabilityButton

AffordabilityButton
    centered horizontally inside: CatFish

SummaryBox
    below: CalculatorText 527px

NewLoanTenure
    aligned vertically left: LoanTenure


