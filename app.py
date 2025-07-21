import streamlit as st
from supabase_client import supabase 

st.set_page_config(page_title="Student Records Manager", layout="centered")
st.title("🎓 Student Records Manager")

choice = st.sidebar.radio("Choose Operation", ["Add Student", "View Students", "Update Student", "Delete Student"])

# CREATE
if choice == "Add Student":
    name = st.text_input("Name")
    email = st.text_input("Email")
    course = st.text_input("Course")
    gpa = st.number_input("GPA", min_value=0.0, max_value=4.0, step=0.01)

    if st.button("Add"):
        if not name or not email or not course:
            st.error("Please fill in all required fields.")
        else:
            data = {"name": name, "email": email, "course": course, "gpa": gpa}
            try:
                supabase.table("students").insert(data).execute()
                st.success("Student added successfully!")
            except Exception as e:
                st.error(f"Insert failed: {e}")

# READ
elif choice == "View Students":
    try:
        result = supabase.table("students").select("*").order("created_at", desc=True).execute()
        st.table(result.data)
    except Exception as e:
        st.error(f"Failed to fetch students: {e}")

# UPDATE
elif choice == "Update Student":
    try:
        students = supabase.table("students").select("id, name").execute().data
        if students:
            selected = st.selectbox("Select Student", students, format_func=lambda s: s["name"])
            new_course = st.text_input("New Course", value=selected.get("course", ""))
            new_gpa = st.number_input("New GPA", min_value=0.0, max_value=4.0, value=float(selected.get("gpa", 0.0)))

            if st.button("Update"):
                update_data = {"course": new_course, "gpa": new_gpa}
                try:
                    supabase.table("students").update(update_data).eq("id", selected["id"]).execute()
                    st.success("Student updated successfully!")
                except Exception as e:
                    st.error(f"Update failed: {e}")
        else:
            st.info("No students found.")
    except Exception as e:
        st.error(f"Failed to fetch students: {e}")

# DELETE
elif choice == "Delete Student":
    try:
        students = supabase.table("students").select("id, name").execute().data
        if students:
            selected = st.selectbox("Select Student to Delete", students, format_func=lambda s: s["name"])
            if st.button("Delete"):
                supabase.table("students").delete().eq("id", selected["id"]).execute()
                st.warning("Student deleted!")
        else:
            st.info("No students to delete.")
    except Exception as e:
        st.error(f"Delete failed: {e}")
