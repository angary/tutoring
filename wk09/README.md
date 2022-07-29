# Tutorial 9

[TOC]

## A. Requirements

### Part 1: Functional vs Non-Functional

- What is the difference between functional and non-functional requirements?
    > **Functional requirements**
    > - specify a specific capability/service that the system should provide.
    > - it's *what* the system does.
    > 
    > **Non-functional requirements**
    > - place a constraint on *how* the system can achieve this.
    > - typically this is a performance characteristic.

- Are the following requirements functional or non-functional?

  1. A website should be capable enough to handle 20 million users without affecting its performance
      > Non-functional 

  1. The background colour for all windows in the application will be blue and have a hexadecimal RGB colour value of 0x0000FF
      > Functional

  1. The Sales system should allow users to record customer sales
      > Functional

  1. The software should be portable. So moving from one Operating System (OS) to another OS will not create any problems.
      > Non-functional

  1. Only managers have the right to view revenue data.
      > Functional

  1. Every unsuccessful attempt by a user to access an item of data shall be recorded on an audit trail.
      > Non-functional (arguable)

  1. Privacy of information, the export of restricted technologies, intellectual property rights, etc. should be audited.
      > Non-functional (arguable)

  1. The software system should be integrated with a banking API
      > Functional (arguable)

> Read more [here](https://www.guru99.com/functional-vs-non-functional-requirements.html).

### Part 2: Good Requirements

Your tutor will break you up into random groups to complete this activity. In 10 minutes, answer the questions below:

1. What are some attributes of good requirements?

   > Testable - you should be able to test if you've met the requirement
   > Non-conflicting - Should take into account the other requirements, non conflicting
   > Specific - Should be clear, vague requirements have more room for error

1. Consider the text below:
   ```
   I want a burger with lots of pickles and mayo but I need to make sure that the mayo doesn't make the burger bun really wet.
   Oh, and it needs to be warm, like, made less than 5 minutes ago warm but not so hot that I burn myself. I'm also not a big
   fan of plastic containers so if it could be in a paper bag that would be good. Actually, make that a brown paper bag, I
   like the colour of that
   ```
   How could we clean this up into well-described requirements, from
   1. The Maccas customer to the staff taking the order
      > I want a burger
      >
      > - Lots of pickles and mayo
      > - Dry bun
      > - Warm but not bot
      > - Brown paper bag
   1. The staff taking the order to the kitchen
      > I want a buger
      >
      > - 10 pickles
      > - 10ml of mayo
      > - 50 degrees celsius bun
      > - Brown paper bag

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

User stories:

I as **someone** I want **some feature** because **some reason**

1. As a student I want to have private channels so that I can discuss the group project with my team privately, without other groups seeing.

2. As a uni student I want to be able to make calls on UNSW treats, because it is a more interactive and real time communication method.

- Write acceptance criteria for each story and discuss when to use Scenario-based and Rule-based acceptance criteria

Scenario - based

1. User A clicks on create private channel button
2. User A is then added to the private channel
3. User A sends a message to the private channel
4. User B who is not in the private channel cannot view the message in the channel from User A

Rule - based

- If the user clicks on start call button, everyone in the channel gets a ringing notification, with a green button to accept or a red button to decline the call.
- If the user clicks on the green button, the notification disappears and they join the voice call.
- If the user clicks on the red button, the notification disappears.

## C. Use Cases

Pick **one** of the above requirements you have written stories for and write a use case for the flow of interaction.

> Use Case: Become part of a channel
>
> - Goal in context: A user can become a member of a channel either by their own initiative or by an invitation from another user.
> - Scope: UNSW Streams
> - Level: Primary Task
> - Preconditions: The user has registered an account and is logged in
> - Success End Condition: The user is in the channel and send a messages to the channel
> - Failed End Condition: The user is not in the channel and cannot send messages to the channel
> - Primary Actor: User
> - Trigger: User selects option to join a channel, or user is invited by another user to a channel

> Success Scenario 1
>
> 1. User selects option to join a public channel
> 1. UNSW Streams displays all messages sent in the channel
> 1. UNSW Streams lists user as a member of the channel
> 1. User sends a message to the channel
> 1. UNSW Streams displays the sent message

> Success Scenario 2
>
> 1. User is invited by another user to join a public/private channel
> 1. UNSW Streams displays all messages sent in the channel
> 1. UNSW Streams lists user as a member of the channel
> 1. User sends a message to the channel
> 1. UNSW Streams displays the sent message

## D. Creating Routes

Break into random teams of 3. The only rule is that no one in the team can be a member of your project group.

In your team, you will have 10 minutes to analyse the current API specification for your project, and to (as a team) propose one or more new "route(s)" (i.e. URL) to the interface to add some cool functionality to the product.

Find something that you as a team get excited about. You'll be sharing your answer with the class, and will be expected to provide for each route:

- A route (i.e. /this/URL/name)
- A CRUD method (e.g. GET)
- Input parameters
- Return object
- Description of what it does

| Name & Description | HTTP Method | Data Types | Exceptions |
| ------------------ | ----------- | ---------- | ---------- |
| `message/sendGif` Send a gif from the authorised user to the channel specified by channelId. Note: Each message should have its own unique ID, i.e. no messages should share an ID with another message, even if that other message is in a different channel.    | `POST`            | `gifUrl`, `token`, `channelId`           | - URL does not go to a GIF / valid GIF file format - Should return error when token or channelID is invalid           |
