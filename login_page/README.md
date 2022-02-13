**Goal**  
Implement some tests using selenium & behave on target page in less than 2 hours.
Since there's a time limit, I prioritized finding as many locators as possible and running more tests over best practices 
such as page object model.

**Requirements**  
- Run pip install -r requirements.txt to get the needed python packages (e.g. selenium, behave, gherkin).
- This project is currently only compatible with Chrome browser. Change chrome driver installation path in config.json,
use command "whereis chrome" (linux) to help find it.

**File content**  
- All three scenarios are located in login.feature. Step code is inside login.py.   
- Currently, environment.py only sets the variable for the chrome installation path.
- Config.json currently just sets the path to the webdriver installation.

**Execution**  
From project root, tests are executed with the command behave login_page. When only one scenario is needed, one can use
behave login_page -n "scenario name".

*Example:*

(venv) julio@julio-GE70-2QE:~/PycharmProjects/technicalTest$ behave login_page -n "Free trial"

**Test Scenarios**  

Scenario: Login Attempt with incorrect email and/or password  
Checks that the site rejects login when the wrong credentials are entered

Scenario: Forgot password  
Checks that user is redirected to the password recovery page and that page displays a "Please check your inbox and follow
the instructions to reset your password" message

Scenario: Free trial  
Checks that user is redirected to the free trial page

**@TODO**  
- [ ] Page model: now that locators are confirmed to work, separate pages should be implemented as separate classes  
- [ ] browser yield must happen outside page objects. Wait time should be able to be modified, currently WebDriverWait is
harcoded. Option for headless browser.
- [ ] Test credentials should come from a separate json file and should not be hardcoded.
- [ ] URLs should come from a cfg file or database.
