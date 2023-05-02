# Created by nicolemercado at 4/25/23
Feature: Amazon search tests

  Scenario: User can search for coke in Amazon
    Given Open Amazon page
#    When Allow to sleep
    When Input text coke
    When Click on search button
    Then Verify that text "coke" is shown

  Scenario: User can search for chair in Amazon
    Given Open Amazon page
#    When Allow to sleep
    When Input text chair
    When Click on search button
    Then Verify that text "chair" is shown