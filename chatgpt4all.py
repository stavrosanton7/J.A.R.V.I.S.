from pyllamacpp.model import Model

def new_text_callback(text: str):
    print(text,end="",flush=True)

prompt = input("How can i help?")

model = Model(ggml_model='C:/J.A.R.V.I.S. A.I/gpt4all-model.bin',n_ctx=512)
Answer = model.generate(prompt,n_predict=50,new_text_callback=new_text_callback,n_threads=6)

print("")
print(Answer)
