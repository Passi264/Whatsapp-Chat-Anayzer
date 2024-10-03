# WhatsApp Chat Analyzer

This project is a WhatsApp Chat Analyzer built using Python and Streamlit. The application allows you to upload WhatsApp chat data and analyze various statistics such as the most active users, message counts, word frequencies, and much more. It also generates visualizations such as timelines, heatmaps, and pie charts for emoji usage.

## Features

- Upload WhatsApp Chat Data: Upload `.txt` files exported from WhatsApp and visualize chat statistics.
- User Analysis: Shows the most active users, busiest days and months, and generates word clouds for common words.
- Visualizations:
  - Monthly and daily message timelines.
  - Most active days and months.
  - Heatmaps showing the activity levels by day and time.
  - Emoji analysis with a pie chart for emoji usage.
- Word Cloud: Generates a word cloud to highlight the most commonly used words in the conversation.
- Emoji Analysis: Displays the emojis used, their counts, and provides a pie chart representation.

## How to Run the Project

```bash
# Clone the repository
git clone https://github.com/Passi264/Whatsapp-Chat-Anayzer.git

# Navigate to the project directory
cd Whatsapp-Chat-Anayzer

# Run the Streamlit app
streamlit run app.py

# Prerequisites:
# - Python 3.7 or higher
# - Install the required packages
pip install -r requirements.txt
```
The app will open in your browser. You can upload a .txt file (exported from WhatsApp) using the file uploader in the sidebar. The app will then preprocess and analyze the data to display various statistics and visualizations.

## Project Structure

- app.py: The main application script that defines the Streamlit interface and visualizations.
- helper.py: Contains helper functions for calculating statistics and generating visualizations.
- preprocessor.py: Responsible for preprocessing the uploaded chat data, extracting relevant fields like dates and usernames.
- stop_hinglish.txt: Contains stopwords used to filter out common words in the word cloud analysis.
- requirements.txt: Lists the dependencies required to run the project (e.g., Streamlit, pandas, seaborn).


