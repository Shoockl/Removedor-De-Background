import tkinter as tk
from tkinter import filedialog
from rembg import remove
from PIL import Image

def tirar_fundo():
    input_path = filedialog.askopenfilename(title="Selecione a sua imagem", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if not input_path:
        return  

    output_path = filedialog.asksaveasfilename(title="Escolha onde salvar sua imagen", defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if not output_path:
        return  

    inp = Image.open(input_path)

   
    output_image = remove(inp)

    
    output_image.save(output_path)

    result_label.config(text=f"Fundo removido com sucesso, a imagem foi salve em: {output_path}")

root = tk.Tk()
root.title("Removedor de fundo")


remove_button = tk.Button(root, text="Clique aqui para selecionar a imagem", command=tirar_fundo)
remove_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
