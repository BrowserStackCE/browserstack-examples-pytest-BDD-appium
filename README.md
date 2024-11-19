# BrowserStack Examples PyTest BDD AppAutomate

PyTest Integration with BrowserStack for Appium.

![BrowserStack Logo](https://d98b8t1nnulk5.cloudfront.net/production/images/layout/logo-header.png?1469004780)

# Introduction

This repository demonstrates an Appium test framework written in Pytest BDD (Behavior Driven Development). It leverages the power of Pytest and the pytest-bdd plugin to write and execute BDD-style tests for mobile applications. 
The Appium script is designed for automating tests on the [Wikipedia Sample Android app](https://www.browserstack.com/app-automate/sample-apps/android/WikipediaSample.apk). 
The script has the ability to run single or parallel test on BrowserStack.

# Prerequisite

Ensure you have Python 3.6+
    
    - For Windows, download latest python version from [here](https://www.python.org/downloads/windows/) and run the installer executable
    - For Mac and Linux, run `python --version` to see what python version is pre-installed. If you want a different version download from [here](https://www.python.org/downloads/)

# Repository Setup

- Clone the repository

- Install dependencies :

Run the following command in project's base directory:
```sh
    pip3 install -r requirements.txt
```

- Upload the Wikipedia Sample Android App

Upload the [Wikipedia Sample Android app](https://www.browserstack.com/app-automate/sample-apps/android/WikipediaSample.apk) to BrowserStack servers using our [REST API](https://www.browserstack.com/docs/app-automate/api-reference/appium/apps#upload-an-app). Here is an example cURL request :

```
curl -u "YOUR_USERNAME:YOUR_ACCESS_KEY" \
-X POST "https://api-cloud.browserstack.com/app-automate/upload" \
-F "file=@/path/to/apk/file"
```

Ensure that @ symbol is prepended to the file path in the above request. Please note the `app_url` value returned in the API response. We will use this to set the application under test while configuring the test later on.

# Running the test :

**1. Configure and run single test**

Open `test_wikipedia.py` file in `tests` folder:

- Replace `BROWSERSTACK_USERNAME` & `BROWSERSTACK_ACCESS_KEY` with your BrowserStack access credentials. Get your BrowserStack access credentials from [here](https://www.browserstack.com/accounts/settings)

- Replace `bs://<app-id>` with the URL obtained from app upload step

- Set the deviceName and platformVersion. You can refer our [Capability Generator](https://www.browserstack.com/app-automate/capabilities)

- Run the below command to execute a single test on BrowserStack AppAutomate:
    ```
    pytest -s tests/test_wikipedia.py 
    ```

**2. Configure and run parallel test**

- In order to run tests in parallel across different configurations, Open `browserstack.yml` file

- Replace `BROWSERSTACK_USERNAME` & `BROWSERSTACK_ACCESS_KEY` with your BrowserStack access credentials. Get your BrowserStack access credentials from [here](https://www.browserstack.com/accounts/settings)

- Replace `bs://<app-id>` wkth the URL obtained from app upload step

- Set the deviceName and platformVersion. You can refer our [Capability Generator](https://www.browserstack.com/app-automate/capabilities)
    
- Run the below command to execute parallel test on BrowserStack AppAutomate:
```
browserstack-sdk pytest -s tests/test_wikipedia.py
```

# Notes
- You can access the test execution results, and debugging information such as video recording, network logs on [App Automate dashboard](https://app-automate.browserstack.com/dashboard)

- You can export the environment variables for the Username and Access Key of your BrowserStack account :
```
export BROWSERSTACK_USERNAME=<browserstack-username> &&
export BROWSERSTACK_ACCESS_KEY=<browserstack-access-key> &&
export BROWSERSTACK_APP_ID=<app_url or custom_id>
```

---
