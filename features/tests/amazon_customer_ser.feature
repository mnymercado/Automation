Feature: Go to Amazon Customer Service Page

  Scenario: Verify elements on Customer Service Page
    Given Open Amazon page
    When Go to Customer Service Page
    And Verify text Welcome to Amazon Customer Service is shown
    Then Verify 10 div is shown
    Then Verify the Search our help library, All help topics is present and input field is present
    Then Verify 11 Search help topics