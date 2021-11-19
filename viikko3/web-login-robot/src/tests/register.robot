*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  peikko
    Set Password  abcd1234
    Set Password Confirmation  abcd1234
    Submit Credentials
    Main Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  pl
    Set Password  abcd1234
    Set Password Confirmation  abcd1234
    Submit Credentials
    Register Should Fail With Message  Too short username
    
Register With Valid Username And Too Short Password
    Set Username  penatintin
    Set Password  12a
    Set Password Confirmation  12a
    Submit Credentials
    Register Should Fail With Message  Too short password

Register With Nonmatching Password And Password Confirmation
    Set Username  oonväsyyy
    Set Password  123asdfh
    Set Password Confirmation  en2haluumachata
    Submit Credentials
    Register Should Fail With Message  Passwords dont mach

Login After Successful Registration
    Create User  Liikaa  tehtäviä312
    Go To Login Page
    Set Username  Liikaa
    Set Password  tehtäviä312
    Submit Login
    Title Should Be  Ohtu Application main page


Login After Failed Registration
    Set Username  l
    Set Password  12a
    Set Password Confirmation  12a
    Go To Login Page
    Set Username  l
    Set Password  tehtäviä312
    Submit Login
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Submit Login
    Click Button  Login

Main Page Should Be Open
    Title Should Be  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}