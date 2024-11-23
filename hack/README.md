### **Summary of Commands**

1. **Clone the Django project from GitHub:**
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Ensure Python 3.10 or higher is installed:**
   Check your Python version:
   ```bash
   python --version
   ```
   If you don't have Python 3.10 or higher, please install the appropriate version from the [official Python website](https://www.python.org/downloads/).

3. **Create a `venv` folder outside the project directory for the virtual environment:**
   Go back to the parent directory of your project and create a `venv` folder:
   ```bash
   cd ..
   python -m venv venv
   ```

4. **Activate the virtual environment:**
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Linux/macOS:
     ```bash
     source venv/bin/activate
     ```

5. **Install dependencies:**
   ```bash
   cd your-repository  # Go back into the project directory if needed
   pip install -r requirements.txt
   ```

6. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

7. **Run the server:**
   ```bash
   python manage.py runserver
   ```
