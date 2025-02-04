from textnode import TextNode, TextType


def main():
    dummy_node = TextNode("some text", TextType.BOLD, "https://www.boot.dev")
    print(dummy_node)


if __name__ == "__main__":
    main()
