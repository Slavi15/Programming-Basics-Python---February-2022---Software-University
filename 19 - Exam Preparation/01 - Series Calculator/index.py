import math

series_name = str(input())
seasons = int(input())
episodes = int(input())
ordinary_episode_time = float(input())

ads_time_per_episode = 0.2 * ordinary_episode_time
episode_time_with_ads = ordinary_episode_time + ads_time_per_episode

special_episode_time = seasons * 10

time = (episode_time_with_ads * episodes * seasons) + special_episode_time

print(f"Total time needed to watch the {series_name} series is {math.floor(time)} minutes.")