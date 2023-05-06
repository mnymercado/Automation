Feature: Tests for 404 page
  
  Scenario: User is able to navigate amazon tab/windows
    Given Open Amazon product B87NF5WGQ11111111 page
    And Store original window
    When Click on dog image
    And Switch to new window
    Then Verify blog is opened
    And Close blog
    And Return to original window