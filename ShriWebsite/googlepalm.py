import google.generativeai as palm


def response_AI(prompt):
    palm.configure(api_key='AIzaSyATkhdCSm1lk0g4IQbWB5lJ3xpUpE6tHR4')
    completion = palm.generate_text(
        model="models/text-bison-001",
        prompt=prompt,
        temperature=0,
        max_output_tokens=1000,
    )
    return completion.result
