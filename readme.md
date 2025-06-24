# ZAGREBALLER

ZagreBaller is the ultimate app for futsal enthusiasts. Connect with players, organize games, and join local futsal events. Find your team, challenge opponents, and play the game you love with ease!

![](readme/mockup.png)

## PROJECT IDEA AND TARGET

Project idea is to create an online platform dedicated to connecting futsal players, enabling them to organize games, join local events, and engage with a community of like-minded sports enthusiasts. It aims to simplify the process of finding futsal players and venues, fostering better access to recreational and competitive futsal opportunities. In addition, it serves as a great entry point for newcomers to the city to quickly find teams. Idea is based on a real need in my city and I'm proud to say it resulted in connecting a young Korean group to their first game even during research phase! Information gathered was organized into user stories with a noticed strong notion that the system needs to be fast and simple with no elaborate social media-like features.

<br>

## User Stories

### Epic: User profile management
<details>
  <summary>view stories</summary><br>

**User story 1: User account creation and login**  
As a new user, I want to create an account and log in to the platform, so that I can access my personal player profile and interact with the community.

**ACCEPTANCE CRITERIA:**
- A sign-up page where users can create an account with basic information (name, email, password).
- A login page where existing users can authenticate using their credentials.
---

**User story 2: View and edit player profile**  
As a logged-in user, I want to view and edit my personal player profile, so that new people can know my basic information

**ACCEPTANCE CRITERIA:**
- A user profile page that displays basic player information
- The ability to update personal information such as email, profile picture
- The ability to save changes after updating the profile.

---
</details>

### Epic: Game management
<details>
  <summary>view stories</summary><br>

**User story 3: Create a game**  
As a user, I want to create a game with specific details (date, time, location, team size), so that I can invite others to join and organize futsal games.

**ACCEPTANCE CRITERIA:**
- A game creation form that allows the user to input relevant details
- The ability to set the number of players required for each team and total players.

---

**User story 4: Join an existing game**  
As a user, I want to browse available games and join one, so that I can participate in futsal games in my area.

**ACCEPTANCE CRITERIA:**
- A list of available games
- The ability to join a game with a simple click, showing confirmation of the action.
- A notification or confirmation message once the user has successfully joined a game.

---

**User story 5: Update a game**  
As a game creator, I want to edit the game details, so that I can adjust the game to reflect any changes.

**ACCEPTANCE CRITERIA:**
- A functionality that allows the game creator to update existing game details.

---

**User story 6: Delete a game**  
As a game creator, I want to delete a game I created, so that it is removed from the platform if necessary.

**ACCEPTANCE CRITERIA:**
- An option for the game creator to delete the game.
- A confirmation prompt before the game is deleted to avoid accidental deletions.

---
</details>

### Epic: Communication & messaging
<details>
  <summary>view stories</summary><br>

**User story 7: In-game messaging system**  
As a user who joined a game, I want to send and receive messages within the game group, so that I can communicate with other players for additional information (e.g., changes, meeting points).

**ACCEPTANCE CRITERIA:**
- A messaging feature available for users who joined the same game.
- Immediately see added message or that it was removed.

---
</details>

### Epic: Game instance management
<details>
  <summary>view stories</summary><br>

**User story 8: View game details**  
As a user, I want to view the game details, so that I can know where and when the game is happening.

**ACCEPTANCE CRITERIA:**
- A detailed game instance page displaying all relevant information (date, time, playing field, location, team size).
- The option to join or leave the game from the game details page.

---

**User story 9: Track joined games**  
As a user, I want to see all the games I have joined or created, so that I can keep track of my upcoming games and activities.

**ACCEPTANCE CRITERIA:**
- A list of all games user is a part of
- A clear distinction between games the user has joined and games they have created.
</details>


<br>

## Agile Development

Project followed Agile methodology throughout development. Core practices included:

- **Iterative Planning**: Development began with user stories based on real-life interviews and observed needs in the local futsal community, forming the core of the MVP.

