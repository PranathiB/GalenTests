===============================================================
Body				        css			body
Adbanner			        css			.ad-leaderboard iframe
RepaymentForm				id			mortgageRepaymentForm
CalculatorText				id			calculator-text-head
CalculatorBox				css			.money-row
MoneyRow-item-*				css			.money-section-text
AmountBox					css			.input-group
Slider-item-*				css			.noUi-base
AffordabilityButton			id			check-affordability-button
Catfish				        css			.stickybox
Footer						css			.summary-footer.visible-xs
Summary						css			.money-row.summary

================================================================



@desktop
------------------------
Adbanner
   visible
   above: RepaymentForm

RepaymentForm
    contains: CalculatorText, CalculatorBox, Catfish, Summary
    #centered horizontally inside: Body
    #centered vertically inside: Body


CalculatorText
    text is: Update the details below to calculate your home loan repayments.
    above: CalculatorBox


CalculatorBox
    above: Summary
    contains: MoneyRow-item-*, Slider-item-*, AmountBox

[ 1- 2 ]
MoneyRow-item-@
    aligned vertically left: MoneyRow-item-@{+1}

Slider-item-1
    below: AmountBox
    aligned vertically left: AmountBox 1px
    aligned vertically all: Slider-item-2


Catfish
    contains: AffordabilityButton
    css padding-top is: 10px
    right of: CalculatorBox



@mobile
-------------------------
Adbanner:
    absent

Catfish
    absent

Footer
    visible



