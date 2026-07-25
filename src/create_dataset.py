import os
import pandas as pd
from features.feature_extractor import extract_features

# مسیر پوشه‌ای که فایل‌های صوتی همه افراد در آن قرار دارند
base_path = "data/voices"

# لیستی برای ذخیره اطلاعات همه فایل‌های صوتی
dataset = []

# پیمایش پوشه هر شخص (مانند Heidari، Taljangani و ...)
for person in os.listdir(base_path):

    # ساخت مسیر کامل پوشه شخص
    person_folder = os.path.join(base_path, person)

    # اگر مورد پیدا شده پوشه نبود، از آن عبور کن
    if not os.path.isdir(person_folder):
        continue

    # پیمایش همه فایل‌های موجود در پوشه شخص
    for file in os.listdir(person_folder):

        # فقط فایل‌های WAV پردازش شوند
        if file.endswith(".wav"):

            # ساخت مسیر کامل فایل صوتی
            file_path = os.path.join(person_folder, file)

            # استخراج ویژگی‌های فایل صوتی
            features = extract_features(file_path)

            # ایجاد یک سطر جدید برای ذخیره اطلاعات فایل
            row = {
                "Person": person,
                "File": file
            }

            # اضافه کردن ویژگی‌ها به سطر
            for i, value in enumerate(features):
                row[f"Feature_{i+1}"] = value

            # افزودن سطر به دیتاست
            dataset.append(row)

# تبدیل لیست داده‌ها به DataFrame
df = pd.DataFrame(dataset)

# ذخیره دیتاست در فایل CSV
df.to_csv("data/features.csv", index=False)

# نمایش چند سطر اول دیتاست
print("\nFirst 5 Rows:")
print(df.head())

# نمایش ابعاد دیتاست
print("\nDataset Shape:")
print(df.shape)

# نمایش نام ستون‌ها
print("\nColumns:")
print(df.columns)

# نمایش تعداد فایل‌های هر شخص
print("\nSamples Per Person:")
print(df["Person"].value_counts())

print("\nDataset created successfully!")
print("Saved as: data/features.csv")
