===================================================================
MMForm			css		#mortgage-comparison
SearchBox		css		.mortgage-search-box
BuyingGuides	css		.col-sm-4.hidden-xs.box.property-guide-box
SortBy			css		#sortby
PackagesBox		css		#mortgage-results-box
===================================================================

@ desktop
-----------------------

MMForm
    contains: SearchBox, BuyingGuides, SortBy, PackagesBox

BuyingGuides
    inside: MMForm 0px right

SortBy
    below: SearchBox
    width: 276px
    height: 36px

PackagesBox
   below: SearchBox
   below: SortBy
