import ipywidgets as widgets

# event handler

def on_search_clicked(b):
    with search_result:
        search_result.clear_output()
        print(
            f"Searching in [{search_target.value}] "
            f"for keyword: '{search_input.value}'"
        )


# 1. search UI components

# 1-A search_control
search_target = widgets.Dropdown(
    options=[
        ("Concepts", "concepts"),
        ("Types", "types"),
        ("Problems", "problems"),
    ],
    description="Schema:",
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

search_button.on_click(on_search_clicked)


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


