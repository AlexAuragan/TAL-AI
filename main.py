from random import shuffle
from data import generate_urls, parse_url_team, shuffle_team, extract_one_champ, parse_url_match 
from tqdm import tqdm
import pandas as pd
urls = generate_urls(2021, 8, 1)

match_eval_df = parse_url_match(urls[0])
match_train_df = pd.concat([parse_url_match(urls[i]) for i in range(1,len(urls))])

match_eval_df.to_csv("match_eval_df.csv")
match_train_df.to_csv("match_train_df.csv")


