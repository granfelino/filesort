## **Project: File Organizer**

**Objective:**
Create a Python program that scans a directory, identifies files by their extensions, and organizes them into subdirectories accordingly. This project will strengthen your skills in Python data structures, built-in functions, modular programming, and working with file systems.

---

### **1. Functional Requirements**

#### **1.1 Directory Scanning**

* Accept a directory path from the user.
* Scan the directory to identify all files (ignore subdirectories initially).
* Use **`os`** and **`pathlib`** for all file system operations (listing files, checking paths, creating directories, moving files).
* Ensure your solution works across different operating systems (cross-platform compatibility).

#### **1.2 File Classification**

* Determine the file type based on its extension.
* Maintain a mapping of categories to extensions (for example: images, documents, scripts).
* Files with extensions not matching any category should be grouped into an "Others" category. 

#### **1.3 File Organization**

* Create subdirectories for each category if they don’t already exist.
* Move files into their corresponding folders using **`os`** or **`pathlib`** operations.
* Avoid overwriting existing files (handle duplicates systematically).

#### **1.4 Reporting**

* Provide a summary at the end of the operation, including:

  * Total files scanned.
  * Number of files moved per category.
  * Any files that could not be moved.

---

### **2. Data Structures Usage**

* **List:** Store all files in the directory and files per category.
* **Tuple:** Represent fixed pairs of data, e.g., (filename, extension).
* **Dictionary:** Map categories to extensions and/or files.
* **Set:** Store unique file extensions or prevent duplicates in categories.

---

### **3. Built-in Functions Usage**

* **Map:** Transform a collection of files into a related property (like extensions).
* **Filter:** Select files that belong to a specific category.
* **Zip:** Pair related collections if needed (e.g., filenames and categories).
* **Enumerate:** Track iteration progress or display numbered reports.

---

### **4. Modules & Virtual Environment**

* Organize your program into **modules**:

  * Module for scanning files.
  * Module for classifying files.
  * Module for moving files.
  * Main module to coordinate program execution.
* Use a **virtual environment** to isolate project dependencies.
* Optionally, create a **requirements file** if external packages are added later.

---

### **5. Optional Enhancements**

* **Recursive scanning:** Include files from subdirectories.
* **Undo functionality:** Restore files to their original locations.
* **Custom categories:** Let users define categories and extensions.
* **Logging:** Keep a record of operations for later review.
* **GUI:** Build a graphical interface to select directories and initiate organization.

---

### **6. Deliverables**

* A fully functional Python project with:

  * Proper use of **`os`** and **`pathlib`** for all file system operations.
  * Modularized code structure.
  * Effective use of data structures and built-in functions.
  * Organized folders and files after execution.
* Summary report of operations.
* Optional documentation explaining usage and enhancements.

---