- **Sprint-Based Progress**: Work was structured into short, focused sprints—each targeting key deliverables such as game creation, authentication, or messaging—allowing for incremental feature delivery and visible progress.

- **Prioritization (MoSCoW Method)**: Features were prioritized using the MoSCoW method (Must have, Should have, Could have, Won’t have for now), ensuring the MVP was both functional and lean. "Must have" items included core gameplay features like joining and creating games, while less critical elements like player rankings were deferred.

- **Retrospectives**: Each development cycle concluded with a reflection on what worked, what didn’t, and what could be improved—leading to ongoing UX and workflow enhancements, especially on mobile.

### GitHub Agile Workflow

The project’s Agile development was managed using GitHub Projects, Issues, and Milestones to ensure transparent and organized progress tracking.

- **Project Board Structure:**  
  The Kanban board is grouped by parent issues called **Epics**, each representing a broad feature area. Under each Epic, sub-issues represent individual **User Stories** (in the MVP milestone) or specific **Tasks** (in the Revision and Documentation milestones).

- **Milestones:**  
  - **MVP:** Contains all user stories necessary for the Minimum Viable Product, as outlined in this README.  
  - **Revision:** Focuses on thorough testing, documenting test results, creating issues for bugs or improvements, and resolving them. Issues here are prioritized using the MoSCoW method with labels.  
  - **Documentation:** Divided into two Epics — one for building `TESTING.md` (completed) and another for creating and refining this `README.md`.

- **Issue Prioritization:**  
  The MoSCoW method was applied to prioritize tasks and features across milestones, ensuring focus on essential functionality before moving to enhancements.

Below is a snapshot of the project Kanban board grouped by Epics and sliced by milestones:

<img src="./readme/gitHub_project_example.png" width="1000" />

<br>

## UX DESIGN

### Logic behind choices

Following the notion of making a simple, fast and direct system and realizing most players would be using phones to browse and join I've decided to organize games into cards and display them below each other with larger screens utilizing extra width to display them in rows. Easy with flexbox! Information shown will contain date, time, name of the arena, CITY BLOCK of the arena as newcomers to city would love to see that. It's followed by total players and a number of open spots. The crucial information and nothing more! On touching one of the cards extra information is shown and functionality to join displayed with a link to exact google maps location available. Forms for inputting data are simple, mobile-friendly, choice based and pre-filled with most popular options (like the date being today or team size of 6). Theme is to be vibrant background and darker elements with light text. Honestly because i personally like it. :)

### Wireframes

Created wireframes display general idea with a sidemenu for smaller screens and multiple columns display for larger screens

- Browsing games

<img src="readme/wireframes/browse_page.png" width="750"/>

<br>

- Creating game

<img src="readme/wireframes/create_edit_game.png" width="750"/>

<br>

- Game details after joining game

<img src="readme/wireframes/game_detail.png" width="750"/>

<br>

- Collapsable menu on mobile

<p float="left">
  <img src="readme/wireframes/mobile_browse.png" height="600" style="margin-right:10px;">
  <img src="./readme/wireframes/mobile_menu_open.png" height="600"/>
</p>


### Background and card images
AI was used to generate background images and Coolors website to match colors to it. Links in credits section

<img src="static/assets/images/bg-big.webp" width="350" height="620"><img src="static/assets/images/simple-background.webp" width="350" height="620">

<br>

## Features

### Landing for the first time - browse and sidebar features

The first thing you see when seeing the page first time is available game list. This is with intention to let you see you can join a game and how clear the information is! What you have is a BROWSING feature that lists all available games sorted by start date.

<details>
  <summary>View Features</summary><br>

![](readme/features/01-browse.png)

On mobile devices you will see a collapsable sidebar-type menu and larger screens will have it on full time. Includes a neat sliding animation as well

![](readme/features/02-colapse-on.png)
![](readme/features/03-collapsed-off.png)

In addition to having a clear instruction to login on the sidebar, any further actions you take will lead to the next feature

</details>

### Login and info-message features

