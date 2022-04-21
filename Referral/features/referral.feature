Feature: Referral

  #@api_test
  Scenario: Verify title text in referral banner
    Given The user is logged in
    When I hit the prefetch api and get the response
    Then I verify title text in banners and referral screen

  @api_test
  Scenario: Verify title text in referral full screen
    Given The user is logged in
    When I hit the prefetch api and get the response
    Then I verify the title text of referral full screen

  #@api_test
  Scenario: Verify description in referral banner in all entry points
    Given The user is logged in
    When I hit the prefetch api and get the response
    Then I verify the description text in referral banner entry points

  #@api_test
  Scenario: Verify the referral campaign
    Given The user is logged in
    When I hit the prefetch api and get the response
    Then I verify the campaign text

  #@api_test
  Scenario: Verify the how it works title text and description
    Given The user is logged in
    When I hit the prefetch api and get the response
    Then I verify the how it works title and description