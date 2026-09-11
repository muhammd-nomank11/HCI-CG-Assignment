# HCI Lab Assignment - Image Processing & Display Metrics

* **Name:** Muhammad Noman
* **Roll No:** 2K24/CSE/105
* **Program:** BS Computer Science (Part-III)

---

## Project Structure
* `code/` — Contains Python implementation scripts for all four lab tasks:
  * `task_1_DPI_Calculator.py`
  * `task_2_Synthetic_Matrix.py`
  * `task_3_Channel_Isolation.py`
  * `task_4_Downsampling.py`
* `outputs/` — Contains terminal execution screenshots and generated Matplotlib visualization figures (`Figure_1`, `Figure_2`).

---

## Lab Tasks Overview
1. **Task 1: Display Pixel Density (PPI/DPI) Calculator**
2. **Task 2: Environment Setup & Synthetic Image Matrix Creation**
3. **Task 3: Channel Slicing & Isolation**
4. **Task 4: Spatial Downsampling & Pixelation via Striding**

---

## Lab Short Answer
**Q: Why does adding an Alpha channel (RGBA) increase an image array’s memory consumption by 33% compared to standard RGB?**

An RGB image uses 3 channels per pixel, while an RGBA image uses 4 channels (adding the Alpha channel). Since the pixel count, bit depth, and dimensions remain identical, moving from 3 channels to 4 increases the total data size by a factor of 4/3 (or 1.333...), which represents a 33.33% increase in memory consumption.