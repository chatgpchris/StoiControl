# 🦅 StoiControl

StoiControl is an interactive self-mastery challenge inspired by Stoic philosophy. 

The app helps users assess how “Stoic” they have been recently by answering reflective questions about emotions, reasoning, and behavior, and provides insightful feedback based on their results.

## 🚀 Take the Stoic Self-Test

You can try the app online via Streamlit Cloud:  

[**Launch StoiControl**](to_be_updated)

## ✨ Features

- 24 thoughtfully designed Stoic self-test questions

- Scoring system with personalized status messages

- Streamlit-based web interface with a modern, readable UI

- Option to retake the test multiple times

- Responsive layout optimized for desktop and mobile


## 💻 How it Works

- Users are welcomed with an introduction to the Stoic Self-Test.

- Each question is presented with multiple-choice answers.

- Users select an option for each question.

- The app calculates a score based on internal scoring rules.

- A status message is displayed that interprets the user's Stoic “score.”

- Users can retake the test to track their growth over time.

The scoring is percentile-based:

Score Range	      Status Category

0–39	            The Unsettled Mind in the Anti-Stoic Zone

40–59	            The Growing Practitioner

60–79	            The Steady Walker

80–94	            The Inner Citadel Builder

95–99	            Philosopher of Life

100	                The Stoic Emperor

### Prerequisites

* Python 3.10+

* Streamlit

### Installation

1.  Clone this repository:

    ```
    git clone [https://github.com/chatgpchris/stoicontrol.git](https://github.com/chatgpchris/stoicontrol.git)
    cd stoicontrol
    ```

2.  Install the required libraries:

    ```
    pip install -r requirements.txt
    ```

3.  Run the application from your terminal:

    ```
    streamlit run stoicontrol.py
    ```
    
4.  Open the URL provided by Streamlit in your browser.


## 📁 Project Structure

stoicontrol/

├─ stoicontrol.py                 # Main Streamlit app

├─ how_much_stoic_have_you_been.py  # Questions and scoring data

├─ requirements.txt               # Python dependencies

├─ .streamlit/

│   └─ config.toml                # Streamlit theme settings

└─ README.md                      # Project documentation


## 🎨 Customization

The app uses a dark Stoic-themed design:

Primary Color: #0077b6

Background: #4b1a1a

Text Color: #f5f5f5

Font: serif

These can be modified in .streamlit/config.toml


## ⚖️ License

This project is released under the MIT License. You are free to use, modify, and distribute it while including proper attribution.
