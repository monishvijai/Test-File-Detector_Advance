
from fastapi import APIRouter
from file_test import clone_and_get_tests

router = APIRouter(prefix="/repo", tags=["Repo"])

@router.post("/clone")
def clone_repo(repo_url: str):
    result = clone_and_get_tests(repo_url)
    return result
