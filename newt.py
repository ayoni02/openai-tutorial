import openai

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
    
openai.api_key = open_file('openaikey.txt')

def gpt3_completion(prompt, engine='text-davinci-002', temp=0.7, top_p=1.0, token=400, freq_pen=0.0, pres_pen=0.0, stop=['<<END>>']):

    prompt = prompt.encode(encoding='ASCII', errors='ignore').decode()
    try:
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            temperature=temp,
            max_tokens=token,
            top_p=top_p,
            frequency_penalty=freq_pen,
            presence_penalty=pres_pen,
            stop=stop
        )
        text = response['choices'][0]['text'].strip()
        return text
    except Exception as oops:
        return "GPT3 error: %s" % oops
    
if __name__ == '__main__':
    prompt = input('Prompt: ')
    print(gpt3_completion(prompt))