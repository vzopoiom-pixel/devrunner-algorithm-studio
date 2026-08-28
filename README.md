# ⚡ DevRunner Studio & Full-Stack Portfolio

An interactive, high-performance developer workbench and multi-language algorithm execution studio built for high-throughput code benchmarking, data structures exploration, and modern full-stack web applications.

---

## 🎯 Flagship Projects Included

1. 💻 **DevRunner Studio (`Java 21` / `Python 3.12` / `SQL` / `C++ 20` / `TypeScript`)**
   - Interactive multi-language IDE & algorithm runner.
   - Built-in benchmarks: Dijkstra's Shortest Path, LRU Cache, High-Frequency Trade Orderbook, Binary Tree Traversal, Complex SQL Aggregations.
   - Real-time execution telemetry: Execution time (ms), memory footprint (KB), and status diagnostics.

2. 📊 **SaaS Telemetry & Analytics Platform**
   - High-contrast analytical dashboard with live revenue metrics, churn tracking, and user activity timelines.

3. 📦 **VaporCore Inventory & Recipe Database**
   - Retail & warehouse management with multi-parametric flavor/SKU filtering, low-stock threshold alerts, and JSON export.

---

## 🚀 Quick Start Guide

### 📋 Prerequisites
- **Node.js**: v18.0.0 or higher ([Download Node.js](https://nodejs.org/))
- **Git**: ([Download Git](https://git-scm.com/))

---

### 1️⃣ Clone the Repository
    git clone https://github.com/vzopoiom-pixel/devrunner-algorithm-studio.git

### 2️⃣ Navigate into the Project Folder
    cd devrunner-algorithm-studio

> ⚠️ **Windows Note:** Ensure your path doesn't contain special characters like `&` or `#` (e.g. use `C:\Users\YourUser\Desktop\portfolio`).

### 3️⃣ Install Dependencies
    npm install

### 4️⃣ Start Development Server
    npm run dev

The application will start immediately at: **http://localhost:3000**

### 5️⃣ Build for Production (Optional)
    npm run build

---

## 🛠️ Summary of All CLI Commands

| Command | Description |
| :--- | :--- |
| `git clone https://github.com/vzopoiom-pixel/devrunner-algorithm-studio.git` | Download the project from GitHub |
| `cd devrunner-algorithm-studio` | Enter the project directory |
| `npm install` | Install all required packages & dependencies |
| `npm run dev` | Launch local development server (localhost:3000) |
| `npm run build` | Compile optimized production bundle to dist/ |

---

## 🔧 Troubleshooting & Common Fixes

<details>
<summary><b>1. Error: ENOENT: no such file or directory, open 'package.json'</b></summary>

**Cause:** You are running `npm install` from `C:\Windows\system32` instead of inside the project folder.  
**Fix:**
```powershell
cd C:\Users\RADIK\Desktop\portfolio
npm install
