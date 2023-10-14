import os
from huggingface_hub import hf_hub_download

# load environment variables
from dotenv import load_dotenv

load_dotenv()

def get_model():
    # Download the model from the Hub
    llm_repo = os.getenv("HF_REPO")
    llm_file = os.getenv("HF_MODEL_FILE")

    llm_local_path = hf_hub_download(repo_id=llm_repo, filename=llm_file, resume_download=True)

    # write the llm_local_path to the .env file
    with open(".env", "a") as f:
        f.write(f"LLM_LOCAL_PATH={llm_local_path}\n")

    print("the local llm path: ============>", os.getenv("LLM_LOCAL_PATH"))

    return llm_local_path
