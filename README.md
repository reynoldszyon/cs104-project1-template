# Knowledge-Based Quiz
> This quiz is based on how well do you know music and its artists.

## Overview
> This program is a music knowledge quiz that will test the users on how well they know music and its artists. Users will answer a series of questions about different artists, songs, and albums. Based on their answers users will earn points for each correct answer, and their final score will determine how well they know music.
>
> For example, if the user answers correctly about which artist released a certain song, they will receive a point. At the end of the quiz, the program will display the usuer's final score and the message based on their results.

## Sample Questions and Responses
> Which artist has her own self-titled album?
> 1. Cardi B
> 2. SZA
> 3. Beyoncé 
> 3. Alicia Keys
>
> Who released the song "Love on the Brain"?
> 1. TLC
> 2. H.E.R.
> 3. Ari Lennox
> 4. Rihanna
>
> Which artist released the song "Heartbreak Anniversary?"
> 1. Danieal Caesar
> 2. Giveon
> 3. Lucky Daye
> 4. Brent Faiyaz
>
> Which artist released the album Confessions in 2004?
> 1. Usher
> 2. Chris Brown
> 3. Trey Songz
> 4. Ne-Yo
>
> Who released the song "Trip"?
> 1. Summer Walker
> 2. Kwn
> 3. Adele
> 4. Ella Mai

## Variables
> **DELETE AND REPLACE ME:** List the variables your program uses. For
> each one, note what it stores and why you structured it that way,
> especially for variables tracking results, explain whether a single
> variable or multiple variables makes sense for your program's logic.
>
> Example:
> - `score` (int): tracks total quiz points. A single variable works here
>   since results are cumulative and only one final score matters.
> - `decade_1920s_points`, `decade_1960s_points`, `decade_1980s_points`
>   (int): separate variables needed since multiple decades can tie for
>   highest score, one combined variable couldn't represent that.
> - `user_choice` (str or int): stores the user's response to a question,
>   compared against expected options to decide which branch of the
>   conditional runs.

## Conditional Logic Outline
> **DELETE AND REPLACE ME:** Outline every conditional statement in your
> program, in the order they appear. For each one, describe it in plain
> language (no code needed): which question/condition it relates to,
> each branch (`if`/`elif`/`else`), the exact condition that triggers
> each branch, the action(s) that happen in each branch, and note any
> nested conditionals and why they're nested.
>
> Example:
> - **Conditional statement 1** — related to "Which of the following
>   painters is an Impressionist? 1-Monet 2-Warhol 3-Rembrandt"
>   - `if` response is 1 (Monet): display congratulatory message,
>     increment `score` by 1
>   - `else`: display incorrect message and explain the correct answer
>
> - **Conditional statement 2** — reveals final results based on `score`
>   - `if` score is 3: display high-knowledge message
>   - `elif` score is 1 or 2: display some-knowledge message
>   - `else`: display message encouraging the user to learn more

## How to Run
1. Clone this repo
2. Run `python3 main.py` or `python main.py`

## Demo Video
[DELETE AND REPLACE ME: link to your 5-minute explanation video]
