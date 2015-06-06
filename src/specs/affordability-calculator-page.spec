==============================================================================
Body				        css		body
RightSection			    css		.right-section
AffordabilityContainer		css		#affordabilityContainer
Catfish				        css		.side-box
Adbanner			        css		.ad-leaderboard iframe
Breadcrumbs			        css		.breadcrumb
SharingWidget			    css		.sharing
ConfirmButton			    id		inPrincipleApprovalButton
CatfishLogo			        css		.sponsor-logo
MainApplicant			    css	    [name=main]
JointMarriedApplicant		css 	[name=jointMarried]
JointUnMarriedApplicant		css 	[name=jointUnMarried]
CatfishMobile               css     .catfish-mobile

================================================================================


@ desktop
---------------------
Adbanner
    visible

Breadcrumbs
    visible

#SharingWidget
#    above: Catfish

AffordabilityContainer
    centered horizontally inside: Body
    contains: Catfish

# Right Section
Catfish
    visible
    contains: ConfirmButton, CatfishLogo

ConfirmButton
    centered horizontally inside: Catfish

CatfishLogo
    centered horizontally inside: Catfish

MainApplicant
   aligned horizontally all: JointMarriedApplicant
   aligned horizontally all: JointUnMarriedApplicant


@ mobile
---------------------
# Right Section
CatfishMobile
    visible

AffordabilityContainer
    centered horizontally inside: Body
