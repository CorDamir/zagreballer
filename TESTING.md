# TESTING

## Manual testing details

<details>
<summary>Log In / Sign Up Forms</summary><br>

| Test Case                                         | Expected Outcome                                               | Result       |
|--------------------------------------------------|----------------------------------------------------------------|--------------|
| Attempt sign up with empty email field            | Message to fill in field displayed                             | As expected  |
| Attempt sign up with improper email format        | Message to include "@" symbol displayed                        | As expected  |
| Attempt sign up with empty username field         | Message to fill in field displayed                             | As expected  |
| Attempt sign up with 1-2 characters in username   | Message that username must be 3-15 characters displayed       | As expected  |
| Attempt sign up with more than 15 characters username | Message that username must be 3-15 characters displayed    | As expected  |
| Attempt sign up with empty password field         | Message to fill in field displayed                             | As expected  |
| Attempt sign up with "123" as password             | Message that password is too short and common displayed, also message that it’s numeric | As expected  |
| Attempt sign up with 7 character password          | Message that password is too short displayed                  | As expected  |
| Attempt sign up with password and confirmation mismatch | Message that passwords do not match displayed             | As expected  |
| Attempt sign up with password similar to username  | Message that password is too similar to username displayed   | As expected  |
| Attempt sign up with empty password confirmation   | Message to fill in field displayed                             | As expected  |
| Click on "Log in" link                             | Redirected to log in form                                       | As expected  |
| Attempt sign up with valid data                    | Sign up completes, message displayed, redirected to log in form | As expected  |
| Attempt log in with empty username field           | Message to fill in field displayed                             | As expected  |
| Attempt log in with empty password field           | Message to fill in field displayed                             | As expected  |
| Attempt log in with unregistered username          | Login failed message displayed                                | As expected  |
| Attempt log in with incorrect password             | Login failed message displayed                                | As expected  |
| Click on forgot password link                       | Redirected to password recovery page                          | Error: Link not working, no action |
| Click on "Sign up" link                             | Redirected to sign up form                                     | As expected  |
| Attempt log in with valid data                      | Log in successful, message displayed, redirected to browse games page, navigation available | As expected  |

</details><br>

<details>
<summary>Forgotten Password Functionality</summary><br>

| Test Case                                         | Expected Outcome                                               | Result       |
|--------------------------------------------------|----------------------------------------------------------------|--------------|
| Click "Log in" link on reset password page        | Redirected to log in page                                      | As expected  |
| Attempt empty input                                | Disallowed, message displayed                                  | As expected  |
| Attempt invalid input                              | Disallowed, message displayed                                  | As expected  |
| Input valid email and send reset link             | Email sent and received at given address                       | As expected  |
| On successful reset link sent, click back to login | Redirected to login page                                      | As expected  |
| Use link received in email                         | Password reset form opens                                      | As expected  |
| Attempt empty input                                | Disallowed, message displayed                                  | As expected  |
| Attempt invalid inputs                             | Password validation used, messages displayed                  | As expected  |
| Attempt mismatching inputs                         | Disallowed, passwords do not match message displayed          | As expected  |
| Attempt valid inputs                               | Redirected to completion page                                 | As expected  |
| Click log in link on completion page               | Redirected to log in page                                      | As expected  |
| Attempt log in with new password                   | Password changed, login successful                             | As expected  |
| Use invalid reset link                             | Disallowed, message displayed, redirect link provided         | As expected  |
| Click request new reset link                       | Redirected to forgotten password form                         | As expected  |

</details><br>

<details>
<summary>Game Browsing Page</summary><br>

| Test Case                                         | Expected Outcome                                               | Result       |
|--------------------------------------------------|----------------------------------------------------------------|--------------|
| Create five games and visit browsing page logged out | Five game cards displayed                                     | As expected  |
| Create five games and visit browsing page logged in as different user | Five game cards displayed                                | As expected  |
| Setup: two finished and three upcoming games in DB, visit browsing page | Only upcoming games shown                                    | Error: all games showing |
| Setup: create two games and visit page            | Games created by user not shown                               | Error: all games showing |
| Click on game card                                | Redirected to game detail page                                | As expected  |

