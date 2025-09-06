# Grazioso Salvare Animal Rescue Dashboard

This project is a **data dashboard** that tracks rescue animals and evaluates their suitability for different types of rescue work (e.g., Water Rescue, Mountain/Wilderness Rescue, Disaster/Tracking).  

It was built to demonstrate **Python programming, data visualization, and interactive dashboard development**.

---

## 📌 Features
- **Data Filtering** → Select rescue types from a dropdown menu to filter animals.  
- **Dynamic Table** → Displays filtered animal data (breed, age).  
- **Charts** → Visualizes breed distribution by rescue type.  

---

## 🛠 Tech Stack
- **Language:** Python  
- **Frameworks:** Dash (Plotly)  
- **Libraries:** Pandas  

---

## 📂 Project Structure
```text
grazioso-salvare-dashboard/
 ├── app.py              # Main dashboard app
 ├── requirements.txt    # Dependencies
 ├── data/
 │   └── animals.csv     # Sample dataset
 └── README.md

🚀 How to Run

Clone the repo: git clone https://github.com/collynk/grazioso-salvare-dashboard.git
cd grazioso-salvare-dashboard

Install dependencies:
pip install -r requirements.txt

Run the app:
python app.py

Open the dashboard in your browser:
http://127.0.0.1:8050/


🎓 Academic Context

This project was completed as part of the SNHU Computer Science program.
It demonstrates:

Building interactive dashboards in Python.

Filtering and visualizing datasets.

Clear documentation and reproducibility.

📈 Future Improvements

Add MongoDB integration for live CRUD operations.

Include map visualization (Leaflet.js).

Deploy dashboard to cloud (Heroku, Render, AWS).
