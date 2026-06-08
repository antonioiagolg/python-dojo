# Float detector

* This was quite simple, first I just did the float parsing, id if any error captured, I printed False. But there was an edge case;

* Numbers without "." were parsing normally, but for the requisite of the challenge they should be false. Then I added a check with module re. If the "." not in the input string, just print False and continue.

* Another approach would be to use "in" operator, which is faster than the regular expression approach (the script took 19 milliseconds to perform this operation using "in", and 28 milliseconds using the re package, I thought it would be less. Test in conpiled languages, in my case I used Odin, took 1.89 milliseconds).
