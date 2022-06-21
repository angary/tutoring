import isEmail from "validator/lib/isEmail.js";
import { v4 as uuidv4 } from "uuid";
import dateFormat from "dateformat";

/**
 * @param {String} email the sample email input
 * @returns error if the email was invalid, else a unique identifier for the
 *          email and the time at which the email was stamped
 */
function stamp(email) {
  if (!isEmail(email)) {
    return { error: "error" };
  }
  const now = new Date();
  return {
    identifier: uuidv4(),
    timeString: dateFormat(now, "dddd - h:MM:ss tt"),
  };
}

console.log(stamp("invalid@@email"));
console.log(stamp("valid@email.com"));
