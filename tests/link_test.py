import unittest
import sys


# add project root to syspath
sys.path.append("../")

try:
    from link import generate_colab_link, generate_colab_link_markdown
except ModuleNotFoundError as e:
    print(e)


class TestLinkGeneration(unittest.TestCase):
    def test_str(self):
        gh = "https://github.com/ShawonAshraf/jax_examples/blob/main/playground/palmers_penguins.ipynb"
        target = "https://colab.research.google.com/github/ShawonAshraf/jax_examples/blob/main/playground/palmers_penguins.ipynb"

        self.assertEqual(generate_colab_link(gh), target)

    def test_md(self):
        gh = "https://github.com/ShawonAshraf/jax_examples/blob/main/playground/palmers_penguins.ipynb"
        target = "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ShawonAshraf/jax_examples/blob/main/playground/palmers_penguins.ipynb)"

        self.assertEqual(generate_colab_link_markdown(gh), target)
