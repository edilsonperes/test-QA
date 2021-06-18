Feature: Book a service

Scenario: User successfully search for a service and book a time
    Given User access "mytime" page
    And Searches for a service in a city
    And User is presented with at least 3 reasults
    When User opens any business
    And Selects all services in the services filter from the left panel
    And Selects second staff in the staff filter from the left panel
    And Clicks the button "Men`s Haircut" service
    And Clicks "Select Time" in the add-on modal opened
    Then User is presented with a list of available time slots with at least 2 entries
    And Service displayed in the right side panel is the one selected before
    And Service price in the right side panel is the same as the one displayed before
    And Staff selected is the staff chosen before