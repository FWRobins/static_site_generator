from textnode import TextNode

print("Hello world")

def main():
    test1 = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    test2 = TextNode("This is some other anchor text", "link", "https://www.boot.dev")

    print(test1)
    print(test2)

    print(test1 == test2)
    

if __name__ == "__main__":
    main()