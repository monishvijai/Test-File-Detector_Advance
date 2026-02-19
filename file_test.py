import os
import subprocess
import shutil


def clone_and_get_tests(repo_url: str):
    folder_name = repo_url.split("/")[-1].replace(".git", "")
    project_path = folder_name

    if os.path.exists(project_path):
        shutil.rmtree(project_path)

    clone_result = subprocess.run(
        ["git", "clone", repo_url],
        capture_output=True,
        text=True
    )

    if clone_result.returncode != 0:
        return {"error": "Failed to clone repository"}

    tests_path = os.path.join(project_path, "tests")
    test_files = []

    if os.path.exists(tests_path):
        for root, dirs, files in os.walk(tests_path):
            for file in files:
                if file.endswith(".py"):
                    test_files.append(file)

        return {
            "message": "Repo cloned successfully",
            "test_files": test_files
        }
    else:
        return {"message": "No 'tests' folder found"}
