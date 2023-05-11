import requests
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from scripts.upload_to_pinata import pinata_upload
from scripts.create_collectible import deploy_and_create_contract


#Configuração de variaveis globais
janela = Tk()
frame_data = Frame(janela, bd=4, bg='#dfe3ee',highlightbackground='#759fe6', highlightthickness=3)
frame_nft=Frame(janela, bd=4, bg='#dfe3ee',highlightbackground='#759fe6', highlightthickness=3)
frame_info=Frame(janela, bd=4, bg='#dfe3ee',highlightbackground='#759fe6', highlightthickness=3)


janela.title("NFT Tmaker")
janela.configure(background='#003566')
janela.geometry("700x500")



#def main():
    

    

def frames():
    
    #Configurando o frame das entradas de dados
    frame_data.place(relx=0.01, rely= 0.02, relwidth=0.4, relheight=0.65)
    
    lb_dados = Label(frame_data, text="Dados da NFT", font=("New Times Roma", 15), bg='#dfe3ee')
    lb_dados.place(relx=0.25, rely=0.03)

    lb_nome = Label(frame_data, text="Nome da NFT:", font=("New Times Roma", 11), bg='#dfe3ee')
    lb_nome.place(relx=0.07, rely=0.2)
    entry_nome = Entry(frame_data)
    entry_nome.place(relx=0.07, rely=0.27)

    lb_descricao = Label(frame_data, text="Descricao da NFT:", font=("Times New Roman", 11), bg='#dfe3ee')
    lb_descricao.place(relx=0.07, rely=0.4)
    entry_descricao = Entry(frame_data)
    entry_descricao.place(relx=0.07, rely=0.47)

    lb_atributos = Label(frame_data, text="Atribudos da NFT:", font=("Times New Roman", 11), bg='#dfe3ee')
    lb_atributos.place(relx=0.07, rely=0.6)
    entry_atributos = Entry(frame_data)
    entry_atributos.place(relx=0.07, rely=0.67)

    lb_anexo = Label(frame_data, text="Anexo da NFT:", font=("Times New Roman", 11), bg='#dfe3ee')
    lb_anexo.place(relx=0.07, rely=0.8)
    bt_anexo= Button(frame_data, text="Anexo da NFT", font=("Times New Roman", 9), bg='#dfe3ee', command=anexo_img)
    bt_anexo.place(relx=0.07, rely=0.87)

    bt_enviar = Button(frame_data, text="Enviar", font=("Times New Roman", 13), bg='#dfe3ee', command=lambda: posting_process(entry_nome, entry_descricao, entry_atributos))
    bt_enviar.place(relx=0.7, rely=0.84)


    #Configurando o frame onde será colocada a nft
    frame_nft.place(relx=0.45, rely= 0.02, relwidth=0.5, relheight=0.96)
    lb_nft = Label(frame_nft, text="Sua NFT", font=("Times New Roman", 20), bg='#dfe3ee')
    lb_nft.place(relx=0.36, rely=0.5)

    #Configurando o frame das informações
    frame_info.place(relx=0.01, rely= 0.68, relwidth=0.4, relheight=0.30)
    lb_informacoes = Label(frame_info, text="Informações", font=("Times New Roman", 15), bg='#dfe3ee')
    lb_informacoes.place(relx=0.31, rely=0.03)


def anexo_img():
    #Por meio do explorador de arquivos, da a possibilidade do usuário escolher a imagem que deseja tornar em uma NFT 
    global path
    path=filedialog.askopenfilename(filetypes=[("Image File",'.jpg')])
   



def posting_process(entry_nome, entry_descricao, entry_atributos):
    nome = entry_nome.get()
    descricao = entry_descricao.get()
    atributos = entry_atributos.get()

    #Apresenta a imagem escolhida pelo usuário na interface criada
    imgPath = Image.open(path)
    imgPath = imgPath.resize((350,460), Image.ADAPTIVE)
    tkimage = ImageTk.PhotoImage(imgPath)
    label_2 = Label(frame_nft, image=tkimage)
    label_2.image = tkimage
    label_2.pack()
    

    #Função que realiza a conexão com o servidor da pinata, enviando os dados da NFT e retornando o IPFS_Hash da NFT
    pinata_resposne = pinata_upload(nome,descricao,atributos,path)

    #Como alternativa, devido nâo conseguir conectar o programa Brownie com a MetaMask, decidi como forma inicial em o usuário
    #   salvar a sua chave privada como uma variavel global de seu sistema
    #setx PRIVATE_KEY valor_chave_privada <--Comando que deve ser executado no termnial
    priv_key = os.getenv('PRIVATE_KEY')#Acessando a chave privada do usuário que foi salva com uma variavel de sistema

    #Cria o contrato ERC721 da NFT fornecida pelo usuário
    text_posted = deploy_and_create_contract(pinata_resposne, priv_key)
    #Informa o texto de postagem da NFT na interface criada
    label_postedText = Label(frame_info, text=text_posted, font=("Times New Roman", 11), bg='#dfe3ee', wraplength= 250)
    label_postedText.place(relx=0.03, rely=0.2)


frames()

janela.mainloop()



