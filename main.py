from fastapi import FastAPI
from llama_cpp import Llama
from utils.download_model import get_model

app = FastAPI()

model_path = get_model()
llama_model = Llama(
    model_path=model_path,
    n_threads=os.cpu_count(),
    n_batch=512,
)


@app.get("/")
async def root():
    return {"message": "Welcome to Llama-land!"}

# Endpoint for accepting a user prompt


@app.post("/prompt")
async def prompt(prompt_data: dict):

    user_prompt = prompt_data["prompt"]

    if not user_prompt:
        return {"message": "Please provide a prompt!"}

    prompt_template = f'''SYSTEM: You are a helpful, respectful and honest assistant. Always answer helpfully.

    USER: {user_prompt}

    ASSISTANT:
    '''

    response=llama_model(
        prompt=prompt_template,
        max_tokens=256,
        temperature=0.5,
        top_p=0.95,
        repeat_penalty=1.2,
        top_k=150,
        echo=True
    )

    print(response["choices"][0]["text"])

    return {"message": response["choices"][0]["text"]}
