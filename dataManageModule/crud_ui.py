import ipywidgets as widgets

# 1. search UI components

# 1-A serach_control
search_target = widgets.Dropdown(
    options=[
        ("Concepts", "concepts"),
        ("Types", "types"),
        ("Problems", "problems"),
    ],
    description="Target:",
    layout=widgets.Layout(width="250px")
)

search_input = widgets.Text(
    description="Keyword:",
    placeholder="name, year, note_path ...",
    layout=widgets.Layout(width="400px")
)

search_button = widgets.Button(
    description="Search",
    button_style="primary",
    icon="search"
)

search_control = widgets.HBox([
    search_target,
    search_input,
    search_button
])


# 1-B. search_result & search_detail
search_result = widgets.Output(
    layout=widgets.Layout(border="1px solid #ddd", padding="8px", width="900px")
)

search_detail = widgets.Output(
    layout=widgets.Layout(border="1px solid #ddd", padding="8px", width="900px")
)

