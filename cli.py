import argparse

from link import generate_colab_link, generate_colab_link_markdown

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generates a Google Link for your notebook in a Github repo")

    parser.add_argument("--gh",
                        required=True,
                        type=str, help="Link to your notebook in a public Github Repo")

    parser.add_argument("--string",
                        dest="generate",
                        help="the generated link will be a regular string or text which you can copy from your console",
                        action="store_const",
                        const=generate_colab_link)

    parser.add_argument("--md",
                        dest="generate",
                        help="the generated link will be wrapped in a markdown block which you can use in readmes",
                        action="store_const",
                        const=generate_colab_link_markdown)

    args = parser.parse_args()
    print(args.generate(args.gh))
