import flet as ft

def main(page: ft.Page):
    page.title = "Teste Flet - Paciência"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    def ao_clicar(e):
        texto.value = "Flet rodando perfeitamente!"
        page.update()

    texto = ft.Text("Se você está vendo isso, o Flet está pronto para a prova.")
    botao = ft.Button("Clique para validar", on_click=ao_clicar)

    page.add(texto, botao)

ft.run(main)