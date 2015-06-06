============================================
Body			        css	body
Breadcrumbs		        css	.breadcrumb
AffordabilityContainer	id	affordabilityContainer
PropertyValueGraph	    id	property-value-graph
OutlayGraph		        id	total-outlay-graph
LTVGraph		        id	ltv-graph
CashDownpaymentGraph 	id	cash-downpayment-graph
TDSRGraph		        id	tdsr-report-graph
MSRGraph		        id	msr-report-graph
CatfishLogo		        css	.sponsor-logo
Sidebar			        css	.right-section .box
SharingWidget		    css	.sharing

================================================

@desktop
AffordabilityContainer
    contains: PropertyValueGraph, OutlayGraph, PropertyValueGraph, LTVGraph, CashDownpaymentGraph, TDSRGraph, MSRGraph, CatfishLogo, Sidebar, SharingWidget
    centered horizontally inside: Body

PropertyValueGraph
    aligned horizontally all: OutlayGraph

LTVGraph
    aligned vertically all: TDSRGraph
    aligned vertically all: CashDownpaymentGraph
    aligned vertically all: MSRGraph


#SharingWidget
#   above: Sidebar

CatfishLogo
    visible

Breadcrumbs
    visible 
