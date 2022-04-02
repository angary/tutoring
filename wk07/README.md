# Tutorial 07

## A. Requirements

1. As a class, discuss this question:

>  What are attributes of good requirements?

- **Independent**: Independent of the solution, for example the requirement shouldn't care about how the problem is solved, it just cares that the problem is solved
- **Negotiable**: A story is not a contract.  A story IS an invitation to a conversation.
- **Valuable**: If a story does not have discernable value it should not be done
- **Estimable**: A story has to be able to be estimated or sized so it can be properly prioritized
- **Short**: You don't want the engineers / whoever is implementing to be confused
- **Testable**: You want to be able to test to verify that requirements are met

- Consistent: Requirements shouldn't conflict with other requirements / the information should be consistent
- Appropriately technical: engineers will need diff. requirements compared to managers


1. In project groups, how could we clean this up into well described requirements?

> How could we clean this up into well described requirements? "I want a burger with lots of pickles and mayo but I need to make sure that the mayo doesn't make the burger bun really wet. Oh, and it needs to be warm, like, made less than 5 minutes ago warm but not so hot that I burn myself. I'm also not a big fan of plastic containers so if it could be in a paper bag that would be good. Actually, make that a brown paper bag, I like the colour of that"

* The burger shall contain lots of pickles
* The burger shall contain lots of mayo
* The mayo shall not make the bun wet
* The burger shall be warm
* The burger shall be wrapped in a brown paper bag

[h11b doc](https://docs.google.com/document/d/1P7AFqaCstO46htl1d2H0_W54KHE_HSMbI4J0nbVjtq0/edit?usp=sharing)
[f09b doc](https://docs.google.com/document/d/1XgBpHQQb8WLg8MJgV2PCHl5StlAkdlOK3UNITBHuTc4/edit?usp=sharing)

Think about converting the above paragraph into a list of requirements in the following contexts:
* From the Maccas customer to the staff taking the order
* From the staff taking the order to the kitchen

## B. Elicitation

**This exercise links to [Lab07 - Requirements](https://cgi.cse.unsw.edu.au/~cs1531/redirect/?path=COMP1531/22T1/students/_/lab07_requirements)**.

Complete Part 1 of the lab exercise in pairs, with someone **not** in your project group.

## C. User Stories

As a class, discuss for the major project:
* What is your target audience / persona for this application? Use this as your type of user.

> A student

* What is a User Story? How are they structured?

> A user story is a short description that captures a need from a type of user for some reason

User stories typically have the format:

As a \<type of user> I want to have \<some feature> because \<some reason>.

* What is an Acceptance Criteria? What are the two ways we can write them?
> An acceptance criteria is like a checklist or description of needs from the user to know when the requirement is met

1. **Rule based**
   1. Only users that have joined the private channel can see the messages / send messages in the private channel
   2. Members of the private channel can add others to the private channel
   3. Members who are added to the private channel can see the messages / send messages
2. **Scenario based**
   1. Given that the user is not in the private channel, they cannot see the messages
   2. Given that I type in a name, and I click on the create private channel button, a new private channel will be created

Start work on Part 2 of the lab exercise. You can continue working in your pairs.

## D. Use Cases

As a class, pick a 'flow' of interaction and between the system and user and write a simple Use Case for this flow together.

Feature: Private Channel

As a UNSW student doing a group work course, I want to be able to make a private channel so that I can discuss group work with my teammates without other students seeing.
   1. Only users that have joined the private channel can see the messages / send messages in the private channel
   2. Members of the private channel can add others to the private channel
   3. Members who are added to the private channel can see the messages / send messages
   4. Given that I type in a name, and I click on the create private channel button, a new private channel will be created
   
Then, in your pairs pick a **different** flow and write a Use Case, starting work on Part 3 of the lab exercise.

## E. Pythonic

Modify [fettucine.py](fettucine.py) to improve it in terms of its adherence to pythonic principles.

## F. Design Principles

A simple piece of code [box.py](box.py) that generates an ASCII box has been provided. What are possible code smells with this code? How would you refactor it to be more consistent with basic software engineering design principles?
