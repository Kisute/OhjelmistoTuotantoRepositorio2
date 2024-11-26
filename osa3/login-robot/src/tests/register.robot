*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials    leila  Leila123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password     
    Input Credentials    kallee    kalle1234        
    Input New Command    
    Input Credentials    kallee    kalle1234     
    Run Application     
    Output Should Contain    Username kallee already taken
    
Register With Too Short Username And Valid Password     
    Input Credentials    aa  kalle123     
    Input New Command     
    Run Application     
    Output Should Contain    Username too short  

Register With Enough Long But Invalid Username And Valid Password     
    Input Credentials    kalle_  kalle123     
    Input New Command     
    Run Application   
    Output Should Contain    Invalid username  
     
Register With Valid Username And Too Short Password     
    Input Credentials    kalle  k     
    Input New Command     
    Run Application    
    Output Should Contain    Password too short 

Register With Valid Username And Long Enough Password Containing Only Letters     
    Input Credentials    kalle  kallekalle     
    Input New Command     
    Run Application     
    Output Should Contain    Password containing only letters

*** Keywords ***
Create User And Input New Command
    Input New Command


