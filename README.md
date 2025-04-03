# FireDucks: Supercharging Pandas for Blazing-Fast Data Analysis

FireDucks is a high-performance alternative to Pandas, designed to accelerate data processing using multithreading, JIT compilation, and lazy evaluation. This repository contains a benchmarking script to compare FireDucks with Pandas for common data operations.

## 🚀 Features
- **Multithreading** for faster computations.
- **JIT Compilation** to optimize performance.
- **Lazy Evaluation** to efficiently handle large datasets.
- **Seamless Integration** with Pandas API.

## 📂 Project Structure
```
FireDucks-Performance/
│-- Fireducks.py  # Benchmarking script for FireDucks vs Pandas
│-- .env          # Configuration file (dataset path)
│-- README.md     # Documentation
│-- .gitignore    # Ignore unnecessary files
```

## 🛠️ Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/FireDucks-Performance.git
   cd FireDucks-Performance
   ```

2. **Install Dependencies**
   ```bash
   pip install firedf python-dotenv pandas
   ```

3. **Update Dataset Path (Optional)**  
   Edit the `.env` file if your dataset is in a different location:
   ```env
   DATASET_PATH=your_dataset.csv
   ```

## 📊 Running the Benchmark
Run the script to compare FireDucks and Pandas:
```bash
python Fireducks.py
```

## 📝 License
This project is open-source and free to use.

---
🔥 Speed up your data processing with FireDucks and unlock high-performance analytics!
