![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Regex](https://img.shields.io/badge/Regex-FF9800?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

# ⌨️ Python Typing Speed Tester
*Measure your typing speed and accuracy with persistent high scores and averages*



---

## 🎞 Demo

![Typing Speed Tester Demo](assets/demo.gif)

---

## ⚙️ Key Features

### 👤 User Management
- Create a username once (validated via **Regex**)
- Automatically recognized on subsequent runs  
![Username Creation](assets/screenshot-username.png)

---

### 📏 Text Length Selection
- Choose between **short**, **medium**, and **long** text samples  
![Text Length Selection](assets/screenshot-length.png)

---

### ⌨️ Typing Test
- Take a typing test with **short**, **medium**, or **long** text options
- Measures speed and accuracy in real-time

![Typing Test](assets/typing.gif)

---

### 📊 Results & Statistics
- Displays:
  - **Typing Speed** in Words Per Minute (WPM)
  - **Accuracy** as a percentage
  - **Highscores** & **Averages** from previous sessions  
![Results](assets/screenshot-results.png)

---

### 🗄️ Database Persistence
- **SQLite** integration for:
  - User storage
  - Test results (speed & accuracy)
- High scores and averages are automatically calculated  

---

### 🧠 Input Validation
- Username validation (only letters, numbers & underscores; 3–16 chars)
- Text length selection validation (must be 1, 2 or 3)

**Username:**
![Screenshot of validation for username](assets/screenshot-validation-username.png)

**Text length:**
![Screenshot of validation for text length selection](assets/screenshot-validation-length.png)

---

## 🛠 Technology Stack

- **Python** – Core programming language  
- **Regex** – Input validation  
- **SQLite** – Local database for user and score storage  

---

## 📚 Project Context

> This project was created during my training at **gibb** as part of the *Modul 122* course.  
>  
> The main goal was to learn **Python programming**, **Regex validation**, and **SQLite database integration**.  
>  
> I previously built a similar program in **PowerShell**, but this Python version adds:
> - Database persistence
> - Regex-based input validation
> - Improved console design  

---

## 🚀 How to Run the Project

```bash
# 1. Clone the repository
git clone https://github.com/lorisjon/TypingSpeedTester.git

# 2. Navigate into the project folder
cd TypingSpeedTester

# 3. Run the program
python tipptest.py
```

---

## 👤 About the Developer

> I am an aspiring software developer with an interest in **console tools, data persistence, and user experience**.  
>  
> This project helped me strengthen my Python fundamentals and introduced me to SQLite database integration and Regex validation.  
>  
<!-- > 🔗 [View my Portfolio](https://your-portfolio-url.com) -->
