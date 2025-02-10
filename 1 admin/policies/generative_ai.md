# Generative AI policy

Addition on October 15th: generative AI is allowed only on certain use cases, and only in assignments and take-home exams. Generative AI is not allowed in in-person exams under any circumstances.

Addition on October 15th (afternoon): you cannot use Google Search, as it provides AI suggestions in the answers, either in in-person or take-home exams. You have to use the DuckDuckGo.com search engine.

Addition on October 15th (afternoon): if you use PyCharm, you have to disable AI code completion (see detailed instructions below).

This version: October 15th, 2024.

This guide contains my policy on generative AI. You'll have to read and pledge to abide by this policy to gain access to assignments and exams.

If you do use generative AI in the allowed cases, you should attribute credit in  a comment, e.g. `# generative AI helped me with this`. I will ignore these comments when computing your allowed share of comments.

Using generative AI outside of the explicitly allowed use cases is forbidden, violates the [CBS Honor Code](https://students.business.columbia.edu/office-of-student-affairs/academic-advising-and-student-success/academic-integrity), and I will report suspected instances. Please contact me if you have any questions about this policy.

## Penalties: 50% of your grade

If your submission is flagged for violation of this policy and our assessment concludes that you violated it, it will cost you up to **50 points**, or 50% of the grade on the assignment or exam, whichever is larger.

## Rationale for this policy

The rationale for this strict policy is that I have seen several students use code suggestions from generative AI without understaning them, but hoping it would fix a problem they don't want to deal with. So I decided to ban most of it, to ensure you develop solid foundations, i.e. that "you learn to walk before you run."

I expect you to own and be responsible for all the code you submit. I will hold you accountable to all your submissions and you are not allowed to use the excuse "generative AI told me to do it."

If you do use generative AI, I encourage you to save it in your chat history, so that in the case of an anomaly detection, you can prove that you used it within the confines of this guide.

## You cannot use AI in in-person exams

You must not use generative AI during in-person exams, under any circumstances.

The rest of this document concerns the use of AI in the other assessments, such as assignments and take-home exams.

## You cannot use Google Search or AI search engines, either in in-person or take-home exams

You **cannot use Google Search**. Google rolled out "AI search labs overview", which answers some searches with AI and is against the AI policy.

You **cannot use AI search engines** such as Perplexity AI. These are the same as asking generative AI a question.

Instead, you have to use the **DuckDuckGo.com** search engine, which does not have AI suggestions.  It gives the same results as Google for all your queries.

## You cannot copy-paste code from AI

You must not ask generative AI to write code for you and you must not copy-paste code from generative AI into your submission.

## You cannot use AI code completion

You are not allowed to make use of AI code completion. Some IDEs (Integrated Development Environments) use AI for code completion. For example, VS Code uses Copilot and Google Colab uses Gemini. If your IDE has this, you should turn it off.

On PyCharm, disable AI code completion by visiting the Preferences (Command-, on macOS), searching for completion on the top left search bar, and unchecking these two boxes:

- under "Code completion", disable "Sort completion suggestions based on machine learning"

- under "Inline completion", disable "Enable local Full Line completion suggestions"

See these pictures:

![](../images/pycharm1.png)

![](../images/pycharm2.png)

On Replit.com, disable AI code completion: click on AI at the bottom left, then uncheck "Enable"

![](../images/Replit-turn-off-AI-completion.png)

## You can use automatic (non-AI) code completion

Most IDEs suggest code for you to complete. For example, if you defined a variable `transactions = []`, and later you start typing the same letters, e.g. `tr`, the IDE will propose completing it to `transactions` and you can use the TAB key to accept this suggestion. The IDE does so by maintaining a table of existing variables and functions in the background.

You are allowed to use this feature, as long as it is not based on AI.

## You can use AI to get ideas and code structure

You can use generative AI to generate ideas, for example "How would I structure code to download data, run a regression, and plot the results", as long as you end your prompts with `do not show code` so the AI does not show you any code.

In this case, you should give attribution in a comment, e.g. `# generative AI helped me with this`.

## You can use AI for _some_ help in refactoring your code

You **cannot** copy-paste your code into an AI, ask it to refactor for you, and copy-paste the solution back into your submission.

You can use AI to refactor your code as long as you understand the AI's suggestions and you don't use any code from it.

Here is an example of code refactoring that is allowed. Consider the following code:

```python
if not isinstance(a, float) and not isinstance(a, int) :
    print("Not a number!")
```

This code has repetition of `isinstance(a, ...)` and is not DRY. You can ask generative AI to refactor it. Then you should read the answer and realize that the function can take a tuple as a second argument. You can then edit the function yourself (without copy-pasting), so it becomes this DRYer:

```python
if not isinstance(a, (float, int)) :
    print("Not a number!")
```

In this case, you should give attribution in a comment, e.g. `# generative AI helped me refactor this code`.

## Assessment and penalties

I will inspect and investigate each case of suspected violation of this policy.

Some of our methods are:

- exam monitoring with Proctorio, which records your screen;

- automated code similarity to flag submissions that look similar and may both have used generative AI;

- checking the invisible watermarks on text generated by AI;

- a one-on-one time with me to show me how you would write the solution from scratch, to assess if the AI did it for you;

- an inspection of your search history on generative AI to understand what happened.

- referral to the Office of Student Affairs for further investigation.

Even if somehow you escape detection on the assignments, violating this policy will be a recipe for disaster on the exams, where I will ask questions that generative AI cannot solve.

Don't try to outsmart me. If you cheat, the risks you are taking far exceed the benefits. Don't do it.
