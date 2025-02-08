# 📌 RottED

## 📖 Description

RottED is an innovative hackathon project aimed at revolutionizing academic content consumption by transforming PDFs into engaging, TikTok-style videos. In a world where people often consume brain rot content with little to no educational value, RottED bridges the gap between entertainment and learning. By leveraging AI-powered API calls for advanced summarization, intelligent image generation, and seamless audio synthesis, this project automates the creation of concise, visually compelling, and informative short-form educational videos. Designed for dynamic learning, RottED enhances accessibility and retention by presenting complex concepts in an engaging and digestible format.
SPECIAL HIGHLIGHT -- Our BrainRot feature for the kids to learn in the language they would have fun with [:)]

## 📂 Project Contents

- **📌 Backend**: Handles PDF processing, generates summaries, creates images, converts text to speech, and assembles videos.
  - **Main.py**: `main.py` for executing backend functions.
  - **App.py**: `app.py` for executing server functions to chat between backend and frontend.
  - **Dependencies**: `requirements.txt` for managing necessary libraries.
- **🎨 Frontend**: A HTML/CSS/JavaScript-based interface that displays the generated videos in a TikTok-style format. And another mobile emulated application design for mobile app.

  - **UI Code**: Contains `index.html` that has the major application functionality and `home.html` which is the landing page.
  - **Assets**: `images/` directories to store related content.
  - **static**: Stores the generated videos for the session.
  - **upload**: Stores uploaded pdfs for the session.

  - **rottED_Android**: This is the android version for the mobile app emulated on android studio. If interested in running this please install Android studio, after opening an emulated device connected with it, build the gradle project to see the app deployed. A video and screenshot would be provided with the submission.
    This could not be uploaded as the project size was big to be put in the main repo so added as an additional link.

## 🎯 Objectives

✔ Extract key concepts from PDFs and generate concise summaries.
✔ Generate AI-driven images based on the summarized content.
✔ Convert textual summaries into natural-sounding speech.
✔ Merge gameplay video, AI-generated images, and audio to form engaging short videos.
✔ Display videos in a user-friendly, reels-style interface.

## 🛠 Tools and Libraries

The project utilizes the following technologies:

### 🖥 Backend:

- **🐍 Python** (for processing and AI integration)
- **🤖 Google Generative AI API** (for summarization, image generation, and prompt handling)
- **🖼 Pillow** (for image processing)
- **🎬 MoviePy** (for video creation)
- **🗣 gTTS** (for text-to-speech conversion)
- **🌐 Flask** (for API handling and backend support) -- The Server

### 🌍 Frontend:

- **📜 HTML/CSS/JavaScript** (for a simple yet effective interactive UI)
- **📜 A Mobile Version** (for ease of use and versitality)

## ⚙ How to Use

### 📌 Prerequisites

Ensure you have Python installed and install the required dependencies:

```bash
pip install -r requirements.txt
```

### 🚀 Setup the Backend

1. Place your API key in a file named `API_KEY.txt`.
2. Start by running the local server using app.py (python app.py)

### 🌎 Running the Frontend

Simply open `index.html` in a web browser.

## 📊 Results

The project produces:

- Concise educational summaries in video format.
- AI-generated images that visually enhance the learning experience.
- Narration audio for accessibility and engagement.
- A TikTok-style scrolling UI for browsing generated videos.

## 📁 File Structure

RottED/
│ ├── app.py/ # Core Server Processes
│ ├── main.py # Main script handling PDF processing and video generation
│ ├── API_KEY.txt # Stores the API key (not included in repo)
│ ├── requirements.txt # Required dependencies
├── frontend/
│ ├── ui/
│ │ ├── code/
│ │ │ ├── home.html # Homepage UI
│ │ │ ├── index.html # Main UI
│ │ ├── images/ # Stores supporting images like the logo
├── .gitignore # Git ignore file
├── README.md # This file

## 🔮 Future Enhancements

Enhanced UI/UX for better interaction: Improve the overall design and usability of the website, ensuring a smooth, modern, and engaging user experience with intuitive navigation and optimized accessibility.

Support for multiple video backgrounds: Allow users to choose or generate different background videos for their content, adding variety and customization to their learning experience.

User authentication for personalized content: Implement login and user profiles, enabling personalized learning paths, progress tracking, and content recommendations based on user activity.

Cloud-based deployment: Deploy the platform on cloud services like AWS, Google Cloud, or Firebase for seamless access, scalability, and better performance.

Interactive quizzes for engagement: Integrate short quizzes within the platform to reinforce learning, test comprehension, and provide immediate feedback to users.

Personalized learning roadmap: Develop a feature that allows users to track their progress through structured learning paths, unlocking new content based on their achievements. This would be AI supported as well. One huge way would be to track the productivity times and monitoring it via the AI to find the peak productivity slots.

Web-based dashboard for insights: Create a user dashboard where learners can view analytics, track their quiz scores, measure time spent on content, and gain insights into their educational journey.

## 👥 Contributors

Sagar Patel - Kunal Pandya - Devarsh Joshi - Tanish Singla

## 🤝 Contributions

Contributions are welcome! Feel free to fork this repository, improve the project, and submit a pull request.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
