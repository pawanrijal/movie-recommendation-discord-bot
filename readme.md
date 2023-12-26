# Movie Recommendation Discord Bot

## Overview

This Discord bot provides movie recommendations based on genres. Users can interact with the bot to get personalized movie suggestions.

## Features

- Dynamic genre mapping from TMDb API.
- Random movie recommendations based on user-specified genres.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- Discord API token for your bot
- TMDb API key

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/movie-recommendation-bot.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your Discord bot token and TMDb API key:

   ```env
   DISCORD_BOT_TOKEN=your_discord_bot_token
   TMDB_API_KEY=your_tmdb_api_key
   ```

## Usage

1. Run the bot:

   ```bash
   python main.py
   ```

2. In Discord, use the `!recommend` command followed by a genre to get a movie recommendation:

   ```bash
   !recommend action
   ```

## Configuration

- The bot's command prefix is set to `!`. You can change this in the code (`command_prefix='!'`) to another character if you prefer.

## Contributing

If you would like to contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Thanks to [Discord.py](https://github.com/Rapptz/discord.py) for the Discord API wrapper.
- Thanks to [TMDb](https://www.themoviedb.org/) for providing movie data.

---

Feel free to modify the content based on your specific project details and preferences. Make sure to include a license file (e.g., `LICENSE.md`) if applicable.
