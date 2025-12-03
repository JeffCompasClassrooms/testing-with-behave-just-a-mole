Feature: Amazon Christmas Shopping

  Scenario: Check if the logo is there
    Given I open the Amazon home page
    Then I expect the Amazon logo to be visible

  Scenario: Search for video games
    When I search for "video games"
    Then I expect the results text to contain "Popular Shopping Ideas"

   Scenario: Add an item to the cart
    When I search for "HDMI Cable"
    And I select the first result
    And I click the add to cart button
    Then I expect the cart count to be "1"

    Scenario: View the cart
     When I click the cart button
     Then I expect to see the subtotal

    Scenario: Change Language to Spanish
      Given I open the Amazon home page
      When I click the language settings
      And I select Spanish
      And I save the language changes
      Then I expect the navigation to be in Spanish
  
    Scenario: Change Language back to English
      Given I open the Amazon home page
      When I click the language settings
      And I select English as the language
      And I save the language changes
      Then I expect the navigation to be in English

    Scenario: Add item to cart and delete it
     When I search for "Toy"
     And I select the first result
     And I click the add to cart button
     And I click the cart button
     And I click the delete button
     Then I expect the cart to have 1 item

    Scenario: Search for Coffee Mug and view details
     Given I open the Amazon home page
     When I search for "Coffee Mug"
     And I select the first result
     Then I expect to see the product title

    Scenario: Verify Footer Link (Careers)
      Given I open the Amazon home page
      When I scroll to the bottom of the page
      And I click the Careers link
      Then I expect to see the Careers page

    Scenario: Attempt Login with Empty Email
      Given I open the Amazon home page
      When I click the sign in button
      And I click Continue without entering email
      Then I expect to see the missing email error

    Scenario: Search with No Results
      Given I open the Amazon home page
      When I search for "fjkdsjkfdsajkfdsakjfdsjk"
      Then I expect to see the no results message

    Scenario: Verify Item Stock Status
      Given I open the Amazon home page
      When I search for "AA Batteries"
      And I select the first result
      Then I expect the item to be In Stock

    Scenario: Navigate to Registry
      Given I open the Amazon home page
      When I click the Registry link
      Then I expect to see the Registry header

    Scenario: Navigate to Gift Cards
      Given I open the Amazon home page
      When I click the Gift Cards link
      Then I expect to see the Gift Cards header

    Scenario: Navigate to Best Sellers
      Given I open the Amazon home page
      When I click the Best Sellers link
      Then I expect to see the Best Sellers header