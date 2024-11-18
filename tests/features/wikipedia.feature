Feature: Wikipedia App

  Scenario: Open the Wikipedia app and verify homepage title
    Given the Wikipedia app is launched
    When the user opens the app
    Then find "search wikipedia" and click the element
    Then send "Browserstack" as input 
    Then search results