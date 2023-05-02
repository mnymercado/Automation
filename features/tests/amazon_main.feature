Feature: Amazon main page tests

  Scenario: User can see hamburger menu
    Given Open Amazon page
    Then Verify hamburger menu icon

  Scenario: Footer has correct number of links
    Given Open Amazon page
    Then Verify footer has 35 links
    Then Verify header has 5 links