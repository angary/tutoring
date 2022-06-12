function stamp(email) {
  return { error: "error" };
}

console.log(stamp("invalid@@email"));
console.log(stamp("valid@email.com"));
