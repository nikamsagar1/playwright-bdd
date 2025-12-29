# Glossary - Automation Testing Terms Explained Simply

This guide explains technical terms in simple English. If you see an unfamiliar word, it's probably here!

---

## A

### Artifact
**What it is**: Files generated after running tests (reports, screenshots)

**Example**: After tests run on GitHub Actions, you download test reports as "artifacts"

**In simple terms**: The stuff left over after tests finish running

---

## B

### BDD (Behavior-Driven Development)
**What it is**: Writing tests in plain English that anyone can understand

**Example**:
```gherkin
Given user is on login page
When user clicks login button
Then dashboard is displayed
```

**In simple terms**: Tests written like English sentences instead of code

### Browser
**What it is**: Application that visits websites (Chrome, Firefox, Safari, Edge)

**Example**: When you manually go to google.com, you use a browser

**In simple terms**: The thing you use to visit websites

### Headless
**What it is**: Running browser without showing the screen

**Example**: Tests run faster without showing browser window

**In simple terms**: Invisible testing (no window shown)

---

## C

### CI/CD
**What it is**: Automatically running tests when code changes

**Example**: Push code → Tests run automatically → Results shown

**In simple terms**: Letting robots run your tests automatically

### CSS Selector
**What it is**: Way to find elements on a webpage using CSS

**Example**: `input[name='username']` finds input field with name "username"

**In simple terms**: Pattern to find specific page elements

### Locator
**What it is**: Way to find an element on the webpage

**Example**: ID, class name, CSS selector, XPath

**In simple terms**: The address of something on a webpage

---

## D

### DevOps
**What it is**: Team that automates deployment and testing

**Example**: Creates CI/CD pipelines

**In simple terms**: People who make things automatic

### Debug / Debugging
**What it is**: Finding and fixing what's wrong

**Example**: Test fails → Run with --headed → Watch what happens → Fix code

**In simple terms**: Problem-solving mode

---

## E

### Element
**What it is**: Component on a webpage

**Example**: Button, text field, dropdown, link

**In simple terms**: Clickable things on a website

### Environment
**What it is**: Different versions of the app (QA, UAT, Production)

**Example**: 
- QA: Testing version
- UAT: User acceptance version
- Prod: Real version for users

**In simple terms**: Different copies of the app

---

## F

### Feature File
**What it is**: File with test scenarios in plain English (.feature)

**Example**: `login.feature` with login test scenarios

**In simple terms**: Human-readable test description

### Fixture
**What it is**: Setup/teardown code that runs before/after tests

**Example**: Open browser → Run test → Close browser

**In simple terms**: Preparation and cleanup code

---

## G

### Gherkin
**What it is**: Language for writing tests in plain English

**Keywords**: Given, When, Then, And, But

**Example**:
```gherkin
Given user is on login page
When user enters password
Then page shows success
```

**In simple terms**: English-like language for tests

### GitHub Actions
**What it is**: Automated testing service from GitHub

**Example**: Run tests on GitHub servers automatically

**In simple terms**: Cloud service that runs your tests

---

## H

### Headless Mode
**What it is**: Running browser without displaying window

**Example**: Tests run invisible (no window shown)

**In simple terms**: Hidden browser testing

---

## I

### Integration Testing
**What it is**: Testing multiple components working together

**Example**: Test login → Dashboard → Add user → Logout

**In simple terms**: Testing the whole flow

---

## J

### JSON
**What it is**: File format for storing data

**Example**: `env_config.json` stores URLs and credentials

**In simple terms**: Text file with data organized nicely

### JUnit
**What it is**: Format for test results

**Example**: `junit.xml` - test results file

**In simple terms**: Standard way to store test results

---

## L

### Locator
**What it is**: Way to find elements on page

**Types**: ID, Class, CSS, XPath, Text match

**Example**: `#username` finds element with ID "username"

**In simple terms**: "Address" of an element on the page

---

## M

### Mock / Mocking
**What it is**: Pretending something exists when it doesn't

**Example**: Mock server returns fake data

**In simple terms**: Fake version of something for testing

---

## O

### Object-Oriented Programming (OOP)
**What it is**: Way of writing code using classes and objects

**Example**: LoginPage class contains login methods

**In simple terms**: Organizing code into logical groups

---

## P

### Page Object
**What it is**: Python class representing a web page

**Example**: LoginPage class with login methods

**In simple terms**: Code that controls one webpage

### Page Object Model (POM)
**What it is**: Design pattern for organizing automation code

**Idea**: One class per page, organize by page

**In simple terms**: Keeping page logic separate from test logic

### Pipeline
**What it is**: Automated workflow (usually in CI/CD)

**Example**: GitHub Actions workflow with multiple steps

**In simple terms**: Series of automatic actions

### Playwright
**What it is**: Library for automating browser interactions

**What it does**: Click, type, navigate, verify

**In simple terms**: Tool for controlling browser automatically

### Pytest
**What it is**: Python testing framework

**Purpose**: Run tests, generate reports

**In simple terms**: Tool for running Python tests

---

## Q

### QA (Quality Assurance)
**What it is**: Team that tests software

**Purpose**: Find bugs before users do

**In simple terms**: People who check if software works

---

## R

### Regression Testing
**What it is**: Testing to make sure old features still work

**Example**: After adding feature X, test that feature Y still works

**In simple terms**: Making sure you didn't break anything

### Report
**What it is**: Summary of test results

**Example**: HTML report showing passed/failed tests

**In simple terms**: Grade sheet for your tests

---

## S

### Scenario
**What it is**: Single test case in a feature file

**Example**: "Admin can login with valid credentials" is one scenario

