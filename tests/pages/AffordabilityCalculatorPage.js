importClass(org.openqa.selenium.interactions.Actions);

this.AffordabilityCalculatorPage = function (driver) {
    GalenPages.extendPage(this, driver, {
        affordabilityContainer: "#affordabilityContainer"
    });
};