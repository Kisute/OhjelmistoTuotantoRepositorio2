*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kalle123
    Output Should Contain  Logged in

Login With Incorrect Password
    Create User  kalle2    kalle123
    Input Login Command
    Input Credentials    kalle2    kalle1234
    Run Application
    Output Should Contain    Invalid username or password

Login With Nonexistent Username
    Create User  kalle3    kalle123
    Input Login Command
    Input Credentials    kalle4    kalle123
    Run Application
    Output Should Contain    Invalid username or password

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command
    
