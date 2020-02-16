*** Settings ***
Library     SeleniumLibrary
Library     /Users/chiragsolanki/PycharmProjects/Shop-Automation/utilities
Library     /Users/chiragsolanki/PycharmProjects/Shop-Automation/constants
Library     /Users/chiragsolanki/PycharmProjects/Shop-Automation/testcases/CustomSeleniumLibrary.py

#Variables       /Users/chiragsolanki/PycharmProjects/Shop-Automation/testcases/CustomSeleniumLibrary.py
Variables       /Users/chiragsolanki/PycharmProjects/Shop-Automation/utilities/selenium_functions.py
Variables       /Users/chiragsolanki/PycharmProjects/Shop-Automation/pageobjects/homepage.py
Variables       /Users/chiragsolanki/PycharmProjects/Shop-Automation/pageobjects/plppage.py

*** Variables ***
${globaldriver}
${driver}
${browser}     "chrome"
${url}     "https://bedbathandbeyond.com"


*** Keywords ***
I open website
    ${driver}=  call method     ${selenium_functions}     set_web_driver_and_launch_site      chrome      https://bedbathandbeyond.com
    Log     ${driver}
    set global variable     ${globaldriver}     ${driver}
    Log     ${globaldriver}

I close browser
    call method     ${selenium_functions}     quite_webdriver    ${globaldriver}
    sleep  5

I choose to close IO pop up modal
    Log     Complete

I choose to navigate to L2 PLP
    [Arguments]  ${l1cat}   ${l2cat}
    log  Navigating to L2 PLP
    call method  ${homepage}    navigate_to_l0      ${globaldriver}       Categories
    call method  ${homepage}    navigate_to_l1      ${globaldriver}       move to       ${l1cat}
    call method  ${homepage}    navigate_to_l2      ${globaldriver}       click         ${l1cat}      ${l2cat}

I verify user landed on PLP
    log             Checking if PLP is loaded
    call method     ${plp}                          check_per_page_sort                 ${globaldriver}
    call method     ${plp}                          check_if_product_grid_displayed     ${globaldriver}

