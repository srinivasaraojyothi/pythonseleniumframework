Feature: twitter posting
@api
Scenario Outline:  creating user
Given I should be able to connect to API with "<testcaseid>"
Then I should be able verify user is created successfully with status code is "201"
And I should be able to verify the created message 

Examples:
    | testcaseid |
    | testcase_payment_1 |

Scenario Outline:  report
Given I should be able to connect to API with "<testcaseid>"
Then I should be able verify responce has product as "astro"
#And I should be able to verify responce has "init" key

Examples:
    | testcaseid |
    | testcase_payment_2_2 |