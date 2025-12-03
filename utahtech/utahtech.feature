Feature: Utah Tech Library Test

    Scenario: Check the title
        Given I open the url "https://library.utahtech.edu/"
        Then I expect that the title is "Utah Tech University Library"

    Scenario: I click on "E-book Collections"
        Given I open the url "https://library.utahtech.edu/"
        When I click on the element "[href='databases/ebooks.html']"
        Then I expect that the url is "https://library.utahtech.edu/databases/ebooks.html"
    
    Scenario: I click on "Faculty Services"
        Given I open the url "https://library.utahtech.edu/"
        When I click on the element "[id='14']"
        Then I expect that element "[id='405']" is visible

    Scenario: I want to book a room
        Given I open the url "https://library.utahtech.edu/"
        When I click on the element "[class = 'scheduler']"
        Then I expect that the path is not "https://library.utahtech.edu/"

    Scenario: I want to go to their twitter
        Given I open the url "https://library.utahtech.edu/"
        When I click on the element "[src='images/common/twitter.svg']"
        Then I expect that the url is "https://x.com/utahtechu"

    Scenario: I search for a book
        Given I open the url "https://library.utahtech.edu/"
        When I click on the button "[class='eb-search__submit-button']"
        Then I expect that the path is not "https://library.utahtech.edu/"

    Scenario: I ask a librarian
        Given I open the url "https://library.utahtech.edu/"
        When I pause for 1000ms
        When I click on the element "[href='#']"
        Then I expect a new window has been opened

    Scenario: I want to go back to the main page
        Given I open the url "https://library.utahtech.edu/"
        When I click on the element "[href='https://utahtech.edu/']"    
        Then I expect that the url is "https://utahtech.edu/"
    
    Scenario: I want to see their email
        Given I open the url "https://library.utahtech.edu/"
        Then I expect that element "[id='footer-contact']" contains the text "225 South 700 East, St. George, Utah 84770—Tel. 435-652-7714—Email: library@utahtech.edu"

    Scenario: I want to see their email
        Given I open the url "https://library.utahtech.edu/"
        When I click on the element "[href='https://utahtech.libinsight.com/add.php?wid=6&type=1&token=4fd3a48ed4f170ea20026047c83066a0']"
        Then I expect the url to contain "utahtech.libinsight.com/"