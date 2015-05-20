===================================================================
MMForm			css		#mortgage-comparison
SearchBox		css		.mortgage-search-box
BuyingGuides	css		.property-guide-box
SortBy			css		#sortby
PackagesBox		css		#mortgage-results-box
SearchButton	css 	#show-search-button
AdvancedSearch  css     .search-more-option
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
    inside: MMForm 0px right

PackagesBox
   below: SearchBox
   below: SortBy

AdvancedSearch
   absent


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
AdvancedSearch
  visible
SearchBox
    image: file ../images/advanced-search.png