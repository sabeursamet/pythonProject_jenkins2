Feature: Drag & Drop

Scenario: Drag & drop element to target
  Given user is in designed URL
  And two boxes appeared
  When user select "Drag" Box
  And Drop it to "Drop here" box
  Then Dropped text appears
