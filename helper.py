from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
import emoji
from collections import Counter
import seaborn as sns
extract= URLExtract()
def fetch_stats(selected_user,df):
    if selected_user != "Overall":
        df = df[df["username"] == selected_user]

    num_messages = df.shape[0]
    words= []
    for message in df["message"]:
            words.extend(message.split())
    filtered_df = df[
        df["message"].str.contains("image omitted", na=False) |
        df["message"].str.contains("gif omitted", na=False) |
        df["message"].str.contains("sticker omitted", na=False) |
        df["message"].str.contains("video omitted", na=False)
        ].shape[0]

    links=[]
    for message in df["message"]:
        links.extend(extract.find_urls(message))

    return num_messages, len(words), filtered_df, len(links)

def most_busy_users(df):
    X =df["username"].value_counts()
    new_df=round((df["username"].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={"username":"person", "count":"message percent"})
    return X,new_df
def create_wordcloud(selected_user, df):
    f = open('stop_hinglish.txt', "r")
    stop_words = f.read()
    if selected_user != "Overall":
        df = df[df["username"] == selected_user]
    df = df[~
            df["message"].str.contains("image omitted", na=False) |
            df["message"].str.contains("gif omitted", na=False) |
            df["message"].str.contains("sticker omitted", na=False) |
            df["message"].str.contains("video omitted", na=False)]
    def remove_stopword(message):
        Y=[]
        for word in message.lower().split():
            if word not in stop_words:
                Y.append(word)
        return" ".join(Y)

    wc= WordCloud(width=500, height=500, min_font_size=10,background_color="white")
    df.loc[:, "message"]=df["message"].apply(remove_stopword)
    df_wc= wc.generate(df["message"].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user,df):
    if selected_user != "Overall":
        df = df[df["username"] == selected_user]
    f=open('stop_hinglish.txt',"r")
    stop_words=f.read()
    df= df[~
        df["message"].str.contains("image omitted", na=False) |
        df["message"].str.contains("gif omitted", na=False) |
        df["message"].str.contains("sticker omitted", na=False) |
        df["message"].str.contains("video omitted", na=False)]
    words = [];
    for message in df["message"]:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)
    return_df= pd.DataFrame(Counter(words).most_common(20)).rename(columns={0:"message", 1:"count"})
    return return_df
def emoji_finder(selected_user,df):
    if selected_user != "Overall":
        df = df[df["username"] == selected_user]
    emojis=[]
    for message in df["message"]:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])
    # emoji_df = pd.DataFrame(emojis,columns=["Emojis"])
    # emojis_df= emoji_df.value_counts().reset_index()
    emojis_df=pd.DataFrame(Counter(emojis).most_common(), columns=["Emojis", "Count"])
    return emojis_df
def get_timeline(selected_user,df):
    if selected_user != "Overall":
        df = df[df["username"] == selected_user]
    timeline_df=df.groupby(["year","month_num","month"]).count()["message"].reset_index()
    timeline_df['year_month'] = timeline_df['year'].astype(str) + ' ' + timeline_df['month']
    return timeline_df
def get_dailytimeline(selected_user,df):
    if selected_user != "Overall":
        df = df[df["username"] == selected_user]
    dailytimeline_df=df.groupby(["only_date"]).count()["message"].reset_index()
    return dailytimeline_df
def most_busyday(selected_user,df):
    if selected_user != "Overall":
        df = df[df["username"] == selected_user]
    return df["day_name"].value_counts()
def most_busymonth(selected_user,df):
    if selected_user != "Overall":
        df = df[df["username"] == selected_user]
    return df["month"].value_counts()
def heatmap(selected_user,df):
    if selected_user != "Overall":
        df = df[df["username"] == selected_user]
    activity_heatmap=df.pivot_table(index="day_name", columns="period", values="message", aggfunc="count").fillna(0)
    return activity_heatmap




