Feature: login


  Background:
    Given login page can be reached


  Scenario: Login Attempt with incorrect email and/or password
    When user inputs email
    And user inputs password
    And user clicks login
    Then user remains in the same page


  Scenario: Forgot password
    When user clicks on forgot password
    Then page goes to reset password
    When user inputs email
    And user clicks on reset request button
    Then page displays email sent message


  Scenario: Free trial
    When user clicks on free trial link
    Then page navigates to free trial section






