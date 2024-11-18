# PyTest BDD with Browserstack AppAutomate

PyTest Integration with BrowserStack.

![BrowserStack Logo](https://d98b8t1nnulk5.cloudfront.net/production/images/layout/logo-header.png?1469004780)
### Requirements

1. Python 3.7+
    
    - For Windows, download latest python version from [here](https://www.python.org/downloads/windows/) and run the installer executable
    - For Mac and Linux, run `python --version` to see what python version is pre-installed. If you want a different version download from [here](https://www.python.org/downloads/)

### Install the dependencies

To install the dependencies, run the following command in project's base directory:

- For Python 3

    ```sh
    pip3 install -r requirements.txt
    ```

- For Python 2

    ```sh
    pip install -r requirements.txt
    ```

## Getting Started

Getting Started with Pytest-BDD-Appium tests in Python on BrowserStack couldn't be easier!

### Run your first test :

**1. Upload your Android App**

Upload your Android app (.apk or .aab file) to BrowserStack servers using our REST API. Here is an example cURL request :

```
curl -u "YOUR_USERNAME:YOUR_ACCESS_KEY" \
-X POST "https://api-cloud.browserstack.com/app-automate/upload" \
-F "file=@/path/to/apk/file"
```

Ensure that @ symbol is prepended to the file path in the above request. Please note the `app_url` value returned in the API response. We will use this to set the application under test while configuring the test later on.

**Note**: If you do not have an .apk or .ipa file and are looking to simply try App Automate, you can download and test using our [sample Android app](https://www.browserstack.com/app-automate/sample-apps/android/WikipediaSample.apk).


**2. Configure and run your first single test**

Open `test_wikipedia.py` file in `tests` folder:

- Replace `BROWSERSTACK_USERNAME` & `BROWSERSTACK_ACCESS_KEY` with your BrowserStack access credentials. Get your BrowserStack access credentials from [here](https://www.browserstack.com/accounts/settings)

- Replace `bs://<app-id>` with the URL obtained from app upload step

- Set the deviceName and platformVersion. You can refer our [Capability Generator](https://www.browserstack.com/app-automate/capabilities)

- Run the below command to execute a single test on BrowserStack AppAutomate:
    ```
    pytest -s <path/to/your/test/file.py> 
    ```

**3. Configure and run your parallel test**

- In order to run tests in parallel across different configurations, Open `browserstack.yml` file

- Replace `BROWSERSTACK_USERNAME` & `BROWSERSTACK_ACCESS_KEY` with your BrowserStack access credentials. Get your BrowserStack access credentials from [here](https://www.browserstack.com/accounts/settings)

- Replace `bs://<app-id>` wkth the URL obtained from app upload step

- Set the deviceName and platformVersion. You can refer our [Capability Generator](https://www.browserstack.com/app-automate/capabilities)
    
- Run the below command to execute parallel Android test on BrowserStack AppAutomate:
```
browserstack-sdk pytest -s <path/to/your/test/file.py> 
```

- You can access the test execution results, and debugging information such as video recording, network logs on [App Automate dashboard](https://app-automate.browserstack.com/dashboard)

---
