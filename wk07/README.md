# Tutorial 07

## A. Pythonic

Modify [fettucine.py](fettucine.py) to improve it in terms of its adherence to pythonic principles.

## B. Requirements

Your tutor may break you up into groups to complete this activity.

* Q. What are attributes of good requirements?
* Q. How could we clean this up into well described requirements? "I want a burger with lots of pickles and mayo but I need to make sure that the mayo doesn't make the burger bun really wet. Oh, and it needs to be warm, like, made less than 5 minutes ago warm but not so hot that I burn myself. I'm also not a big fan of plastic containers so if it could be in a paper bag that would be good. Actually, make that a brown paper bag, I like the colour of that"

[Google Doc Link](https://docs.google.com/document/d/1HPiraH0Amiu2Du3znVHZE_aM2wfGYOWC2pyaxC371HI/edit?usp=sharing)

## C. User Stories

Consider the core requirements of UNSW Streams:

1. Ability to login, register if not registered, and log out
2. Ability to see a list of channels
3. Ability to create a channel, join a channel, invite someone else to a channel, and leave a channel
4. Within a channel, ability to view all messages, view the members of the channel, and the details of the channel
5. Within a channel, ability to send a message now, or to send a message at a specified time in the future
6. Within a channel, ability to edit, share between channels, remove, pin, unpin, react, or unreact to a message
7. Ability to view anyone's user profile, and modify a user's own profile (name, email, handle, and profile photo)
8. Ability to search for messages based on a search string
9. Ability to modify a user's admin permissions: (MEMBER, OWNER)
10. Ability to send message directly to a user (or group of users) via direct messaging (DM).

Pick **two** of the above and write a series of user stories that encompass each requirement:

* Discuss as a class the potential target audience, and use this as your type of user;
* Write acceptance criteria for each story and discuss when to use Scenario-based and Rule-based acceptance criteria

> For example:
>   (3) Ability to create a channel, join a channel, invite someone else to a channel, and leave a channel
>
>   As a UNSW staff member, I want to be able to create a private channel so that I can communicate with a specific group of colleagues at once
>   * The user can create a private channel with a name
>   * Given that I have conceived a public channel, I can add a series of users as part of its creation
>   * Given that I have created a private channel, when channels are listed then the channel is marked as private
>
>   As a UNSW staff member, I want to be able to create a public channel so that I can be a part of a community of like-minded people
>   * The user can create a public channel with a name
>   * Given that I have conceived a public channel, I can add a series of users as part of its creation
>   * Given that I have created a public channel, when channels are listed then the channel is marked as public
>
>   As a UNSW staff member, I want to be able to join a public channel so that I can meet new people and broaden my perspectives
>   * The user can join any channel that is public
>
>   As a UNSW staff member, I want to be able to invite someone else to a channel so that new members joining my team can also be included in the communication
>   * Given I am a member of a channel, when I invite any user not currently in the channel to join then they become a member of the channel
>
>   As a UNSW staff member, I want to be able to leave a channel so that when I move into different teams I am not receiving irrelevant messages
>   * Given that I am a member of a channel, when I leave the channel I no longer receive messages from it



## D. Use Cases

Pick **one** of the above requirements you have written stories for and write a use case for the flow of interaction.

> Use Case: Become part of a channel
> Goal in context: N/A
> Scope: UNSW Streams
> Level: Primary Task
> Preconditions: The user has registered an account and is logged in
> Success End Condition: The user can join and send a message to a channel
> Failed End Condition: The user cannot join and send a message to a channel
> Primary Actor: User
> Trigger: User selects option to join a channel, OR user is invited to a channel

> Success Scenario 1
> 1. User selects option to join a public channel
> 2. UNSW Streams displays all messages sent in the channel
> 3. UNSW Streams lists user as a member of the channel
> 4. User sends a message to the channel
> 5. UNSW Streams displays the sent message

> Success Scenario 1
> 1. User is invited by another user to join a public/private channel
> 2. UNSW Streams displays all messages sent in the channel
> 3. UNSW Streams lists user as a member of the channel
> 4. User sends a message to the channel
> 5. UNSW Streams displays the sent message


## E. Design Principles

A simple piece of code [box.py](box.py) that generates an ASCII box has been provided. What are possible code smells with this code? How would you refactor it to be more consistent with basic software engineering design principles?
