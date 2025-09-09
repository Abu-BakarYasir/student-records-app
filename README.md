# 🎓 Student Records Manager

This is A Basic simple CRUD web app built with **Streamlit** and **Supabase** for managing student records.

## 🚀 Features

- **Add Student**: Input name, email, course, and GPA.
- **View Students**: Displays all students in a table.
- **Update Student**: Modify existing student’s course and GPA.
- **Delete Student**: Remove student from the records.

## 🧰 Tech Stack

- **Frontend**: Streamlit
- **Backend/Database**: Supabase (PostgreSQL)
- **Python Libraries**: `streamlit`, `supabase`, `python-dotenv`

## ⚙️ Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/student-records-app.git
   cd student-records-app
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**  
   Create a `.env` file with:
   ```
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_anon_key
   ```

4. **Run the App**  
   ```bash
   streamlit run app.py
   ```

## 📁 Folder Structure

```
├── app.py                 # Streamlit UI
├── supabase_client.py     # Supabase connection
├── .env                   # Secrets
├── requirements.txt       # Python dependencies
└── .gitignore             # Files to ignore in git
```

Screenshots:
<img width="1353" height="634" alt="3" src="https://github.com/user-attachments/assets/ce202542-9c48-47e0-962f-de4da3202963" />

