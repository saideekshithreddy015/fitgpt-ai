import wget
import zipfile
import os

url = "https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_csv.zip"

print("Downloading dataset...")

filename = wget.download(url)

print("\nDownload complete!")

print("Extracting dataset...")

with zipfile.ZipFile(filename, 'r') as zip_ref:
    zip_ref.extractall("datasets")

print("Dataset extracted successfully!")