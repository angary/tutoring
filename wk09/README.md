# Tutorial 9

[TOC]

## A. Requirements

### Part 1: Functional vs Non-Functional

- What is the difference between functional and non-functional requirements?

- Are the following requirements functional or non-functional?

  1. A website should be capable enough to handle 20 million users without affecting its performance

  1. The background colour for all windows in the application will be blue and have a hexadecimal RGB colour value of 0x0000FF

  1. The Sales system should allow users to record customer sales

  1. The software should be portable. So moving from one Operating System (OS) to another OS will not create any problems.

  1. Only managers have the right to view revenue data.

  1. Every unsuccessful attempt by a user to access an item of data shall be recorded on an audit trail.

  1. Privacy of information, the export of restricted technologies, intellectual property rights, etc. should be audited.

  1. The software system should be integrated with a banking API

### Part 2: Good Requirements
  
Your tutor will break you up into random groups to complete this activity. In 10 minutes, answer the questions below:

1. What are some attributes of good requirements?

1. Consider the text below:
    ```
    I want a burger with lots of pickles and mayo but I need to make sure that the mayo doesn't make the burger bun really wet.
    Oh, and it needs to be warm, like, made less than 5 minutes ago warm but not so hot that I burn myself. I'm also not a big
    fan of plastic containers so if it could be in a paper bag that would be good. Actually, make that a brown paper bag, I
    like the colour of that
    ```
    How could we clean this up into well-described requirements, from
    1. The Maccas customer to the staff taking the order

    1. The staff taking the order to the kitchen

## B. User Stories

Consider the core requirements of UNSW Treats:

Ability to:
1. Register, login and log out
1. See a list of channels
1. Create a channel, join a channel, invite someone else to a channel, and leave a channel
1. Within a channel, view all messages, view the members of the channel, and the details of the channel
1. Within a channel, send a message now, or send a message at a specified time in the future
1. Within a channel, edit, share between channels, remove, pin, unpin, react, or un-react to a message
1. View anyone's user profile, and modify a one's profile (name, email, handle, and profile photo)
1. Search for messages based on a search string
1. Modify a user's admin permissions: (MEMBER, OWNER)
1. Send a message directly to a user (or group of users) via direct messaging (DM).

Pick **one** of the above and write a series of user stories that encompass each requirement:

1. Discuss as a class the potential target audience, and use this as your type of user;
* Write acceptance criteria for each story and discuss when to use Scenario-based and Rule-based acceptance criteria

## C. Use Cases

Pick **one** of the above requirements you have written stories for and write a use case for the flow of interaction.

## D. Creating Routes

Break into random teams of 3. The only rule is that no one in the team can be a member of your project group. 

In your team, you will have 10 minutes to analyse the current API specification for your project, and to (as a team) propose one or more new "route(s)" (i.e. URL) to the interface to add some cool functionality to the product.

Find something that you as a team get excited about. You'll be sharing your answer with the class, and will be expected to provide for each route:
- A route (i.e. /this/URL/name)
- A CRUD method (e.g. GET)
- Input parameters
- Return object
- Description of what it does
