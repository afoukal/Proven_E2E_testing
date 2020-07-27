# Created by Bogos at 7/26/2020
Feature: Test Scenarios for Quiz functionality

  Scenario: User can see "3 minutes to your best skincare, let's go!" message
    Given Open Home page
    When Choose Get My Formula
    Then Verify introductory message is displayed

  Scenario: User sees "What are your main skin concerns?" and Choose all that apply
    Given Open Home page
    When Choose Get My Formula
    When Introductory message disappear
    Then Concern question is displayed
    And Concern question instruction is displayed

  Scenario: User sees Sensitivity, Redness, Fine lines or wrinkles, Loss of firmness or elasticity, Hyperpigmentation, Acne, Dryness, Other options
    Given Open Home page
    When Choose Get My Formula
    When Introductory message disappear
    Then All concern options are displayed

  Scenario: "How sensitive is your skin" question is visible
    Given Open Q1_sensitivity question


  Scenario: User takes Sensitivity and Redness Quiz
    Given Open Home page
    When Choose Get My Formula
    When Introductory message disappear
    When Choose Sensitivity and Redness concerns
    When Click Next
    When Provide User name Ana