</details><br>

<details>
<summary>Navigation</summary><br>

| Test Case                                         | Expected Outcome                                               | Result       |
|--------------------------------------------------|----------------------------------------------------------------|--------------|
| Click "Browse games" link                          | Redirected to available games page                            | As expected  |
| Click "My profile" link                            | Redirected to personal profile page                           | As expected  |
| Click "My games" link                             | Redirected to user dashboard page                             | As expected  |
| Click "Create new game" link                      | Redirected to game creation page                              | As expected  |
| Click "Logout" link                               | User logged out, message displayed                            | As expected  |
| Resize window to < 768px width                    | Side menu collapses left with animation, toggle button appears | As expected  |
| Click menu toggle button (collapsed menu)        | Side menu slides open with animation, toggle button toggles  | As expected  |
| Click menu toggle button (open menu)              | Side menu slides closed with animation, toggle button toggles | As expected  |
| Resize back to > 768px                            | Side menu opens, toggle button disappears                     | As expected  |

</details><br>

<details>
<summary>User Dashboard (My Games) Page</summary><br>

| Test Case                                         | Expected Outcome                                               | Result       |
|--------------------------------------------------|----------------------------------------------------------------|--------------|
| Create games and visit dashboard                   | User’s created games displayed                                 | As expected  |
| Click on game card                                 | Redirected to game detail page                                | As expected  |
| Click "Edit" button                               | Game edit form opens with pre-filled data                      | As expected  |
| Input valid changes and save                       | Changes saved and reflected                                    | As expected  |
| Click "Delete" button                             | Confirmation requested, game deleted on confirmation          | As expected  |

</details><br>

<details>
<summary>Create Game Page</summary><br>

| Test Case                                         | Expected Outcome                                               | Result       |
|--------------------------------------------------|----------------------------------------------------------------|--------------|
| Attempt game creation without selecting sports hall | Message to select sports hall displayed                       | As expected  |
| Attempt game creation with date in the past       | Message to select today's or future date displayed            | As expected  |
| Attempt game creation today with time in the past | Message to select future time displayed                        | Error: game successfully created |
| Attempt game creation with preferred age range min > max | Message to select appropriate age range displayed          | Error: game successfully created |
| Attempt game creation with more players needed than total players | Message about required players overshoot displayed          | Error: game successfully created |
| Attempt game creation with proper input            | Game created, redirected to game detail page                   | As expected  |

</details><br>

<details>
<summary>Game Detail Page</summary><br>

| Test Case                                         | Expected Outcome                                               | Result       |
|--------------------------------------------------|----------------------------------------------------------------|--------------|
| User logged in, not joined the game               | Game details displayed, communication section hidden, join button present | As expected  |
| User logged in, attempt to join with open spots   | Game joined, communication section displayed, leave button present | As expected  |
| User logged in, attempt to join no spots left     | Message that you can't join full games displayed               | As expected  |
| User not logged in, attempt to join                | Message to log in displayed, redirected to login page          | As expected  |
| Click map directions link                          | Google maps opens with precise sports hall location            | As expected  |
| Attempt to add empty comment                       | Message to type a comment displayed                             | As expected  |
| Attempt to add comment                             | Comment added, immediately visible                              | As expected  |
| Setup: comments from multiple users not current user | Comments visible, delete button not present                   | As expected  |
| Setup: comments from current user                  | Comments visible, delete buttons present                        | As expected  |
| Attempt to remove own comment                      | Button works, comment removed, change immediately visible      | As expected  |
| User logged in and joined game, click leave button | User unjoined, communication section hidden, join button present | As expected  |
| Setup: 3 more players needed                        | Open spots calculated and displayed correctly                  | As expected  |
| Setup: 2 more players needed, user joins            | Open spots adjusted correctly                                   | As expected  |

</details><br>

<details>
<summary>User Profile Page</summary><br>

