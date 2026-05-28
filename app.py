import streamlit as st

from backend import (
    init_tasks,
    add_task,
    get_tasks,
    mark_task_done
)

# =====================================
# INITIALISATION
# =====================================

init_tasks()

# =====================================
# INTERFACE
# =====================================

st.title("Ma TodoList")

# Ajouter une tâche
new_task = st.text_input("Ajouter une tâche")

if st.button("Ajouter"):

    add_task(new_task)

# =====================================
# AFFICHAGE DES TÂCHES
# =====================================

st.subheader("Liste des tâches")

tasks = get_tasks()

for i, task in enumerate(tasks):

    col1, col2 = st.columns([0.8, 0.2])

    with col1:

        status = (
            "Terminé"
            if task["done"]
            else "À faire"
        )

        st.write(
            f"{status} - {task['task']}"
        )

    with col2:

        if not task["done"]:

            if st.button(
                "Marquer comme fait",
                key=f"done_{i}"
            ):

                mark_task_done(i)
                st.rerun()