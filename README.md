[3~# 🚀 Python Log Monitor

## 📌 Overview
This is a simple, python log monitor.

It simulates:
* a Python application that generates logs
* a monitoring script that scans logs and detects errors

This helps you understand how real systems produce logs and how engineers monitor and detect issues.

## ⚙️ Features
* Generate application logs
* Read and process logs
* Detect error patterns (ERROR, CRITICAL, timeout, failed)
* Write alerts to a file
* Easy to extend

## ▶️ How It Works
1. `app.py` generates logs continuously
2. Logs are written to `logs/app.log`
3. `monitor.py` reads the logs
4. If errors are found, they are saved in `output/alerts.txt`

## ▶️ How to Run

**Step 1: Run the app (generate logs)**
```bash
python src/app.py
```

**Step 2: Run the monitor (scan logs)**
```bash
python src/monitor.py
```

## 🧪 Example

**app.log**
```
2026-03-19 20:00:01 INFO Server started
2026-03-19 20:00:03 ERROR Database connection failed
```

**alerts.txt**
```
2026-03-19 20:00:03 ERROR Database connection failed
```

## 🧠 What I Learned
* 

## 🧑‍🤝‍🧑 Team Workflow (IMPORTANT)
We use a simple Pull Request (PR) workflow.

### Rules
* ❌ Do NOT push directly to `main`
* ✅ Always create a new branch
* ✅ Create a Pull Request (PR)

### Steps
```bash
# 1. Create a branch
git checkout -b feature/your-feature-name

# 2. Make changes
git add .
git commit -m "your message"

# 3. Push
git push origin feature/your-feature-name

# 4. Open PR on GitHub
# 5. Review → Merge
```

### Simple Flow
```
Work → Branch → Push → PR → Review → Merge
```

## 📦 Requirements
```
# No external dependencies required
# (optional: pytest for testing)
```

## 🔮 Future Improvements
* real-time monitoring (like `tail -f`)
* alert thresholds (e.g., too many errors)
* Slack/Webhook alerts
* Prometheus + Grafana integration
* Docker and Kubernetes

## 👨‍💻 Author
Sandip Kharel

*(Add your names here)*
