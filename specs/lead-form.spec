==================================================================================
ModalContainer		css		#inPrincipleApprovalForm
ModalDialog		css		#inPrincipleApprovalForm .modal-dialog
BankLogo		css		.bank-logo
LeadText		css		.lead-text-section
==================================================================================
@ all
-----------------------------
ModalDialog
  contains: BankLogo

@ desktop
----------------
ModalDialog
    centered horizontally inside: ModalContainer

BankLogo
  right of: LeadText

@ mobile
----------------
ModalDialog
    centered horizontally on: ModalContainer 20px

BankLogo
   below: LeadText


