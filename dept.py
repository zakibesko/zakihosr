"""
ENGLISH:
This example shows the difference between text and binary files
ARABIC:
هذا المثال يوضح الفرق بين الملفات النصية والثنائية
"""

import os

# ============================================================
# PART 1: Creating a TEXT file
# الجزء 1: إنشاء ملف نصي
# ============================================================

print("=" * 50)
print("PART 1: TEXT FILE / ملف نصي")
print("=" * 50)

# English: Create a text file with readable content
# العربية: إنشاء ملف نصي بمحتوى مقروء

text_content = """Hello World!
This is a text file.
You can read this easily.
Numbers: 12345
Arabic: مرحبا بالعالم"""

with open("example_text.txt", "w", encoding="utf-8") as file:
    file.write(text_content)

print("✓ Created text file: example_text.txt")
print(f"Content written: {text_content[:50]}...")  # First 50 chars


# ============================================================
# PART 2: Creating a BINARY file
# الجزء 2: إنشاء ملف ثنائي
# ============================================================

print("\n" + "=" * 50)
print("PART 2: BINARY FILE / ملف ثنائي")
print("=" * 50)

# English: Create binary data (raw bytes)
# العربية: إنشاء بيانات ثنائية (بايتات خام)

# English: These are raw bytes - not human readable!
# العربية: هذه بايتات خام - غير مقروءة للإنسان!

binary_content = b'\x48\x65\x6c\x6c\x6f\x00\x00\x00\x89PNG\r\n\x1a\n\xff\xd8\xff\xe0'

with open("example_binary.bin", "wb") as file:  # Note: 'wb' mode for binary write
    file.write(binary_content)

print("✓ Created binary file: example_binary.bin")
print(f"Binary data (first 20 bytes): {binary_content[:20]}")


# ============================================================
# PART 3: Trying to read binary file as text (FAILS)
# الجزء 3: محاولة قراءة ملف ثنائي كنص (تفشل)
# ============================================================

print("\n" + "=" * 50)
print("PART 3: Reading binary file as text (WRONG WAY)")
print("الجزء 3: قراءة ملف ثنائي كنص (طريقة خاطئة)")
print("=" * 50)

# English: If we try to read a binary file as text, we get garbage
# العربية: إذا حاولنا قراءة ملف ثنائي كنص، نحصل على رموز غير مفهومة

try:
    with open("example_binary.bin", "r") as file:  # 'r' mode for text
        garbage = file.read()
        print(f"Reading as text gives: {garbage}")
except UnicodeDecodeError as e:
    print(f"ERROR! Cannot read binary file as text!")
    print(f"Error message: {e}")
    print("This is why we need 'rb' mode for binary files!")


# ============================================================
# PART 4: Reading binary file correctly
# الجزء 4: قراءة ملف ثنائي بشكل صحيح
# ============================================================

print("\n" + "=" * 50)
print("PART 4: Reading binary file correctly (RIGHT WAY)")
print("الجزء 4: قراءة ملف ثنائي بشكل صحيح (طريقة صحيحة)")
print("=" * 50)

with open("example_binary.bin", "rb") as file:  # 'rb' = read binary
    binary_data = file.read()
    print(f"Read binary data: {binary_data[:20]}...")
    print(f"Length: {len(binary_data)} bytes")
    print(f"Each byte is a number between 0-255")


# ============================================================
# PART 5: Checking file types
# الجزء 5: التحقق من أنواع الملفات
# ============================================================

print("\n" + "=" * 50)
print("PART 5: File Type Detection")
print("الجزء 5: اكتشاف نوع الملف")
print("=" * 50)

def is_likely_text_file(filename):
    """
    ENGLISH:
    Try to guess if a file is text by attempting to read it as text
    ARABIC:
    محاولة تخمين إذا كان الملف نصيًا بمحاولة قراءته كنص
    """
    try:
        with open(filename, 'r') as f:
            f.read(1024)  # Try reading first 1024 bytes as text
        return True  # If no error, likely text
    except UnicodeDecodeError:
        return False  # If error, definitely binary
    except Exception:
        return False

# Test both files
print(f"example_text.txt is text? {is_likely_text_file('example_text.txt')}")
print(f"example_binary.bin is text? {is_likely_text_file('example_binary.bin')}")


# ============================================================
# PART 6: Why binary files exist (efficiency)
# الجزء 6: لماذا توجد الملفات الثنائية (الكفاءة)
# ============================================================

print("\n" + "=" * 50)
print("PART 6: Why Binary Files? (Size Comparison)")
print("الجزء 6: لماذا الملفات الثنائية؟ (مقارنة الحجم)")
print("=" * 50)

# English: Create the same data as text and binary
# العربية: إنشاء نفس البيانات كنص و كثنائي

# Data: numbers from 0 to 999
# البيانات: أرقام من 0 إلى 999

# As TEXT (human readable)
# كنص (مقروء للإنسان)
with open("numbers_text.txt", "w") as f:
    for i in range(1000):
        f.write(f"{i}\n")

# As BINARY (raw bytes - 4 bytes per number)
# كثنائي (بايتات خام - 4 بايتات لكل رقم)
import struct
with open("numbers_binary.bin", "wb") as f:
    for i in range(1000):
        f.write(struct.pack('i', i))  # 'i' = signed integer (4 bytes)

# Compare sizes
text_size = os.path.getsize("numbers_text.txt ")
binary_size = os.path.getsize("numbers_binary.bin")

print(f"Text file size: {text_size:,} bytes")
print(f"Binary file size: {binary_size:,} bytes")
print(f"Binary is {text_size/binary_size:.1f}x smaller!")
print("Binary files are more efficient for numbers and complex data")