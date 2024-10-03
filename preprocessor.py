import regex as re
import pandas as pd


def preprocess(data):
    # Define the patterns for date and messages
    pattern1 = r'\[(\d{4}-\d{2}-\d{2}), (\d{2}:\d{2}:\d{2} [AP]M)\]'
    dates = re.findall(pattern1, data)
    cleaned_dates = []

    for date, time in dates:
        clean_time = time.replace('\u202f', '')[:5] + time[-2:]
        cleaned_dates.append(f"{date} {clean_time}")

    pattern = r'\[\d{4}-\d{2}-\d{2}, \d{2}:\d{2}:\d{2} [AP]M\] ([^:]+): (.+)'
    matches = re.findall(pattern, data)
    formatted_messages = [f'{user.strip()}: {message.strip()}' for user, message in matches]

    # Create DataFrame
    Df = pd.DataFrame({'user messages': formatted_messages, 'message dates': cleaned_dates})

    # Convert message dates to datetime format
    Df["message dates"] = pd.to_datetime(Df["message dates"], format='%Y-%m-%d %I:%M%p')
    Df.rename(columns={"message dates": "date"}, inplace=True)

    # Extract usernames and messages directly from 'user messages'
    Df[['username', 'message']] = Df['user messages'].str.extract(r'^(.*?):\s*(.*)$')

    # Drop the 'user messages' column as it's no longer needed
    Df.drop(columns=["user messages"], axis=1, inplace=True)

    # Extract year, month, day, hour, and minute from date
    Df["year"] = Df["date"].dt.year
    Df["month"] = Df["date"].dt.month_name()
    Df["month_num"] = Df["date"].dt.month
    Df["only_date"] = Df["date"].dt.date
    Df["day"] = Df["date"].dt.day
    Df["day_name"] = Df["date"].dt.day_name()
    Df["hour"] = Df["date"].dt.hour
    Df["minute"] = Df["date"].dt.minute
    period = []
    for hour in Df["hour"]:
        if hour==23:
            period.append(str(hour)+"-"+str("00"))
        elif hour==0:
            period.append(str("00")+"-"+str(hour + 1))
        else:
            period.append(str(hour)+"-"+str(hour+1))
    Df["period"]= period


    return Df

