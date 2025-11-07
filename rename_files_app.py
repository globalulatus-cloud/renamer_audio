import os
import streamlit as st

st.title("Bulk File Renamer")

# Folder path input
folder_path = st.text_input("Enter folder path:")

def rename_files(folder, base_name):
    if not os.path.isdir(folder):
        st.error("Invalid folder path. Please check and try again.")
        return

    files = sorted(os.listdir(folder))
    if not files:
        st.warning("No files found in the given folder.")
        return

    renamed_count = 0
    for i, file_name in enumerate(files, start=1):
        old_path = os.path.join(folder, file_name)
        if os.path.isfile(old_path):
            ext = os.path.splitext(file_name)[1]
            new_name = f"{base_name}_{i:03d}{ext}"
            new_path = os.path.join(folder, new_name)
            os.rename(old_path, new_path)
            renamed_count += 1
    st.success(f"Renamed {renamed_count} files to {base_name}_### format successfully.")


# Buttons for renaming
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Rename as Embedded"):
        rename_files(folder_path, "Embedded")

with col2:
    if st.button("Rename as Server"):
        rename_files(folder_path, "Server")

with col3:
    if st.button("Rename as WUW"):
        rename_files(folder_path, "WUW")
