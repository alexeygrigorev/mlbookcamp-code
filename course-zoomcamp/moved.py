import os

base_url = "https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master"

root_dir = os.getcwd()

current_script = os.path.basename(__file__)


def generate_new_link(file_path):
    relative_path = os.path.relpath(file_path, root_dir)
    new_link = f"{base_url}/{relative_path.replace(os.sep, '/')}"
    return new_link


def update_md_file(file_path):
    new_link = generate_new_link(file_path)
    new_content = f"[Moved to new location]({new_link})"

    with open(file_path, "w") as f:
        f.write(new_content)

    print(f"Updated: {file_path} -> {new_link}")


def delete_non_md_file(file_path):
    try:
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    except OSError as e:
        print(f"Error deleting {file_path}: {e}")


def update_and_clean_folder(folder_path):

    for subdir, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(subdir, file)

            if file == current_script:
                continue

            if file.endswith(".md"):
                update_md_file(file_path)
            else:
                delete_non_md_file(file_path)


update_and_clean_folder(root_dir)