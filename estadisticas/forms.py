from django import forms

orden_estadisticas = (
    ("-nombre", "Nombre ↑"),
    ("nombre", "Nombre ↓"),
    ("-tipo", "Tipo ↑"),
    ("tipo", "Tipo ↓"),
    ("-pais", "País ↑"),
    ("pais", "País ↓"),
    ("-nivel", "Nivel ↑"),
    ("nivel", "Nivel ↓"),
    ("-batallas", "Batallas ↑"),
    ("batallas", "Batallas ↓"),
    ("-victorias", "Victorias ↑"),
    ("victorias", "Victorias ↓"),
    ("-experiencia", "Experiencia ↑"),
    ("experiencia", "Experiencia ↓"),
    ("-subtotal", "Subtotal ↑"),
    ("subtotal", "Subtotal ↓"),
    ("-win8", "Win8 ↑"),
    ("win8", "Win8 ↓"),
    ("-total", "Total ↑"),
    ("total", "Total ↓"),
    ("-garaje", "Garaje"),
    ("-premium", "Premium"),
)


class EstadisticasForm(forms.Form):
    lista_uno = forms.ChoiceField(
        label='Filtro 1', choices=orden_estadisticas)
    lista_dos = forms.ChoiceField(
        label='Filtro 2', choices=orden_estadisticas)
    lista_tres = forms.ChoiceField(
        label='Filtro 3', choices=orden_estadisticas)
