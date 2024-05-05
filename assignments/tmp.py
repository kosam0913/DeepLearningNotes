from pathlib import Path

target_dir = r"D:\xhu_temp\DeepLearning\assignments\ml_operation_specialization"

for file in Path(target_dir).rglob("*.*"):
    # rename with lower cases
    file_name = file.name
    new_name = f"_{file_name.lower()}"
    file.rename(new_name)