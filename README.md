# 📶 Mahigo PassView

A clean, responsive web interface inspired by Streamlit to securely view and manage saved Wi-Fi profiles and passwords extracted from your Linux environment.

This project is optimized for deployment as a static site on **Tencent Cloud EdgeOne Pages**.

---

## 🏗️ Architecture & Security Design

Because standard web browsers operate inside a highly secure sandbox environment, client-side JavaScript **cannot directly run system commands** like `nmcli` or read local Linux system directories. 

To overcome this securely, **Mahigo PassView** splits the process into two layers:
1. **Local Exporter (`export.py`):** A lightweight local Python utility that securely reads `nmcli` connections and creates a structured, static `data.json` package file.
2. **Cloud Dashboard (`index.html`):** A beautiful, high-performance static frontend hosted on EdgeOne Pages that loads and presents your static JSON logs.

---

## 📁 Repository Structure

Ensure your project folder contains the following core files before pushing to deployment:

```text
mahigo-passview/
├── index.html       # The EdgeOne Pages static frontend dashboard
├── data.json        # Your exported network configuration matrix
└── export.py        # Local Python extraction script (Do not deploy this)
```

---

## 🚀 Setup & Deployment Guide

### Step 1: Extract Local Wi-Fi Profiles
Run the extraction utility locally on your Linux machine to package your saved profiles:

```bash
python3 export.py
```

*Note: Depending on your system's `nmcli` permissions, you might need to run the script with elevated privileges (`sudo python3 export.py`) to correctly extract secured `.psk` strings.*

### Step 2: Push Data to GitHub
Initialize your repository and commit both the dashboard layout and your newly populated data file:

```bash
git init
git add index.html data.json
git commit -m "feat: initial static dashboard bundle"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

### Step 3: Host on Tencent Cloud EdgeOne Pages
1. Log in to the **Tencent Cloud Console** and navigate to **EdgeOne**.
2. Select **Pages** from the sidebar menu and click **Create Project**.
3. Link your GitHub account and select your project repository.
4. Configure the **Build Settings**:
   * **Framework Preset:** `None` / `Static Site`
   * **Build Command:** *(Leave Blank)*
   * **Output Directory:** `.` (or the directory containing your `index.html`)
5. Click **Save and Deploy**. EdgeOne will distribute your project globally across its edge network nodes.

---

## 🔒 Security Disclaimer
The `data.json` file contains **plain-text Wi-Fi passwords**. If you push this file to a public GitHub repository, your private passwords will be visible to anyone. 
* **Always** keep your target GitHub repository set to **Private**.
* Only grant access tokens to trusted deployment environments.
