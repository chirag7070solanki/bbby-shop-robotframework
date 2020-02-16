*** Settings ***
Resource  ../StepDefs/HomepageStepDefs.robot
Variables       /Users/chiragsolanki/PycharmProjects/Shop-Automation/utilities/selenium_functions.py

Test Setup  I open website
Test Teardown  I close browser

*** Test Cases ***
PLP Loading 1
    When I choose to close IO pop up modal
    Then I choose to navigate to L2 PLP     Bath    Bath Towels
    Then I verify user landed on PLP

PLP Loading 2
    When I choose to close IO pop up modal
    Then I choose to navigate to L2 PLP     Furniture    Bedroom
    Then I verify user landed on PLP

