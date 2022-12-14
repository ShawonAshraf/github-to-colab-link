"""
takes in the url to a jupyter notebook hosted on github (public repo) and 
returns a url as string to run the notebook in Google colab.
"""


def generate_colab_link(github_url_for_notebook: str) -> str:
    colab_root = "https://colab.research.google.com/"
    gh_root = "https://github.com"
    gh_prefix = "github"

    # the url format for colab notebooks loaded from github looks like this:
    # colab_root/github/USERNAME/REPO/blob/branch/additional_path_if_exists/notebook.ipynb

    # the tail will retain the / at the beginning
    gh_notebook_url_tail = github_url_for_notebook.split(gh_root)[1]

    # construct colab url string
    colab_link = colab_root + gh_prefix + gh_notebook_url_tail

    return colab_link


"""
returns a string in markdown format to be used in github readmes or other markdown format
"""


def generate_colab_link_markdown(github_url_for_notebook: str) -> str:
    colab_link = generate_colab_link(github_url_for_notebook)
    makrdown_str = "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]" + \
        f"({colab_link})"

    return makrdown_str


if __name__ == "__main__":
    gh = "https://github.com/ShawonAshraf/nlu-jointbert-dl2021/blob/main/notebooks/nlu_jointbert_dl21.ipynb"
    target = "https://colab.research.google.com/github/ShawonAshraf/nlu-jointbert-dl2021/blob/main/notebooks/nlu_jointbert_dl21.ipynb"
    target_md = "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ShawonAshraf/nlu-jointbert-dl2021/blob/main/notebooks/nlu_jointbert_dl21.ipynb)"

    assert generate_colab_link(gh) == target
    assert generate_colab_link_markdown(gh) == target_md
