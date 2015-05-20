load("init.js");
load("pages/AffordabilityCalculatorPage.js");

//testOnDevice(devices.desktop, "Affordability Calculator", "/mortgage/affordability-calculator", function(driver, device)
//{
//	new AffordabilityCalculatorPage(driver).waitForIt();
//  logged("Testing Affordability Calculator on desktop", function() {
//    checkLayout(driver, "specs/affordability-calculator-page.spec", device.tags);
//  })
//});

testOnAllDevices("Affordability Calculator", "/mortgage/affordability-calculator", function(driver, device)
{
  new AffordabilityCalculatorPage(driver).waitForIt();
  logged("Testing Affordability Calculator on devices", function() {
    checkLayout(driver, "specs/affordability-calculator-page.spec", device.tags);
  })
});
