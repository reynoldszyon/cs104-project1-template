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
> - 'store'(int): Keeps track of the number of questions the users answer correctly. One score variable makes sence because all of the correct ancswer will contribute to the user's final score.
> - 'answer1'(int): Stores the user's answer to the question about which artist has their own self-titled album. This answer will be used in a condiotnal statement to determine if the user is correct.
> - 'answer2'(int): Stores the user's answer to the question about who released the song "Love on the Brain." This answer will be checked using conditonal logic.
> - 'answer3'(int): Stores the user's answer to the question about who released "Heartbreak Anniversary." This answer will be used to determine wheater the user gets a point.
> - 'answer4'(int): Stores the user's answer to the question about which artist released the album Confessions in 2004. The program will use this answer in a conditonal statement.
> - 'answer5'(int): Stores the user's answer to the question about who released the song "Trip." The program will check this answer using a conditional logic
> - 'name'(str): Stores the user's name so the program can address them why displaying thier quiz results.
> - 'total_questions'(int): Stores the total number of questions in the quiz. This will be used when displaying the user final score, such as "You scored 4 out of 5."

## Conditional Logic Outline
> - **Conditional statement 1** — related to "Which artist has their own self-titled album?"
>   - `if` the response is 3 (Beyoncé): display a correct message and increase `score` by 1.
>   - `else`: display incorrect message and give the correct answer.
>
> - **Conditional statement 2** — related to "Who released the song 'Love on the Brain'?"
>   - `if` the response is 4 (Rihanna): display a correct message and increase `score` by 1.
>   - `else`: display incorrect message and display correct answer.
>
> - **Conditional statement 3** — related to "Which artist released the song 'Heartbreak Anniversary'?"
>   - `if` the response is 2 (Giveon): display a correct message and increase `score` by 1.
>   - `else`: display an incorrect message and encourage the user to try again next time.
>
> - **Conditional statement 4** — related to "Which artist released the album Confessions in 2004?"
>   - `if` the response is 1 (Usher): display a correct message and increase `score` by 1.
>   - `else`: display an incorrect message and display the correct answer.
>
> - **Conditional statement 5** — related to "Who released the song 'Trip'?"
>   - `if` the response is 4 (Ella Mai): display a correct message and increase `score` by 1.
>   - `else`: display an incorrect message and give the correct answer.
>
> - **Conditional statement 6** — reveals final results based on `score`
>   - `if` the score is 5: display a message saying the user has excellent Music Knowledge.
>   - `elif` the score is 3 or 4: display a message saying the user has good Music Knowledge.
>   - `else`: display a message encouraging the user to listen to more music and try again.

## How to Run
1. Clone this repo
2. Run `python3 main.py` or `python main.py`

## Demo Video
(https://www.loom.com/share/cb7b8d06eb8349c19b0765be74e653d4)
