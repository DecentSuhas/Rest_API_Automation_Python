Feature: Referral

  @test
  Scenario: Verify title text in referral banner
    Given User is logged in
    When I hit the prefetch api and get the response
    Then I verify title text in banners and referral screen

