import streamlit as st
import preprocessor
import helper
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
st.sidebar.title("whatsapp chat analyser")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data=bytes_data.decode("utf-8")
    df=preprocessor.preprocess(data)
    user_list= df["username"].unique().tolist()
    user_list.sort()
    user_list.insert(0,"Overall")
    selected_user = st.sidebar.selectbox(
        "Select User", user_list
    )
    if st.sidebar.button("Show Analysis"):
        num, word_message, media_message, links = helper.fetch_stats(selected_user, df)
        col1, col2, col3, col4 = st.columns(4)

        with col1:
                st.header("Total Messages")
                st.title(num)
        with col2:
                st.header("Total Words")
                st.title(word_message)
        with col3:
                st.header("Total media messages")
                st.title(media_message)
        with col4:
                st.header("Total URL")
                st.title(links)
        st.title("Monthly Timeline")
        timeline_df = helper.get_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline_df["year_month"], timeline_df["message"])
        plt.xticks(rotation="vertical")
        st.pyplot(fig)
        st.title("Daily Timeline")
        dailytimeline_df=helper.get_dailytimeline(selected_user,df)
        fig,ax = plt.subplots()
        ax.plot(dailytimeline_df["only_date"],dailytimeline_df["message"])
        plt.xticks(rotation="vertical")
        st.pyplot(fig)
        col1,col2=st.columns(2)
        with col1:
            st.title("Most Busy Days")
            busyday= helper.most_busyday(selected_user,df)
            busyday.index = busyday.index.astype(str)
            fig, ax = plt.subplots()
            ax.bar(busyday.index, busyday.values)
            plt.xticks(rotation="vertical")
            st.pyplot(fig)
        with col2:
            st.title("Most Busy Month")
            busymonth = helper.most_busymonth(selected_user, df)
            busymonth.index = busymonth.index.astype(str)
            fig, ax = plt.subplots()
            ax.bar(busymonth.index, busymonth.values)
            plt.xticks(rotation="vertical")
            st.pyplot(fig)
        activity_df= helper.heatmap(selected_user,df)
        fig, ax = plt.subplots()
        sns.heatmap(activity_df)
        st.pyplot(fig)
        if selected_user =="Overall":
            st.title("Most Busy Users")
            X, new_df= helper.most_busy_users(df)
            fig, ax = plt.subplots()
            col1, col2 = st.columns(2)
            with col1:
                ax.bar(X.index, X.values,color="red")
                plt.xticks(rotation="vertical")
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)

        st.title("Most Common Words")
        cloud= helper.create_wordcloud(selected_user,df)
        fig,ax= plt.subplots()
        ax.imshow(cloud)
        ax.axis('off')
        st.pyplot(fig)

        new=helper.most_common_words(selected_user,df)
        fig, ax=plt.subplots()
        st.title("Most commmon words Graph")
        ax.barh(new["message"],new["count"])
        plt.xticks(rotation="vertical")
        st.pyplot(fig)


        emoji_df = helper.emoji_finder(selected_user, df)
        if not emoji_df.empty:
            col1, col2 = st.columns(2)
            with col1:
                st.title("Emoji Analysis")

                st.dataframe(emoji_df)
            with col2:
                st.title("Pie Chart for Emojis")
                font_path = r"C:\Users\ASUS\Desktop\segoe-ui-emoji.ttf"
                prop = fm.FontProperties(fname=font_path)
                fig, ax = plt.subplots()
                ax.pie(emoji_df["Count"].head(),labels=emoji_df["Emojis"].head(),autopct="%0.2f", textprops={'fontproperties': prop})
                st.pyplot(fig)




