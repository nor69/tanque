from django import forms

orden_repeticiones = (
    ("-nombre", "Nombre ↑"),
    ("nombre", "Nombre ↓"),
    ("-tipo", "Tipo ↑"),
    ("tipo", "Tipo ↓"),
    ("-pais", "País ↑"),
    ("pais", "País ↓"),
    ("-nivel", "Nivel ↑"),
    ("nivel", "Nivel ↓"),
    ("-destruidos", "Destruidos ↑"),
    ("destruidos", "Destruidos ↓"),
    ("-causado", "Causado ↑"),
    ("causado", "Causado ↓"),
    ("-bloqueado", "Bloqueado ↑"),
    ("bloqueado", "Bloqueado ↓"),
    ("-detectado", "Detectado ↑"),
    ("detectado", "Detectado ↓"),
    ("-aturdimiento", "Aturdimiento ↑"),
    ("aturdimiento", "Aturdimiento ↓"),
    ("-premium", "Premium"),
)


class RepeticionesForm(forms.Form):
    lista_uno = forms.ChoiceField(
        label='Filtro 1', choices=orden_repeticiones)
    lista_dos = forms.ChoiceField(
        label='Filtro 2', choices=orden_repeticiones)
    lista_tres = forms.ChoiceField(
        label='Filtro 3', choices=orden_repeticiones)
