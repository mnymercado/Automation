Feature: Tests for products Page

  Scenario: User can select specific product colors
    Given Open Amazon product B08JHKQPBV page
    Then Verify user can click through colors

  Scenario: User can select the specified product colors
    Given Open Amazon product B07BJKRR25 page
    Then Verify user can clicks through specified color
