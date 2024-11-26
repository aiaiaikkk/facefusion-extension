import gradio as gr
from facefusion import blend_faces

class Script:
    def title(self):
        return "FaceFusion Plugin"

    def show(self, is_img2img):
        return True

    def ui(self, is_img2img):
        with gr.Blocks() as interface:
            with gr.Row():
                img1 = gr.Image(label="输入图片 1", type="numpy")
                img2 = gr.Image(label="输入图片 2", type="numpy")
            alpha = gr.Slider(minimum=0.0, maximum=1.0, value=0.5, step=0.1, label="融合比例")
            output = gr.Image(label="融合结果")
            button = gr.Button("开始融合")
            
            # 按钮点击触发融合逻辑
            button.click(fn=blend_faces, inputs=[img1, img2, alpha], outputs=output)
        return interface
