
# ```python
# --------------------------------------------------------------
# 🧱 Collection Data-Types in Python (List | Tuple | Set | Dict)
# --------------------------------------------------------------
# Type   | Characteristics         | Ordered | Collection | Notes
# --------------------------------------------------------------
# List   | Mutable                 | Yes     | ✅          | ⭐ Most used (~90%)
# Tuple  | Immutable               | Yes     | ✅          | Great for fixed data
# Set    | Mutable, Unique values  | No      | ✅          | Removes duplicates
# Dict   | Mutable, Key–Value pair | Yes*    | ✅          | Keys are unique
# --------------------------------------------------------------


# --------------------------








# --------------------------
# 🇮🇩IDN
# 💡 Penjelasan singkat tiap tipe:

# 1. **List (`[]`)**
#
#    * 🔁 *Mutable*: bisa diubah isinya setelah dibuat (bisa tambah, ubah, hapus elemen).
#    * 📜 *Ordered*: elemen disimpan berurutan sesuai urutan penambahan.
#    * 📦 *Collection*: bisa menyimpan berbagai tipe data (campur: string, int, float, dll).
#    * ⭐ Dipakai di 90% kasus Python sehari-hari.
#
#    ```python
#    fruits = ["apple", "banana", "cherry"]
#    fruits.append("mango")  # menambah item
#    ```
#
# 2. **Tuple (`()`)**
#
#    * 🔒 *Immutable*: tidak bisa diubah setelah dibuat.
#    * 📜 *Ordered*: urutannya tetap.
#    * ⚡ Cocok untuk data konstan, misalnya koordinat atau konfigurasi.
#
#    ```python
#    coordinates = (10, 20)
#    ```
#
# 3. **Set (`{}`)**
#
#    * ⚙️ *Mutable*: bisa diubah.
#    * 🚫 *Unordered*: tidak menjamin urutan elemen.
#    * 🔁 *Unique*: otomatis menghapus duplikasi.
#    * Cocok untuk operasi matematika seperti union, intersection.
#
#    ```python
#    numbers = {1, 2, 2, 3}
#    print(numbers)  # {1, 2, 3}
#    ```
#
# 4. **Dictionary (`{key: value}`)**
#
#    * 🧭 *Mapped collection*: menyimpan pasangan kunci-nilai.
#    * 🔁 *Mutable*: bisa ubah nilai berdasarkan key.
#    * 🗂️ *Ordered* sejak Python 3.7 (urutan berdasarkan penambahan item).
#    * Cocok untuk data terstruktur.
#
#    ```python
#    person = {"name": "Alif", "age": 25}
#    person["city"] = "Garut"
#    ```
#
# ---

# 💡 Brief explanation of each type:
# 🇺🇸󠁿ENG
# 1. **List (`[]`)**
#
# * 🔁 *Mutable*: can change its contents after creation (add, change, delete elements).
# * 📜 *Ordered*: elements are stored sequentially in the order they were added.
# * 📦 *Collection*: can store various data types (mixed: string, int, float, etc.).
# * ⭐ Used in 90% of everyday Python cases.
#
# ``` python
# fruits = ["apple", "banana", "cherry"]
# fruits.append("mango") # add an item
# ```
#
# 2. **Tuple (`()`)**
#
# * 🔒 *Immutable*: cannot be changed after creation.
# * 📜 *Order*: the order is fixed.
# * ⚡ Suitable for constant data, such as coordinates or configurations.
#
# ``` python
#coordinates = (10, 20)
# ```
#
# 3. **Set(`{}`)**
#
# * ⚙️ *Mutable*: can be changed.
# * 🚫 *Unordered*: does not guarantee the order of elements.
# * 🔁 *Unique*: automatically removes duplicates.
# * Suitable for mathematical operations such as union, intersection.
#
# ``` python
# numbers = {1, 2, 2, 3}
# print(numbers) # {1, 2, 3}
# ```
#
# 4. **Dictionary(`{key: value}`)**
#
# * 🧭 *Mapped collection*: stores key-value pairs.
# * 🔁 *Mutable*: can change values ​​based on key.
# * 🗂️ *Ordered* since Python 3.7 (ordering based on item addition).
# * Suitable for structured data.
#
# ``` python
# people = {"name": "Alif", "age": 25}
#people["city"] = "Garut"
# ```
#
# ---