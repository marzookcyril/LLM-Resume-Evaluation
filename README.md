# LLM-Resume-Evaluation

## Overview:
LLM-Resume-Evaluation is an innovative project for the job application process. Leveraging state-of-the-art Language Model Matchers (LLMs). It tailors resumes to match the unique requirements of specific job offers. This method ensures that each resume is optimized to stand out and resonate with the expectations of prospective employers.

## Key Features:
1. Language Model Matchers (LLMs):
Utilizes cutting-edge LLMs, including GPT-3, for intelligent and context-aware resume analysis.
Understands job descriptions and candidate profiles to generate personalized content.

2. Job Offer Optimization:
Customizes resumes for specific job offers, enhancing the likelihood of a perfect match.
Analyzes key skills, qualifications, and language nuances to create tailored application documents.

3. Automated Scoring System:
Implements an automated scoring mechanism based on job requirements and industry standards.
Provides feedback on the strength of the resume and suggests improvements for better alignment.

4. Smart Recommendation Engine:
Recommends skill enhancements and content modifications to boost resume effectiveness.
Guides users in optimizing their professional profiles for targeted job applications.


## Benefits:
Time-Efficient Job Application: Streamlines the application process by automating resume customization, saving time for applicants.
Increased Job Match Accuracy: Improves the likelihood of landing interviews by aligning resumes precisely with job requirements.
Continuous Improvement: Encourages users to enhance their skillsets based on personalized recommendations, fostering professional growth.

## Quick start : 

Fill the `api_key.py` file with your OpenAI API key : https://beta.openai.com/account/api-keys

Your addition should look like `API_KEY = "YOUR_API_KEY"`

To generate a targeted cv : 

Fill the job offer in the file `inputs/job_offer.py`, make sure you don't let return to lines and replace them all with `\n`.

Then add the experiences, education and project of the person you want to generate the CV (the language doesn't matter) in the file `inputs/input_person_infos/person_dynamic_infos.py`. The informations are dynamic because they are the ones that will be changed by Suro. 
The static informations such as name, contact, email address, city etc can be filled in `inputs/input_person_infos/person_static_infos.py`.
Make sure that you follow the example structure. 

Make sure you have all the dependecies installed by running `pip install -r requirements.txt` or `pip3 install -r requirements.txt` 

To generate the json resume, run the following command : `python core.py`

The generated resume is in `cv.resume.json`

You can use an online convertor to display it as a pdf.
For instance, this will generate you a word version that you can convert https://resumefodder.com/generate.html
