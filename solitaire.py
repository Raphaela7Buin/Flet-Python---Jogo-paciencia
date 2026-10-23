import flet as ft


class Solitaire:
    def __init__(self):
        self.start_positions = {}  # Guarda a posição original de cada carta do grupo


def main(page: ft.Page):
    # Configuração de título e margens da página
    page.title = "Jogo de Cartas - Paciência"
    page.padding = 0

    def get_dragged_group(card):
        """Retorna a carta clicada e todas as cartas abaixo dela na mesma pilha."""
        if hasattr(card, "current_slot") and card.current_slot:
            slot = card.current_slot
            index = slot.cards.index(card)
            return slot.cards[index:]
        return [card]

    def place_group(cards_group, target_slot):
        """Posiciona todo o grupo de cartas no novo slot em ordem de cascata."""
        source_slot = getattr(cards_group[0], "current_slot", None)

        for card in cards_group:
            if source_slot:
                source_slot.cards.remove(card)

            card.top = target_slot.top + (len(target_slot.cards) * 25)
            card.left = target_slot.left

            target_slot.cards.append(card)
            card.current_slot = target_slot

    def bounce_back_group(game, cards_group):
        """Devolve todas as cartas do grupo para suas posições originais."""
        for card in cards_group:
            if card in game.start_positions:
                card.top = game.start_positions[card]["top"]
                card.left = game.start_positions[card]["left"]

    def start_drag(e: ft.DragStartEvent):
        dragged_group = get_dragged_group(e.control)
        solitaire.start_positions.clear()

        for card in dragged_group:
            controls.remove(card)
            controls.append(card)
            solitaire.start_positions[card] = {"top": card.top, "left": card.left}

        page.update()

    def drag(e: ft.DragUpdateEvent):
        dragged_group = get_dragged_group(e.control)

        for card in dragged_group:
            card.top = max(0, card.top + e.local_delta.y)
            card.left = max(0, card.left + e.local_delta.x)
            card.update()

    def drop(e: ft.DragEndEvent):
        dragged_group = get_dragged_group(e.control)
        lead_card = dragged_group[0]
        placed = False

        for slot in slots:
            if getattr(lead_card, "current_slot", None) == slot:
                continue

            target_top = slot.top + (len(slot.cards) * 25)

            if abs(lead_card.top - target_top) < 35 and abs(lead_card.left - slot.left) < 35:
                place_group(dragged_group, slot)
                placed = True
                break

        if not placed:
            bounce_back_group(solitaire, dragged_group)

        for card in dragged_group:
            card.update()

    # 1. TRÊS SLOTS EM BRANCO
    slot1 = ft.Container(
        width=70, 
        height=100, 
        left=300, 
        top=40, 
        border=ft.Border.all(2, ft.Colors.WHITE_38),
        border_radius=6
    )
    slot2 = ft.Container(
        width=70, 
        height=100, 
        left=380, 
        top=40, 
        border=ft.Border.all(2, ft.Colors.WHITE_38),
        border_radius=6
    )
    slot3 = ft.Container(
        width=70, 
        height=100, 
        left=460, 
        top=40, 
        border=ft.Border.all(2, ft.Colors.WHITE_38),
        border_radius=6
    )

    slot1.cards = []
    slot2.cards = []
    slot3.cards = []

    slots = [slot1, slot2, slot3]

    # 2. TRÊS CARTAS COM IMAGENS
    url_carta1 = "https://account.impacta.edu.br/res/files/carteirinha-inova-fotos/1/b0f11bc9ad08aae86d9850913b54995c9e712fdf2f07e72d1c486f595120d7d4-foto.png"
    url_carta2 = "https://account.impacta.edu.br/res/files/carteirinha-inova-fotos/1/186b9ea66dc7dc24b6d7299fe5ddef92708ea3dfa3814a66c0a31e7153503d16-foto.png"
    url_carta3 = "https://account.impacta.edu.br/res/files/carteirinha-inova-fotos/1/eebb9db113de44341c83e9fa5857ce5efeddc4bb89ba48a825b7bc6c70b80b41-foto.png"

    card1 = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=5,
        on_pan_start=start_drag,
        on_pan_update=drag,
        on_pan_end=drop,
        left=40,
        top=40,
        content=ft.Container(
            content=ft.Image(src=url_carta1, width=70, height=100, fit="cover"),
            border_radius=6,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        ),
    )
    card1.current_slot = None

    card2 = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=5,
        on_pan_start=start_drag,
        on_pan_update=drag,
        on_pan_end=drop,
        left=120,
        top=40,
        content=ft.Container(
            content=ft.Image(src=url_carta2, width=70, height=100, fit="cover"),
            border_radius=6,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        ),
    )
    card2.current_slot = None

    card3 = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=5,
        on_pan_start=start_drag,
        on_pan_update=drag,
        on_pan_end=drop,
        left=200,
        top=40,
        content=ft.Container(
            content=ft.Image(src=url_carta3, width=70, height=100, fit="cover"),
            border_radius=6,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        ),
    )
    card3.current_slot = None

    solitaire = Solitaire()

    controls = [*slots, card1, card2, card3]

    # 3. FUNDO DINÂMICO (Usando a instância ft.Alignment diretamente)
    background_container = ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1.0, -1.0),  # Canto superior esquerdo
            end=ft.Alignment(1.0, 1.0),     # Canto inferior direito
            colors=[
                "#0d3b23",
                "#1b5e20",
                "#0a2918",
            ],
        ),
        content=ft.Stack(controls=controls, width=1000, height=600),
    )

    page.add(background_container)


ft.run(main)