# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  

enter number in guess input, but it doesn't work, just need to use submit button
have to enter another number to see in history, not after submitted it.
when all the way to 100 still say go higher, did 101 go lower, so answer is broken some how.
history did go past 5 entry logs
the go higher and go lower are pointing opposite directions
hard and normal has their ranges mixed up

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| enter 60 | the enter button for entering guess input submiting the button   | the enter button for entering guess input does nothing | nothing happens. |
| click "New Game" | to reset the page, to do a new game | clicking the button nothing happens | nothing happens. |
| enter 60 after a fifth attempt | to see the entry in the history,  | after a fifth attempt, no entry is seen in the history | error only partially works |


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

I did ask for solutions to three of my problems
it did give good solution for 'new game' button and for displaying the history of entries correctly. 
but it did give good explaintions for for how to fix the submit button and entering the button, so I had to ask again
for more clear examples. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

It did give me good solutions to problems I asked about except for ones I needed to clarify or find the code to ask about specifically.
And it did not fix the hints problem, had to go back and fix it. and asking for more solutions once to a specific description of hint problem that 
Summary of what changed:
1. logic_utils.py — filled in the stub with the real, fixed logic: get_range_for_difficulty, parse_guess, update_score unchanged in behavior; check_guess now returns just the outcome string ("Win"/"Too High"/"Too Low") to match what the starter tests expect, with a new get_hint_message(outcome) helper supplying the emoji text.
2. app.py — removed the duplicated function definitions and now does from logic_utils import ...; updated the one call site (outcome = check_guess(...) + get_hint_message(outcome)) to match the new signature.
3. tests/test_game_logic.py — added two regression tests pinning down the exact bug you asked about: check_guess(9, 10) == "Too Low" and check_guess(100, 99) == "Too High". Both cross a digit-length boundary, so if the string-comparison bug were ever reintroduced, these would fail immediately (lexicographically "9" > "10" and "99" > "100", which is wrong numerically).
All 5 tests pass, and both files still compile cleanly.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit needs to be restarted after code updates/changes, so the reruns are needed.
Also, it could imported/downloaded to run locally, and has website guides in theq learn more.


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

 I would reuse the way to write prompts to give options for me to decide which is the best option for me
 And for improvements I think I would ask about a bug one at a time, instead of one at a time.
 I can see how AI options can be useful, and explaining things in a section that I know is wrong to give a deeper understanding.

