import openai

def rephrase_job_offer(job_offer):
    full_prompt = "Summarize in 500 words this job offer and the skills it contains.  \nJob offer :\n" + job_offer
    if int(len(full_prompt)) > 16000 :
        return None
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt= full_prompt,
    temperature=0.1,
    max_tokens= 500,
    top_p=0.1,
    frequency_penalty=0,
    presence_penalty=0,
    )
    return response["choices"][0]["text"]