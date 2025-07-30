# 🌦️ Weather Checker Application

יישום אינטראקטיבי הבנוי ב־**Streamlit**, המאפשר למשתמשים לבדוק את מזג האוויר הנוכחי ותחזית שבועית לפי עיר, תוך שימוש בנתונים בזמן אמת מ־[OpenWeatherMap API](https://openweathermap.org/).

---

## 🚀 תכונות עיקריות

- 🔎 קבלת נתוני מזג אוויר לפי שם עיר
- 🌡️ הצגת טמפרטורה, לחץ, לחות ומהירות רוח
- 📆 תחזית שבועית עם טמפ' מקס/מינימום ותיאור
- 📍 שימוש בקואורדינטות (lat/lon) עבור תחזית מדויקת
- 📊 ממשק רספונסיבי עם `st.columns()` להצגה נוחה
- 🧠 טעינת משתני סביבה מ־`.env` באופן מאובטח
- 🔐 אין שמירה של מפתחות API בקוד
- 📦 מנוהל עם **Poetry**

---

## 🖥️ הדגמת שימוש

```bash
 poetry run streamlit run app.py
```

| פרמטר            | דוגמה                |
|------------------|----------------------|
| 🌡️ טמפרטורה     | `22.5 °C`            |
| 💨 מהירות רוח    | `5.5 m/s`            |
| 📅 יום תחזית     | `Monday, July 29`    |
| 🧾 תיאור         | `Scattered Clouds`   |

---

## 🛠️ טכנולוגיות בשימוש

- **Python 3.10+**
- [Streamlit](https://streamlit.io/)
- [OpenWeatherMap API](https://openweathermap.org/api)
- `requests`
- `python-dotenv`
- `datetime`

---

## 📁 מבנה הפרויקט

```
weather-checker/
├──src/
    ├── weather-checker/
    └── main.py              # קובץ ראשי של האפליקציה
├── .env                # משתני סביבה (מפתח API)
├── .gitignore          # קבצים לא למעקב Git
├── README.md           # תיעוד הפרויקט
└── pyproject.toml      # הגדרות Poetry

```

---

## 🧪 הוראות התקנה והרצה

### 1. שיבוט הפרויקט

```bash
git clone https://github.com/iShmuel/weather_app.git
cd weather-checker
```

### 2. התקנת הסביבה עם Poetry

```bash
poetry install
poetry shell
```

### 3. יצירת קובץ `.env`

```env
WEATHER_API=your_api_key_here
```

### 4. הרצת האפליקציה

```bash
streamlit run app.py
```

---

## 🔑 קבלת מפתח OpenWeatherMap

1. עבור ל־[https://openweathermap.org/api](https://openweathermap.org/api)
2. בצע הרשמה / התחברות
3. צור מפתח API חדש
4. הדבק אותו בקובץ `.env` שלך

---

## 📚 מטרות מתקדמות (Stretch Goals)

### ✅ הצגת זמן מקומי בעיר שנבחרה
שימוש בספרייה `pytz` להצגת השעה המקומית של העיר.

### ✅ הגדרות נשמרות ב־JSON
שמירת העדפות משתמש כמו עיר ברירת מחדל, יחידות טמפרטורה וכו'.

### ✅ מפות ואייקונים
הצגת מפות עם `folium` ואייקוני מזג אוויר מ־OpenWeatherMap.

---

## 🧾 דוגמת תגובה מה־API (מקוצרת)

```json
{
  "coord": { "lon": -0.13, "lat": 51.51 },
  "weather": [{ "description": "light rain", "icon": "10d" }],
  "main": { "temp": 20.5, "humidity": 60, "pressure": 1012 },
  "wind": { "speed": 4.6 },
  "dt": 1628167200,
  "name": "London"
}
```

---

## 💡 הנחיות לתרומה

Pull Requests יתקבלו בברכה! נשמח לשיפורים ב־UI, תחזית טובה יותר, קאשינג או שילוב APIs נוספים.

---

## 📜 רישיון

הפרויקט פתוח וזמין תחת רישיון MIT.
