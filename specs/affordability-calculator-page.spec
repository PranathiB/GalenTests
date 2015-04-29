=================================================
Body				css		body
RightSection			css		.right-section
AffordabilityContainer		css		#affordabilityContainer
Catfish				css		.side-box
Adbanner			css		.ad-leaderboard iframe		
Breadcrumbs			css		.breadcrumb
SharingWidget			css		.sharing
ConfirmButton			id		inPrincipleApprovalButton
CatfishLogo			css		.sponsor-logo
=================================================


@desktop
Adbanner
    visible

Breadcrumbs
    visible

SharingWidget
    above: Catfish

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
