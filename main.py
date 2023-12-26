import os
from dotenv import load_dotenv
import requests
import discord
from discord.ext import commands
import random

# Load environment variables from .env file
load_dotenv()

# Access environment variables
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

intents = discord.Intents.default()
intents.messages = True  # Enable the messages intent

bot = commands.Bot(command_prefix='!', intents=intents)

# Function to fetch genre mapping from TMDb
def fetch_genre_mapping():
    url = 'https://api.themoviedb.org/3/genre/movie/list'
    params = {
        'api_key': TMDB_API_KEY,
        'language': 'en-US',
    }
    response = requests.get(url, params=params)
    data = response.json()
    genre_mapping = {}
    if 'genres' in data:
        for genre in data['genres']:
            genre_mapping[genre['name'].lower()] = genre['id']
    return genre_mapping

# Get the genre mapping
genre_mapping = fetch_genre_mapping()

# Function to get movie recommendations based on genre
def get_movie_recommendation(genre_id):
    url = f'https://api.themoviedb.org/3/discover/movie'
    params = {
        'api_key': TMDB_API_KEY,
        'language': 'en-US',
        'sort_by': 'popularity.desc',
        'include_adult': 'false',
        'include_video': 'false',
        'with_genres': genre_id,
    }
    response = requests.get(url, params=params)
    data = response.json()
    if 'results' in data and data['results']:
        movie = random.choice(data['results'])
        return f"{movie['title']} ({movie['release_date'][:4]})"
    else:
        return "No recommendations found for this genre."

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='recommend')
async def recommend_movie(ctx, genre=None):
    if genre is None:
        await ctx.send("Please specify a genre. Usage: `!recommend [genre]`")
        return

    genre_id = genre_mapping.get(genre.lower())
    if genre_id is None:
        await ctx.send("Invalid genre. Available genres: " + ', '.join(genre_mapping.keys()))
        return

    recommended_movie = get_movie_recommendation(genre_id)
    await ctx.send(f"I recommend watching: **{recommended_movie}**")

# Run the bot
bot.run(DISCORD_BOT_TOKEN)
