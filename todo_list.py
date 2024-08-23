import streamlit as st

# TO-DO APP
st.title("TO-DO LIST")

# Tasks list
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# New task input
st.header("Enter New Task")
new_task = st.text_input("New task")

if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append({"task": new_task, "completed": False})
        st.success(f"Task added: {new_task}")
    else:
        st.warning("Please enter a task")

# List tasks and mark them as completed
st.header("Your Tasks")

if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.1, 0.9])
        task["completed"] = col1.checkbox("", value=task["completed"], key=f"task_{i}")
        col2.write(task["task"])

    # Delete completed tasks
    if st.button("Delete Completed Tasks"):
        st.session_state.tasks = [task for task in st.session_state.tasks if not task["completed"]]
        st.success("Completed tasks have been deleted.")
else:
    st.write("Your to-do list is empty.")

