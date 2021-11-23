# Tutorial 8

## A. Creating your own routes

In your team, you will be given 5-10 minutes to analyse the current API specification for your project, and to (as a team) propose one (or a couple) of new "route(s)" (i.e. url) to the interface to add some cool functionality to the product. Find something that you as a team get excited about. You'll be sharing your answer with the class, and will be expected to provide for each route:
  * A route (i.e. /this/url/name)
  * A CRUD method (e.g. GET)
  * Input parameters
  * Return object
  * Description of what it does

[Example](https://gist.github.com/angary/e66d9595607fe9856d70ca06f7a5a245)

## B. Functional and Non-Functional

* What is the difference between functional and non functional requirements? (See lecture slides)
  * **Functional**: What we need to do
  * **Non-Functional**: How we have to implement something
* Are the following requirements functional or non functional?
  1. Every unsuccessful attempt by a user to access an item of data shall be recorded on an audit trail.
    > Non functional
  2. Privacy of information, the export of restricted technologies, intellectual property rights, etc. should be audited.
    > Non functional
  3. The software system should be integrated with banking API
    > Functional

## C. ISBN Validator

An ISBN (International Standard Book Number) is a 10 character string assigned to every commercial book before 2007. Each character is a digit between 0 and 9, but the last character might also be 'X'.

<img src='https://blog-cdn.reedsy.com/directories/admin/featured_image/264/a6c86df5fe718614a3c60daa95825b77.jpg' width='200' />

### Part 1

Write a program in [isbn.py](isbn.py) that asks the user for an ISBN (in `main`) and determines whether it is valid or not (in `is_valid()`).

The check for validity goes as follows:
* Multiply each of the first 9 digits by its position. The positions go from 1 to 9.
* Add up the 9 resulting products.
* Divide this sum by 11, and get the remainder, which is a number between 0 and 10.
* If the remainder is 10, the last character should be the letter 'X'. Otherwise, the last character should be the remainder (a single digit).

#### Examples

```txt
What is the ISBN? 1503290565
1503290565 is valid
```

```txt
What is the ISBN? 938007834X
938007834X is valid
```

```txt
What is the ISBN? 2222222224
2222222224 is invalid
```

### Part 2

In [decorator.py](decorator.py) complete the decorator function `ISBNValidator` which calls the `isValid` function from the previous part, and check whether the input is a valid ISBN, if not raise a `ValueError`.

After completing it, open a new terminal and run this command

```bash
$ python3 -m http.server
Serving HTTP on :: port 8000 (http://[::]:8000/) ...
```
HTTP server is a python inbuilt library that you can run by doing `python3 -m http.server` but it only supports GET requests.

Now in a different terminal run your code:

```bash
$ python3 decorator.py
What is the ISBN? 938007834X
Sent ISBN to the publisher!
Printing book <Legend of Hayden>
ISBN: 938007834X
```

You should be able to see some output like this in the other terminal:

```bash
Serving HTTP on :: port 8000 (http://[::]:8000/) ...
::ffff:127.0.0.1 - - [03/Oct/2021 20:16:51] "GET /?isbn=938007834X HTTP/1.1" 200 -
```

If the input ISBN is not valid it will simply print the ISBN is invalid and neither of the functions should run:

```bash
$ python3 decorator.py
What is the ISBN? 2222222224
2222222224 is invalid.
```

with no output in the other terminal.

## D. Property-Based Testing

In `divisors.py`, complete the definition of the function according to its documentation.

A simple test is located in `divisors_test.py`. Consider what property, or properties, this function has and write them as property-based tests.