| Test Case                                         | Expected Outcome                                               | Result       |
|--------------------------------------------------|----------------------------------------------------------------|--------------|
| Change picture and save                            | Changes saved message displayed, picture updated               | As expected  |
| Change first name and save                         | Changes saved message displayed                                 | As expected  |
| Change last name and save                          | Changes saved message displayed                                 | As expected  |
| Change e-mail and save                             | Changes saved message displayed                                 | As expected  |
| Change date of birth and save                      | Changes saved message displayed                                 | As expected  |
| Save with empty first name field                   | Message to fill in field displayed                              | Error: server 500 |
| Save with empty last name field                    | Message to fill in field displayed                              | Error: server 500 |
| Save with empty e-mail field                       | Message to fill in field displayed                              | Error: server 500 |
| Delete date of birth entry and save                | Message to fill in field displayed                              | Error: server 500 |
| Attempt to upload non-image file as profile picture | Message to use image file displayed                            | Error: server 500 |
| Edit fields then press reset button                | All fields revert to state before changes                       | As expected  |

</details><br>

<details>
<summary>Edit and Delete Game Functionality</summary><br>

| Test Case                                         | Expected Outcome                                               | Result       |
|--------------------------------------------------|----------------------------------------------------------------|--------------|
| Click edit game button                             | Game creation form opens with data pre-filled, button labeled "Save Changes" | Error: Date, start time, and duration not pre-filled |
| Input desired information and save changes        | Game details updated                                          | As expected  |
| Input invalid data (past time, invalid age range) | Change prevented by validation                               | Error: invalid data saved |
| Change needed players from 5 to 3 when 4 players joined | Change prevented, message displayed, input remains          | Error: invalid data saved |
| Click delete button                                | After confirmation, game deleted from database               | As expected  |

</details><br>

## 🛠️ Issue Tracking & Fixes
<detail>

| Section                        | Issue Description                                                                 | Cause / Diagnosis                                            | Fix / Resolution Summary                                                                         |
|-------------------------------|-----------------------------------------------------------------------------------|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| Log In / Sign Up Forms        | Forgot password link not working                                                 | Feature not implemented                          | Feature implemented using django builtin smtp and sendgrid                                                     |
| Game Browsing Page            | All games showing (should show only upcoming)                                    | Filtering not applied                                        | Added filtering to current time + 1 hour                                                              |
| Game Browsing Page            | Own games visible in browse page (should be excluded)                            | Missing exclusion logic for user-created games               | Added exclusion where logged user is game creator                                                                           |
| Create Game Page              | Allows past time, invalid age range, or too many needed players                  | No validation on those fields                                | Added code to handle all issues                         |
| Game Edit Page                | Fields not pre-filled when editing a game                                        | Initial values not set in form context                       | Refactored code from game creation into functions and put them to use in edit view                                        |
| Game Edit Page                | Edit not rendering page (possibly 500 error)                                     | `else` statement wrongly left during refactor                | Removed unnecessary `else` from `edit_game` view                                                   |
| Game Edit Page                | Edit allowed invalid player count (e.g. fewer needed than already joined)        | Validation missing                                            | Added `if` check to handle joined players during edits                                        |
| User Profile Page             | Server 500 when saving with empty required fields or invalid image               | Missing form validation                                      | Used `clean_image` method in cloudinary form for validation, empty first name and username were intended and error was temporary heroku issue, changed email input field type to email from text                                             |
| User Profile Page             | Uploading non-image file causes server error                                     | No file type check                                            | See above                                                                                      |
| Create Game Page              | HTML validation issue with empty meta tag                                        | Empty meta tag present                                       | Removed empty `<meta>` from index.html                                                        |
| Game Pages (Multiple Buttons) | Some modal buttons don’t work                                                    | JS logic didn’t distinguish properly between buttons          | Improved `displayConfirmationModal()` logic using proper `if-else`                            |
| Game Edit / Create            | HTML validation issue with incorrect semantic tag                                | Improper use of `<section>` where `<div>` is expected        | Replaced `<section>` with `<div>`                                                             |

