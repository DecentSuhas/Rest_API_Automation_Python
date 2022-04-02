Feature: Referral

  Scenario: Verify title text in referral banner
    Given User is logged in
    When I perform call to action
    Then I verify title text in banners and referall screen

