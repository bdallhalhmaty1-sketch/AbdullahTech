import flet as ft
import webbrowser

PHONE = "967783044700"

def main(page: ft.Page):
    page.title = "Abdullah Tech"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    def whatsapp(e):
        webbrowser.open(f"https://wa.me/{PHONE}")

    page.add(
        ft.Text(
            "Abdullah Tech",
            size=30,
            weight=ft.FontWeight.BOLD,
        ),
        ft.Divider(),
        ft.Card(
            content=ft.Container(
                padding=15,
                content=ft.Column(
                    controls=[
                        ft.Text("📱 برمجة تطبيقات", size=20),
                        ft.Text("🔧 صيانة تقنية", size=20),
                        ft.Text("💻 حلول برمجية", size=20),
                    ]
                ),
            )
        ),
        ft.Container(height=20),
        ft.ElevatedButton(
            "تواصل عبر واتساب",
            icon=ft.Icons.CHAT,
            on_click=whatsapp,
        ),
    )

ft.app(target=main)
