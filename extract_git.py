import git

repo = git.Repo('<path_to_repo>')
commits = list(repo.iter_commits('master', max_count=50))  # Adjust as needed

diffs = []
for commit in commits:
    diffs.append(commit.diff().patch)