# Created by nicolemercado at 4/25/23
Feature: SignIn to Amazon

  Scenario: User can try to signin in Amazon
    Given Open Sign-In Amazon page
    When Click Returns and Orders
    And Input in input field Nicole
    Then Verify amazon logo, continue button, Need help, Forgot Password, Other issues with Sign-In, Create you Amazon account button and Sign in text is shown

  Scenario: Check Amazon Cart if Empty
    Given Open Sign-In Amazon page
    When Click Cart
    Then Verify that Your Amazon Cart is empty

  Scenario: Sign in Page open from Sign In popup
    Given Open Amazon page
    When Click pop up Sign in page
    Then Verify Sign in Page is open

