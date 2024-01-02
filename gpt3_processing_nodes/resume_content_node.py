import openai

def rephrase_content(content, type, job_offer):
    base_prompt = "Someone is applying for a job offer. He has a list of experiences that are not directly relevant to the job and he would like to know how to detail (and add more informations) his experiences in order to please the hiring manager (They are in French and he doesn't speak English). He asks a magic AI that makes your resume perfect for a specific job. Here is an example of what he asked to the magic AI. He gave it the details of one experience and the information of a job offer. As a result, he received a perfectly rephrased and adapted version (in french) of the experience he shared. The magic AI took his experience and made it relevant for the hiring manager.  Here is what it looked like : \nInput for the magic AI : "
    full_prompt = base_prompt + "\Job offer information :\n" + job_offer + "\n\nDetails of the experience to rephrase : \n" + content + "Magic AI's output:\nRephrased experience (displayed in french as bullet points ready to be added to your resume):"
    response = None
    if type == "exp" :
        response = openai.Completion.create(
        model="text-davinci-002",
        prompt=full_prompt,
        temperature=0.7,
        max_tokens=500,
        top_p=1,
        frequency_penalty=2,
        presence_penalty=0,
        best_of=3
        )
    return response["choices"][0]["text"]

def rephrase_elements(list_content, type, job_offer):
    output = []
    for element in list_content:
        rephrased_content = rephrase_content(element["content"], type, job_offer).replace("-","").replace("\n\n","\n").split('\n')[1:]
        output.append(
            { 
                "name": element["meta"]["name"],
                "position": element["meta"]["position"],
                "url": "",
                "startDate":  element["meta"]["startDate"],
                "endDate": element["meta"]["endDate"],
                "highlights": rephrased_content,
                #"Summary" : "This is a summary that will be soon be subject to the Elexir"
                }
            )
    return output
