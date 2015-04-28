========================================================
RefinancingForm 	id			mortgageRefinancingForm
CalculatorText		id			calculator-text-head
MoneyRows			css			.money-row	
CatFish				css 		.stickybox
SummaryBox			css			.money-row.summary
========================================================


@desktop
RefinancingForm
    contains: CatFish, SummaryBox, CalculatorText

CalculatorText
    text is: Update the details below to calculate your repayments when you refinance your home loan.

CatFish
    width: 320px
    right of: MoneyRows 10px

Summary
    below: CalculatorText 10px


