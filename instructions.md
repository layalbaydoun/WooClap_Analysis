# Data Internship Tech Case - 2026

# Introduction

The goal of this case is to assess your skills as a futur Data Analyst

# Data Internship Tech Case - 2026

# Introduction

The goal of this case is to assess your skills as a futur Data Analyst

At Wooclap, we don't believe in "trick" exercises where you must guess what we want because that does not represent how we work on daily basis. We try to be as explicit as we can regarding what we're looking for in those exercises.

If you have any doubts or questions, feel free to send an email to [victor.ernoult@wooclap.com](mailto:victor.ernoult@wooclap.com) or plan a call to ask for further clarifications, this will not penalize you in any way.

Your completed exercises should be sent at least **one full day** before the restitution meeting to give us time to review them.

For this exercice I recommend you to use python as it will be a part of the internship but you can choose whatever you feel more comfortable with.

# Submission guidelines

You can create private Github repositories for those exercises and add the following people

- Konilo (data analyst): https://github.com/Konilo
- Alexandre (data engineer): https://github.com/alexandre-leonard
- Victor (data analyst): https://github.com/victor-ernoult
- Bérenger (lead data): https://github.com/Berenger-Wooclap
- Joana (data analyst): https://github.com/JoanaDaCosta-wooclap
- Jonathan (CTO): https://github.com/dfdeagle47

Please include a README.md file detailing your name, the steps to run the exercises if relevant and any additional notes you deem important.

Please note that if we feel the quality of the tech case does not match what we’re looking for, we’ll transform the debriefing session into a shorter feedback session.

# Exercises

## Data

[metadata.csv](attachment:de1dd677-d310-405b-95f7-26dc717f163b:metadata.csv)

[sample.csv](attachment:023ed9e1-c751-4cd9-b1ac-f859be6ada86:sample.csv)

## Context

Wooclap is a tool that allows teachers and trainers to easily ask questions (open questions, multiple choice questions, etc.) to an audience of students via their smartphones.

On the Wooclap app, teachers create questions inside what we call **events**. An event is, essentially, a group of questions. Teachers can use the same event multiple times, in different lessons or **sessions** (on different days, or in the morning and afternoon, for example).

The sample you have (`sample.csv`) is a CSV file containing an entry for each answer sent with, among other things, the time at which this answer was sent, and the identifier of the event containing the question (see `metadata.csv` for more information on the content of the `sample.csv` log file).

## Exercise 1: Data formatting

- Create a script to write the CSV dataset in parquet format using a partitioning per day (to allow a better storage in a data lake, for example).

## Exercice 2: Data Exploration

- Make a graph to analyse the distribution of answers over time.
- Based on what you observe, propose a method to identify sessions (no need to implement it but document the methodology).
- Feel free to point out anything you deem of interest in this dataset.

## AI disclosure

We are aware that the use of AI nowadays can be a full-fledged tool that can assist you in completing this technical case.

We are not opposed to the use of this tool if it is helpful to you.

However, if this is the case, we ask that you be transparent about its use when submitting your test. We may ask you questions about your understanding of the answers provided by the AI and also the way you used it.

If you wish, you can also share your LLM session with us, including all your exchanges. This can help us better understand your reasoning and way of working.