To use the website you need to be a user and login so it's only natural to have a pretty theme-fitting login menu. It also doubles as access to signup menu

<details>
  <summary>View Features</summary><br>


![](readme/features/04-appropriate-message-and-login.png)

In case you're coming from other places on website you'll already be introduced to the info-message feature like above. It pops up on top of the screen and let's you know what happened. It is persistent and consistent throughout the entire app.

</details>

### Signup

Now you realized you need to signup, so let's do that, it's super simple and fast just like research says players want it. You will get reacquainted with message-info feature if anything is going wrongly here.

<details>
  <summary>View Features</summary><br>

![](readme/features/05-signup-and-checks.png)

</details>

### Navigation and logout features

After signing up and logging in you will see the true usability of the sidebar feature as a navigational element and indicator if you're logged in. It also has a self-explanatory logout feature

<details>
  <summary>View Features</summary><br>

![](readme/features/06-logged-in-menu.png)

</details>

### User profile edit

You can use the sidebar to now access this feature. Simple and easy form allows you to add your name, email and date of birth and also choose your profile picture.

<details>
  <summary>View Features</summary><br>

![](readme/features/07-user-profile-checks-reset.png)

Trying to save the changes brings us to the next feature

</details>

### Confirmation dialog

Every action on the site that has a significant effect on your experience or affects other users will be prevented from happening on accident by this simple but effective dialogue

<details>
  <summary>View Features</summary><br>

![](readme/features/08-confirmation-dialog.jpg)

</details>

### Game card

Your info is fully set up! Let's look at some games - unless you're already there of course, this is enabled on purpose for speed. What you see is a game card showing you exactly the information you need to know and nothing more or less.

<details>
  <summary>View Features</summary><br>

![](readme/features/08-game-card.png)

It also acts as a link to see game details and possibly join the game

</details>

### Detail and joining game features

This card has the same structure as the original game card but gives you extra information, creator's notes and even a link to exact game arena location on google maps. Those pins are set at the door coordinates. It also allows you to join a game

<details>
  <summary>View Features</summary><br>

![](readme/features/09-detail-and-join.png)

Joining the game is super easy, just click on the obvious button and confirm it with the dialogue feature

</details>

### Messages

Upon joining access to messages related to this game is available. Feature includes the ability to add or remove your own messages for any questions or discussions prior to game start. Connect with the creator!

<details>
  <summary>View Features</summary><br>

![](readme/features/11-communication.png)

</details>

### Leaving game

Detailed display will also allow you to leave the game (with confirmation of course)

<details>
  <summary>View Features</summary><br>

![](readme/features/10.feature-leave.png)

</details>

### Create game

Since you know that one isn't for you let's create one with you and your friends. On the navigation go to create game and you'll get this super simple form to use

<details>
  <summary>View Features</summary><br>

![](readme/features/12-create-game.png)

All fields are pre-filled with ready options so if you're starting a 6v6 game today from 18-19h and need 3 more players (not caring about ages at all), simply select the location from drop-down list and click create. Confirm with dialogue and you're done! Doesn't get faster than that. In case you'd like to change it a bit - all options are selectable and you can even add additional information.

</details>

### Edit game

After creating a game you'll end up in it's detailed view just to be sure everything is fine and here you'll see that it now offers you edit and delete options.

<details>
  <summary>View Features</summary><br>

![](readme/features/13-edit-delete.png)

Realizing you'll actually be starting an hour later than shown, you click on edit button and end up in the good old game creation form with all your previous data pre-filled, ready to be changed to correct and a "save changes" button just to be sure we're not creating a different game. Confirm the action and you're done.

![](readme/features/14-edit.png)

</details>

### Delete game

Now you're back in newly edited game's detailed view and have the option to delete it since three of your friends cancelled and you don't feel like looking for 6 more players in the next 40 minutes. No problem, just use the delete button, confirm the action and you're done. Start looking for players earlier next time :)

<details>
  <summary>View Features</summary><br>

</details>

### My games

