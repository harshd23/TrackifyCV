# TrackifyCV 📑🔍

Trackify is a powerful tool designed to assist professionals in optimizing their resumes to better align with job descriptions. By analyzing the content of both the resume and the job description, Trackify provides valuable insights, such as detailed explanations of the resume's strengths, suggestions for skill enhancement, identification of missing keywords, and an overall percentage match. This ensures that users can effectively tailor their resumes to meet specific job requirements, increasing their chances of landing their desired roles.

![PDFAssist](https://github.com/harshd23/TrackifyCV/blob/main/trackifycv1.png)
![PDFAssist](https://github.com/harshd23/TrackifyCV/blob/main/trackifycv2.png)

## Technologies Used:-

- Langchain + LLM(Google Gemini 1.5 Pro)
- Streamlit: UI

## Features:-

- Provides detailed insights and explanations of your resume's content.
- Recommends ways to enhance your skills based on job descriptions.
- Identifies missing keywords to better align with job requirements.
- Calculates how closely your resume matches the job description.

## Project Structure:-

- app.py: The main Streamlit application script.
- requirements.txt: A list of required Python packages for the project.
- .env: Configuration file for storing your Google API key.

## Steps to run the project:-

1.Clone this repository to your local machine using:

```bash
  git clone https://github.com/harshd23/TrackifyCV.git
```

2.Install the required dependencies using pip:

```bash
  pip install -r requirements.txt
```

3.Set up your Google API key by creating a .env file in the project root and adding your API

```bash
  GOOGLE_API_KEY = "put_your_google_api_key_here"
```

## Usage of the project:-

1.Run the Streamlit app by executing:

```bash
streamlit run app.py
```

2.The web app will open in your browser:

- You can upload your Resume in PDF format directly.
- Once the resume is uploaded successfully, then click on any one of the four options provided to get more information about your resume.
- Thus, you can then freely explore other options and improve your resume based on suggestions given.
