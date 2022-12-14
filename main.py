import sys

from link import generate_colab_link, generate_colab_link_markdown

if __name__ == "__main__":
    allowed_options = {
        "--str": generate_colab_link,
        "--md": generate_colab_link_markdown
    }

    option = sys.argv[1]
    gh_link = sys.argv[2]

    colab_link = allowed_options[option](gh_link)
    print(colab_link)
