Feature: Amazon Bestseller Feature

  Scenario: Amazon Bestseller Page Nav Links
    Given Open Amazon Bestseller Page
    Then Verify Nav has 5 links

  Scenario: Amazon Best Seller Test case using loop
    Given Open Amazon Bestseller Page
    Then Verify each nav opens the right page