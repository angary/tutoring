/**
 * A program to print out the values of a shopping list
 */

const shoppingList = ["apples", "oranges", "pears"];

/**
 * For loop method, quite a bit going on
 * 
 * Pros:
 * - can use `break` and `continue`
 * 
 * Cons:
 * - verbose
 * - can have small errors with loop conditions
 */
for (let i = 0; i < 3; i++) {
  console.log(shoppingList[i]);
}

/**
 * Const of loop, is cleaner, but you don't have access to the
 * current index
 * 
 * Pros:
 * - short and succinct
 * - can use `break` and `continue`
 * 
 * Cons:
 * - does not have access to index
 */
for (const item of shoppingList) {
  console.log(item);
}

/**
 * forEach method, forEach is a function that takes in a
 * function which takes in a item of the list and the index,
 * and then applies that function to each item and index
 * of the list
 * 
 * Pros:
 * - short and succinct
 * - have access to the item and its index
 * 
 * Cons:
 * - cannot use break / continue
 */
shoppingList.forEach((item, index) => {
  console.log(item);
});


