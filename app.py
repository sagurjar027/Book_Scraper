import streamlit as st
from bs4 import BeautifulSoup
import requests


st.set_page_config(page_title="Book Scapper App",page_icon="📚")

st.title("📚Book Scrapper app!!")
st.subheader("Welcome to the Book Scrapper app!")

category = st.selectbox("Select a category", ["Travel", "Music", "Mystery", "Science", "Fiction"])


# Function to fetch books from a website
def books_fetch(category):
    if category == "Travel":
        url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
        reponse = requests.get(url)
        soup = BeautifulSoup(reponse.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")
        st.write(f"There are {len(books)} books in {category} category")
        for book in books:
            title = book.h3.a["title"]
            # price should be in INR
            price = book.find("p", class_="price_color").text
            rating = book.p["class"][1]
            img_rel_url = book.img["src"].replace("../../", "")
            st.image(f"https://books.toscrape.com/{img_rel_url}", width=100)
            st.write(f"Title  : {title}")
            st.write(f"Price  : {price}")
            st.write(f"Rating  : {rating} star")
            st.write("---")
        
    elif category == "Music":
        url = "https://books.toscrape.com/catalogue/category/books/music_34/index.html"
        reponse = requests.get(url)
        soup = BeautifulSoup(reponse.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")
        st.write(f"There are {len(books)} books in {category} category")
        for book in books:
            title = book.h3.a["title"]
            # price should be in INR
            price = book.find("p", class_="price_color").text
            rating = book.p["class"][1]
            img_rel_url = book.img["src"].replace("../../", "")
            st.image(f"https://books.toscrape.com/{img_rel_url}", width=100)
            st.write(f"Title  : {title}")
            st.write(f"Price  : {price}")
            st.write(f"Rating  : {rating} star")
            st.write("---")

    elif category == "Mystery":
        url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
        reponse = requests.get(url)
        soup = BeautifulSoup(reponse.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")
        st.write(f"There are {len(books)} books in {category} category")
        for book in books:
            title = book.h3.a["title"]
            # price should be in INR
            price = book.find("p", class_="price_color").text
            rating = book.p["class"][1]
            img_rel_url = book.img["src"].replace("../../", "")
            st.image(f"https://books.toscrape.com/{img_rel_url}", width=100)
            st.write(f"Title  : {title}")
            st.write(f"Price  : {price}")
            st.write(f"Rating  : {rating} star")
            st.write("---")
    elif category == "Science":
        url = "https://books.toscrape.com/catalogue/category/books/science_22/index.html"
        reponse = requests.get(url)
        soup = BeautifulSoup(reponse.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")
        st.write(f"There are {len(books)} books in {category} category")
        for book in books:
            title = book.h3.a["title"]
            # price should be in INR
            price = book.find("p", class_="price_color").text
            rating = book.p["class"][1]
            img_rel_url = book.img["src"].replace("../../", "")
            st.image(f"https://books.toscrape.com/{img_rel_url}", width=100)
            st.write(f"Title  : {title}")
            st.write(f"Price  : {price}")
            st.write(f"Rating  : {rating} star")
            st.write("---")
    elif category == "Fiction":
        url = "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html"
        reponse = requests.get(url)
        soup = BeautifulSoup(reponse.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")
        st.write(f"There are {len(books)} books in {category} category")
        for book in books:
            title = book.h3.a["title"]
            # price should be in INR
            price = book.find("p", class_="price_color").text
            rating = book.p["class"][1]
            img_rel_url = book.img["src"].replace("../../", "")
            st.image(f"https://books.toscrape.com/{img_rel_url}", width=100)
            st.write(f"Title  : {title}")
            st.write(f"Price  : {price}")
            st.write(f"Rating  : {rating} star")
            st.write("---")


st.sidebar.title("About the App")
st.sidebar.info("This is a simple book scrapper app which scrapes books from https://books.toscrape.com/ website which was developed by ~Sahil Gurjar. You can select a category and it will fetch the books in that category.")

#add statics to the sidebar
st.sidebar.title("Statistics")
st.sidebar.write("Total number of books avaliable: 1000")
st.sidebar.write("Total number of categories: 5")







if st.button("Fetch Books"):
    st.write(f"Fetching books in {category}...")
    # Simulate fetching books from a website https://books.toscrape.com/
    books_fetch(category)



#adding footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        text-align: center;
    }
    </style>
    <div class="footer">
    <p>Created by Sahil Gurjar</p>
    </div>
    """,
    unsafe_allow_html=True
)


#adding contact us
st.sidebar.title("Contact Us")
st.sidebar.write("If you have any questions or feedback, please feel free to reach out to us at:")
st.sidebar.write("Email: sagurjar027@gamil.com")
st.sidebar.write("linkdin: https://www.linkedin.com/in/sahil-kasana6055/")

#app feedback and store feedback in feed.txt file
st.subheader("Feedback!!")
st.write("We would love to hear your thoughts on our app. Please provide your feedback below:")
feedback = st.text_area("Please provide your feedback here:")
Name = st.text_input("Name")
if st.button("Submit Feedback"):
    with open("feed.txt", "a") as f:
        f.write(f"Username: {Name}   Feedback: {feedback}\n")
    st.success("Thank you for your feedback!")


