let num = 5;

for (let i = 0; i < num; i++) {
  for (let j = 1; j < i + 1; j++) {
    console.log(" ", (end = " "));
  }
  for (let j = 0; j < num; j++) {
    console.log("*", (end = " "));
  }
  console.log();
}