Ther is one more option on the sidebar after you've created next week's games and left for the day. It's waiting for your return and readily shows you all the games you've created and joined to easily organize yourself. My games gives you exactly this.

<details>
  <summary>View Features</summary><br>

![](readme/features/15-my-games.png)

</details>

<br>

## Data Model

- **FutsalGame** is the core model representing a scheduled futsal match, including essential details such as the number of players needed, team sizes, and the date and time of the game.  
- **Player** represents a user participating in the system, either by joining or creating games. It stores personal information and is linked to the authentication system.  
- There is a **many-to-many relationship** between *FutsalGame* and *Player* to allow multiple players to join multiple games, and each game to include multiple players.  
- Additionally, *FutsalGame* and *Player* have a **one-to-many relationship** representing game creation: one player can create many games, but each game has only one creator.  
- **FutsalField** represents the physical location where games are held, including venue details and geographic information.  
- *FutsalField* and *FutsalGame* share a **one-to-many relationship**: a single game takes place at one location, but a venue can host multiple games over time.  
- **CommentModel** captures user comments related to game communication.  
- *CommentModel* has a **many-to-one relationship** with both *FutsalGame* and *Player*, meaning each comment is authored by a single player and belongs to one game, while players can create many comments across different games.  

Please see the diagram below for a detailed visual representation:

![](readme/database-model.jpg)

<br>

## Data Security

ZagreBaller follows standard Django security practices to protect user data and application integrity. Key security measures include:

- **Secret Management**: Sensitive information such as Django's secret key and API keys are stored securely in an `env.py` file and injected into environment variables. This ensures that no secrets are hard-coded or exposed in the codebase.

- **Deployment Security**: The application is deployed on Heroku, which provides a secure platform with HTTPS enabled by default to ensure encrypted communication between users and the server.

- **Debugging Mode**: Debugging mode is explicitly disabled (`DEBUG = False`) in the production environment to prevent exposure of sensitive debugging information.

- **Authentication**: Django’s built-in authentication system manages user login securely, handling password hashing and session management.

While no additional custom security features were implemented, the project benefits from Django’s mature security framework and the security infrastructure provided by Heroku.

<br>

## Testing

Comprehensive testing was performed throughout the project. For detailed testing procedures and results, please see the [TESTING.md](./TESTING.md) file.

<br>

## Credits and Acknowledgments

- The custom Django user model was initially based on code from this helpful tutorial, which I later adapted to fit my needs: [Django Custom User Model Tutorial](https://learndjango.com/tutorials/django-custom-user-model)  
- The combined login/signup form design was inspired by this source, and I extended its style to other page elements after customization: [Login/Registration Form Source](https://www.codingnepalweb.com/create-login-registration-form-html-css/)  
- All images were generated using the AI tool [Leonardo AI](https://app.leonardo.ai/)  
- For managing and troubleshooting database interactions, especially running direct SQL queries with Django, I relied on the database tool [DBeaver](https://dbeaver.io/)  
- To refresh and research HTML/CSS concepts, I frequently consulted [W3Schools](https://www.w3schools.com/) and the [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS)  
- The most comprehensive and invaluable resource throughout development was the [official Django documentation](https://docs.djangoproject.com/en/5.1/)  
- I used [ChatGPT](https://chatgpt.com/) to generate generic user stories at the start of the project, which significantly influenced the design and development approach
- Also, [ChatGPT](https://chatgpt.com/) to convert spreadsheed data into markdown format copied directly to TESTING.md saving enormous amount of time   
- After selecting the background images, the color palette was carefully chosen using [Coolors](https://coolors.co/c2efb3-97abb1-746f72-735f3d-594a26)  
- AI-generated images were optimized and converted to .webp format with the help of [FreeConvert](https://www.freeconvert.com/)
- The [Y Sheet App](https://app.ysheet.com/) was used to organize and manage all development and testing data efficiently  
- Email functionality for password recovery was implemented using [SendGrid](https://app.sendgrid.com/)  
- To learn and follow Python docstring standards, I referred to [PEP 257](https://peps.python.org/pep-0257/)