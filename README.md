# GameBot
Game bot for discord!!

<p align="center">
  <img src="https://github.com/IsabellaSchneider7/GameBot/blob/main/telebot%20logo.JPG" width="500" />
</p>

# Inspiration
We were inspired to make TeleBot as a way to connect with friends during COVID. One game we all enjoy is Telestrations, a mix of the games Telephone and Pictionary. Many similar online games either cost money, require a second device to play, or are on a website that only works well on desktop. We wanted to make a game that was accessible and easy to play. We chose to make a Discord bot that serves as the moderator for the game, collecting player's drawings and guesses.

# What it does
To play Telestrations, players alternate guessing text and drawing. Player 1 inputs a prompt, then Player 2 has to try and draw that prompt. Player 2 passes the drawing to Player 3, who has to guess what the original prompt was based off of the image. Then Player 4 draws whatever Player 3 wrote down, and so on.

Players set up the TeleBot game in their Discord server. The play command produces a message that players can react to to join the game, and then the start command is used to start the game. TeleBot runs the actual gameplay through direct messages. It asks Player 1 for a prompt, then sends their prompt to Player 2, then sends Player 2's subsequent drawing to Player 3, and so on until all players have had their turn.

After the game is over, TeleBot sends the entire "story" to the Discord channel where the game was set up. It also gives the game a score out of 100 based on how close the first and last prompts are. (A higher score means that they were more similar, which means that the players had better communication!) Each player has their total score stored in Firebase, and the score from each game they play is added to it. Players' scores can be retrieved with the scores command.

Other features include a timeout for players' submissions (so that if someone goes AFK the game can still continue) and a random prompt generator (for even numbers of players, so that it always starts and ends on text).

# How we built it
We built TeleBot using Firebase and Python's discord library, apscheduler, and natural language toolkit.

# Challenges we ran into
It was difficult at first to handle reactions to allow players to join the game. This was a new topic for us, so it took some time to figure out. We also ran into challenges when trying to pass images between players and display them correctly at the end of the game. Another challenge that took a lot of figuring out was sharing variables between files in a way that worked but still allowed our code to be organized.

# Accomplishments that we're proud of
We're proud that we built a working Discord bot! We're also proud that we are able to store user's scores and play a complete game. This was a completely new experience for us and the fact that we got the game fully functional in such a short amount of time is a great accomplishment!

# What we learned
We learned about how to set up a Discord bot and the different features available, as well as asynchronous programming in Python. We also learned about using language libraries to compare how similar two sentences are.

# What's next for TeleBot
We would like to add additional games (such as a story game where users each input one sentence) and more game settings to make TeleBot able to suit any server! We would also like to add functionality for running multiple games at once in the same server.
