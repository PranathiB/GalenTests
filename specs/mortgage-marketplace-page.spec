===================================================================
MMForm			css		#mortgage-comparison
SearchBox		css		.mortgage-search-box
BuyingGuides	css		.property-guide-box
SortBy			css		#sortby
PackagesBox		css		#mortgage-results-box
SearchButton	css 	#show-search-button
===================================================================

@all
-----------
SortBy
    below: SearchBox
    width: < 285px
    height: < 40px


@ desktop
-----------------------

MMForm
    contains: SearchBox, BuyingGuides, SortBy, PackagesBox

BuyingGuides
    inside: MMForm 1px right

PackagesBox
   below: SearchBox
   below: SortBy


@ mobile
---------------------
MMForm
    contains: SortBy, PackagesBox

SortBy
    width: < 285px
    height: < 40px

SearchButton
    css bottom is: 0px
    css position is: fixed
	
BuyingGuides
    absent

@ mobile-search
------------------
SearchBox
    image: file ../images/advanced-search.png