**In simple terms**: One test story

### Screenshot
**What it is**: Picture of screen taken during test

**Purpose**: Debugging failed tests

**In simple terms**: Photo of what the test saw

### Smoke Test
**What it is**: Quick test of main functionality

**Purpose**: Ensure basic features work

**In simple terms**: Quick sanity check

### Step Definition
**What it is**: Python code for Gherkin steps

**Example**: Code that makes "When user clicks button" work

**In simple terms**: Translation from English to code

---

## T

### Test Case
**What it is**: Single test that checks one thing

**Example**: "User can login with valid credentials"

**In simple terms**: One thing to test

### Test Suite
**What it is**: Collection of related tests

**Example**: All login tests together

**In simple terms**: Group of tests

### Timeout
**What it is**: Maximum time to wait for something

**Example**: Wait 5000ms for element to appear

**In simple terms**: Patience limit in seconds/milliseconds

---

## U

### UAT (User Acceptance Testing)
**What it is**: Environment where users test before release

**Example**: Real users try the app before it goes live

**In simple terms**: Testing by actual users

### Unit Testing
**What it is**: Testing individual code functions

**Example**: Test if login function works

**In simple terms**: Testing one small piece at a time

---

## W

### Wait / Waiting
**What it is**: Pausing test until something happens

**Example**: Wait for element to appear

**In simple terms**: Giving page time to load

### Workflow
**What it is**: Series of steps in automation

**Example**: GitHub Actions workflow with setup → test → report

**In simple terms**: Step-by-step instructions for automation

---

## X

### XPath
**What it is**: Way to find elements using path syntax

**Example**: `//button[contains(text(), 'Login')]`

**In simple terms**: Complex way to find elements (last resort)

---

## Key Acronyms Quick Reference

| Acronym | Stands For | Meaning |
|---------|-----------|---------|
| BDD | Behavior-Driven Development | English-like testing |
| CI/CD | Continuous Integration/Deployment | Auto testing/deployment |
| QA | Quality Assurance | Testing team |
| UAT | User Acceptance Testing | User testing |
| OOP | Object-Oriented Programming | Code organization style |
| POM | Page Object Model | Testing design pattern |
| HTML | HyperText Markup Language | Web page format |
| XML | Extensible Markup Language | Data format |
| JSON | JavaScript Object Notation | Data format |
| CSS | Cascading Style Sheets | Web styling |
| API | Application Programming Interface | Way software talks to software |
| SDK | Software Development Kit | Tools for developers |

---

## Common Testing Terms

### Pass ✅
- Test executed successfully
- Expected result matched actual result
- "The test passed!"

### Fail ❌
- Test did not pass
- Expected result didn't match
- "The test failed!"

### Skip ⏭️
- Test was not executed
- Usually because condition not met
- "The test was skipped!"

### Error ⚠️
- Something went wrong in test code
- Not a failure - a mistake
- "Error: element not found!"

### Warning ⚡
- Something might be wrong
- But test still ran
- "Warning: slow response!"

---

## Testing Levels

### Unit Testing
**What**: One function/method
**Speed**: Fast ⚡
**Example**: Test if login() function works

### Integration Testing
**What**: Multiple components together
**Speed**: Medium ⚡⚡
**Example**: Login + Dashboard + Logout

### End-to-End (E2E) Testing
**What**: Complete user journey
**Speed**: Slow ⚡⚡⚡
**Example**: User registers → Logs in → Buys product → Logs out

### System Testing
**What**: Entire system
**Speed**: Very slow ⚡⚡⚡⚡
**Example**: Whole application on production

---

## Test Types

### Functional Testing
**Purpose**: Does it work as expected?
**Example**: Can user login?

### Performance Testing
**Purpose**: Is it fast enough?
**Example**: Page loads in < 2 seconds?

### Security Testing
**Purpose**: Is it secure?
**Example**: Can hacker steal passwords?

### Usability Testing
**Purpose**: Is it easy to use?
**Example**: Can users find login button?

---

## Environments Quick Ref

| Environment | Purpose | Audience | Risk |
|-------------|---------|----------|------|
| Development | Developer testing | Developers | High |
| QA | Quality testing | Testers | High |
| UAT | User testing | End users | Medium |
| Staging | Pre-release | Internal | Low |
| Production | Live system | All users | None (must be stable!) |

---

## Browser Terminology

### Browser Engine
**What**: The actual software running browser
**Types**: Chromium, WebKit, Firefox
**In simple terms**: Engine behind browser

### Headless Browser
**What**: Browser without UI
**Speed**: Faster
**Purpose**: Testing without showing window

### Browser Context
**What**: Isolated browser session
**Like**: Incognito window
**Purpose**: Separate from main browser

---

## Tips for Learning

1. **Don't memorize everything** - Use this glossary when needed
2. **Learn by doing** - Terms make sense when you use them
3. **Look things up** - When confused, search glossary
4. **Ask questions** - If explanation unclear, ask for example
5. **Read documentation** - Links explain concepts more

---

## Additional Resources

### Where to Learn More

| Topic | Resource |
|-------|----------|
| Gherkin | cucumber.io/docs/gherkin |
| Playwright | playwright.dev |
| pytest | pytest.org |
| Python | python.org |
| Git | git-scm.com |

---

## Summary

**Remember:**
- 🎯 **Automation**: Making computers do repetitive testing
- 📝 **Gherkin**: English-like language for tests
- 🐍 **Python**: Programming language used here
- 🎭 **Playwright**: Tool for browser automation
- ✅ **Testing**: Checking if software works correctly

---

**Have a term not listed here? Add it to this glossary!**

**Last Updated**: December 29, 2025
