# Created by nicolemercado at 4/25/23
Feature: Amazon search tests

  Scenario Outline: User can search for coke in Amazon
    Given Open Amazon page
#    When Allow to sleep
    When Input text <search_word>
    When Click on search button
    Then Verify that text <expected_res> is shown
    Examples:
      | search_word | expected_res |
      | coke        | "coke"       |
      | chair       | "chair"      |
      | tissue      | "tissue"     |

  Scenario: User can search for chair in Amazon
    Given Open Amazon page
#    When Allow to sleep
    When Input text chair
    When Click on search button
    Then Verify that text "chair" is shown

  Scenario: Check Amazon cart if not empty
    Given Open Amazon page
    When Input text coke
    When Click on search button
    And Click first product
    And Click Add to Cart button
    And Go to Amazon Cart
    Then Verify cart not empty