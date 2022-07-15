// The message contains characters that are not lower-case letters or spaces
export const findVowels = (message: string) => {
  if (/[^a-z ]/.test(message)) {
    throw new Error(
      "The message contains characters that are not lower-case letters or spaces"
    );
  }
  // Count number of vowels in message
  // const result = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0};
  // for (const char of message) {
  //   if ([..."aeiou"].includes(char)) {
  //     result[char] += 1
  //   }
  // }
  const result = {};
  for (const char of "aeiou") {
    result[char] = (message.match(new RegExp(char, "g")) || []).length;
  }
  return result;
};
