import ipywidgets as widgets
from . import crud_ops
from .db_connection import get_connection
from IPython.display import display
import pandas as pd

# event handler

def on_search_clicked(b):
        
    scheama = search_target.value
    where_clause = search_where.value.strip().replace("\n", " ")
    
    conn = get_connection()

    try:
        if scheama == "concepts":
            rows = crud_ops.fetch_concepts(conn, where_clause)
        elif scheama == "types":
            rows = crud_ops.fetch_types(conn, where_clause)
        elif scheama == "problems":
            rows = crud_ops.fetch_problems(conn, where_clause)
    finally:
        conn.close()

    df = pd.DataFrame(rows, columns=rows[0].keys()) if rows else pd.DataFrame()

    with search_result:
        search_result.clear_output()
        print(
            f"Search Results: {len(rows)} rows found.",
        )

    with search_detail:
        search_detail.clear_output()
        if not df.empty:
            display(df)
        else:
            print("No details to display.")


def on_new_clicked(b):
    pass  # To be implemented   


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

search_where = widgets.Textarea(
    description="WHERE:",
    placeholder="e.g.\nname LIKE '%normal%'\nyear = 2023",
    layout=widgets.Layout(width="900px", height="80px")
)

search_button = widgets.Button(
    description="Search",
    button_style="primary",
    icon="search"
)

search_control = widgets.HBox([
widgets.HBox([search_target, search_button]),
              search_where
])


# 1-B. search_result & search_detail
search_result = widgets.Output(
    layout=widgets.Layout(border="1px solid #ddd", padding="8px", width="900px")
)

search_detail = widgets.Output(
    layout=widgets.Layout(border="1px solid #ddd", padding="8px", width="900px")
)



# 2. new UI components


# 2-A. new_control
new_target = widgets.Dropdown(
    options=[
        ("Concepts", "concepts"),
        ("Types", "types"), 
        ("Problems", "problems"),
    ],
    description="Schema:",
    layout=widgets.Layout(width="250px")
)

new_values = widgets.Textarea(
    description="Values:",
    placeholder="e.g.\nname='New Concept', description='Description here'",
    layout=widgets.Layout(width="900px", height="80px")
)

new_button = widgets.Button(
    description="Add New",
    button_style="success",
    icon="plus"
)

new_control = widgets.HBox([
    widgets.HBox([new_target, new_button]),
    new_values
])

# 2-B. new_result
new_result = widgets.Output(
    layout=widgets.Layout(border="1px solid #ddd", padding="8px", width="900px")
)


# event binding
search_button.on_click(on_search_clicked)
new_button.on_click(on_new_clicked)