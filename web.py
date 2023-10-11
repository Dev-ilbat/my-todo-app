import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("My To-Do App")
st.subheader("This is my To-Do App")
st.write("This app is created to increase your productivity")

for index, todo in enumerate(todos):  # for every item in the todos list, we create a checkbox
    checkbox = st.checkbox(todo, key=todo)  # creates a unique key for every to-do
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]  # delete from session state dictionary
        st.experimental_rerun()

st.session_state["new_todo"] = ""
st.text_input(label="New Todo", placeholder="Add a new To-Do",
              on_change=add_todo, label_visibility='hidden', key='new_todo')