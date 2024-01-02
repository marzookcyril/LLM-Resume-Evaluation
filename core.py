
import openai
from inputs.job_offer import job_offer_sample, job_offer_sample_2, job_offer_sample_3, job_offer_CHAOUL
from inputs.input_person_infos.person_dynamic_infos import sample_expriences, sample_education,sample_projects,general_infos, sample_expriences_CHAOUL
from gpt3_processing_nodes.job_offer_node import rephrase_job_offer
from gpt3_processing_nodes.resume_content_node import rephrase_content, rephrase_elements
from api_key import API_KEY

import json
from inputs.input_person_infos.person_static_infos import static_infos 

import time
openai.api_key = API_KEY

# rephrased_experiences= []
# rephrased_education = []
# rephrased_projects = []


# rephrased_job_offer = rephrase_job_offer(job_offer_sample_3)
# rephrased_experiences = rephrase_elements(sample_expriences, "exp", rephrased_job_offer)
# rephrased_education = rephrase_elements(sample_education, "exp")
# rephrased_projects = rephrase_elements(sample_projects, "exp")

def run_pipeline(infoo, job_offer, experiences = [], education = [], projects = [] ):
      rephrased_job_offer = rephrase_job_offer(job_offer)
      rephrased_experiences = rephrase_elements(experiences, "exp", rephrased_job_offer)
      infoo["work"] = rephrased_experiences
      return infoo



# breakpoint()
new_resume1 = static_infos
#new_resume2 = static_infos
#new_resume3 = static_infos
job1 = run_pipeline(new_resume1, job_offer_CHAOUL, sample_expriences_CHAOUL)
with open('cv.CHAOUL1.json', 'w') as json_file:
  json.dump(job1, json_file)
print("Done")


job1 = run_pipeline(new_resume1, job_offer_CHAOUL, sample_expriences_CHAOUL)
with open('cv.CHAOUL2.json', 'w') as json_file:
  json.dump(job1, json_file)
print("Done")


job1 = run_pipeline(new_resume1, job_offer_CHAOUL, sample_expriences_CHAOUL)
with open('cv.CHAOUL3.json', 'w') as json_file:
  json.dump(job1, json_file)
print("Done")

print("Safe saleet had la job offer.")

# job2 = run_pipeline(new_resume2, job_offer_sample_2, sample_expriences)
# with open('cv.resume2.json', 'w') as json_file:
#   json.dump(job2, json_file)


# job3 = run_pipeline(new_resume3, job_offer_sample_3, sample_expriences)
# # static_infos["work"] = static_infos["work"] + rephrased_experiences
# with open('cv.resume3.json', 'w') as json_file:
#   json.dump(job3, json_file)
# breakpoint()

print("Done")


# PIPELINE FORMAT

# pipeline = [
#     {
#     "id" : 0,
#     "processing_function" : rephrase_job_offer,
#     "input" : job_offer_sample,
#     "output" : None
#     },
#     {
#     "id" : 1,
#     "processing_function" :    rephrase_content,
#     "input" : ["Output#0",sample_expriences, sample_education, sample_projects],
#     "output" : [rephrased_experiences, rephrased_education, rephrased_projects]
#     }]

# Pipeline architecture to be done afterwards
# for node in pipeline:
#     output = None
#     previous_output = {"Output#0" : output}
#     for input in node["input"]:
#         if input in previous_output:
#             input = previous_output[input]
#     output = node["processing_function"](*node["input"])

