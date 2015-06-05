===============================================================
Adbanner			        css			.ad-leaderboard iframe
BannerSection               css         .section.banner
MortgageIndex               id          #mortgage-index
NewMortgageBox              css         .new-banner-box
ReMortgageBox               css         .re-banner-box
Banner-box-*                css         .banner-box
PackageContainer            css         .section.featured
AffordabilitySection        css         .affordability-section
GuidesSection               css         .guides-section
BanksSection                css         .banks

===============================================================

    
@desktop
---------------------------------------
NewMortgageBox
    aligned horizontally all: ReMortgageBox
    above: PackageContainer

Adbanner
    visible
    below: NewMortgageBox
    below: ReMortgageBox


@ mobile
-----------------------------------
NewMortgageBox
    above: ReMortgageBox
    

@all
--------------------------------------
BannerSection
    contains: NewMortgageBox, ReMortgageBox
    
PackageContainer
    below: Adbanner
    above: BanksSection
    above: AffordabilitySection

BanksSection
    below: PackageContainer
    image: file images/BanksSection.png, error 20%

AffordabilitySection
    above: GuidesSection
    below: BanksSection

GuidesSection
    below: PackageContainer
