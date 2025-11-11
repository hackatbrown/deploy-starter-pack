import gradio as gr

def greet(name): 
    return f"Hello, {name or 'team'}!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text", title="Hack@Brown Gradio")
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
