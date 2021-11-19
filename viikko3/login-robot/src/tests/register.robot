*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  penaaa  pena1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  pena1235
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  pe  pena1234
    Output Should Contain  Too short username

Register With Valid Username And Too Short Password
    Input Credentials  pena  p1
    Output Should Contain  Too short password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  pena  abcdefghijklmN
    Output Should Contain  password cannot contain only letters

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123
