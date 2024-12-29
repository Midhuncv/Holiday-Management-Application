# Holiday-Management-Application

# Holiday Finder Application

A full-stack web application that fetches and displays holidays for a specific country and year using the Calendarific API. The application is built with **Django** for the backend and **React** for the frontend.

---

## Features

1. **Search Holidays by Country and Year**

   - Users can search holidays by entering the country code (ISO-2 format) and a specific year.

2. **Interactive UI**

   - A colorful and user-friendly interface built using Tailwind CSS.

3. **API Integration**

   - Fetches data from the [Calendarific API](https://calendarific.com/).

4. **Error Handling**

   - Gracefully handles errors such as invalid inputs, missing API keys, or empty responses.

5. **Caching**
   - Uses Django's caching framework to store API responses for faster repeated queries.

---

## Technologies Used

### Backend

- **Django**: Python-based web framework for building robust APIs.
- **Django Rest Framework (DRF)**: For API creation.
- **django-cors-headers**: To handle CORS between frontend and backend.

### Frontend

- **React**: For building a responsive user interface.
- **Axios**: For making API calls to the backend.
- **Tailwind CSS**: For styling the UI.

---

## Setup Instructions

### Backend

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd backend
   ```
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate

pip install -r requirements.txt

CALENDARIFIC_API_KEY=your_api_key_here
DEBUG=True

python manage.py runserver # with you system ip address eg 192.168.0.104:8000

Frontend
Navigate to the Frontend Directory

cd frontend

npm install

axios.defaults.baseURL = "http://192.168.0.104:8000/";

npm start

##Run the Application
python manage.py runserver
npm start

Register at Calendarific to get your API key.

Add the API key to the .env file in the backend:

CALENDARIFIC_API_KEY=your_api_key_here
