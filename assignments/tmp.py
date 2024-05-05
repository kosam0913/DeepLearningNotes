from pathlib import Path

target_dir = r"D:\xhu_temp\DeepLearning\assignments\ml_operation_specialization"

for file in Path(target_dir).rglob("*.*"):
    # remove the starting underscore
    file_name = file.name
    if file_name.startswith("_"):
        new_name = file_name[1:]
        new_file = file.parent / new_name
        file.rename(new_file)
        print(f"Renamed {file} to {new_file}")
    else:
        print(f"Skipped {file}")