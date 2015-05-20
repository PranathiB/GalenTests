var domain = "rr.propertyguru.com.sg";

/*
A list of all devices that will be used in our tests
*/
var devices = {
    mobile: {
        deviceName: "mobile",
        size: "320x568",
        tags: ["mobile", "all"]
    },
    tablet: {
        deviceName: "tablet",
        size: "1024x768",
        tags: ["tablet", "all"]
    },
    desktop: {
        deviceName: "desktop",
        size: "1920x1080",
        tags: ["desktop", "all"]
    }
};

var TEST_USER = {
    username: "testuser@example.com",
    password: "test123"
};

/*
This function creates an instance of WebDriver
and stores it in a test session. Later it will be picked up 
by after-test event
*/
function openDriver(url, device) {
    var driver = createDriver(null, device.size);

    session.put("driver", driver);

    // Checking if url is actually a uri or a full url
    if (url != null) {
        if (url.indexOf("http://") != 0 && url.indexOf("https://") != 0) {
            url = "http://" + domain + url;
        }
        driver.get(url);
    }
    else {
        console.log(device);
        if(device == "mobile")
          driver.get("http://m."+ domain);
        else
          driver.get("http://" + domain);
    }
    return driver;
}

/*
This event will be called after each test.
Here we will close the browser window.
Also in case of test failure we shall make a screenshot 
and attach it to the report
*/
afterTest(function (test) {
    var driver = session.get("driver");
    if (driver != null) {
        if (test.isFailed()) {
            session.report().info("Screenshot").withAttachment("Screenshot", takeScreenshot(driver));
        }
        driver.quit();
    }
});



function _test(testNamePrefix, url, callback) {
    test(testNamePrefix + " on ${deviceName} device", function (device) {
        var driver = openDriver(url, device);
        callback.call(this, driver, device);
    });
}

/*
This function will be used in our tests in order to create 
a list of tests parameterize for each device that we have defined in the begining
*/
function testOnAllDevices(testNamePrefix, url, callback) {
    forAll(devices, function () {
        _test(testNamePrefix, url, callback);
    });
}

/*
This function is used in order to create a single test for a specific device
*/
function testOnDevice(device, testNamePrefix, url, callback) {
    forOnly({device: device}, function() {
        _test(testNamePrefix, url, callback);
    });
}

/*
    Exporting functions to all other tests that will use this script
*/
(function (export) {
    export.devices = devices;
    export.openDriver = openDriver;
    export.testOnAllDevices = testOnAllDevices;
    export.TEST_USER = TEST_USER;
})(this);