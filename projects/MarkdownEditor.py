class MarkdownEditor:
    def __init__(self):
        self.tokens = ""
        self.main()

    def main(self):
        while True:
            x = input("- Choose a formatter:")
            if x == "!done":
                self.done()
            elif x == "!help":
                self.help_function()
            elif x == "plain":
                self.plain()
            elif x == "bold":
                self.bold()
            elif x == "italic":
                self.italic()
            elif x == "inline-code":
                self.inline_code()
            elif x == "link":
                self.link()
            elif x == "header":
                self.header()
            elif x == "new-line":
                self.new_line()
            elif x == "ordered-list":
                self.ordered_list()
            elif x == "unordered-list":
                self.unordered_list()
            else:
                print("Unknown formatter or command. Please try again")

    def help_function(self):
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")

    def plain(self):
        text = input("- Text: ")
        self.tokens += text
        print(self.tokens)

    def bold(self):
        text = input("- Text: ")
        self.tokens += "**" + text + "**"
        print(self.tokens)

    def italic(self):
        text = input("- Text: ")
        self.tokens += "*" + text + "*"
        print(self.tokens)

    def inline_code(self):
        text = input("- Text: ")
        self.tokens += "`" + text + "`"
        print(self.tokens)

    def link(self):
        label = input("- Label: ")
        url = input("- URL: ")
        self.tokens += "[" + label + "](" + url + ")"
        print(self.tokens)

    def header(self):
        level = int(input("Level: "))
        while not (1 <= level <= 6):
            print("The level should be within the range of 1 to 6")
            level = int(input("Level: "))
        text = input("- Text: ")
        self.tokens += "#" * level + " " + text + "\n"
        print(self.tokens)

    def new_line(self):
        self.tokens += "\n"
        print(self.tokens)

    def ordered_list(self):
        rows = int(input("- Number of rows: "))
        while rows < 1:
            print("The number of rows should be greater than zero")
            rows = int(input("- Number of rows: "))
        for i in range(rows):
            text = input(f"Row #{i + 1}")
            self.tokens += str(i + 1) + ". " + text + "\n"
        print(self.tokens)

    def unordered_list(self):
        rows = int(input("- Number of rows: "))
        while rows < 1:
            print("The number of rows should be greater than zero")
            rows = int(input("- Number of rows: "))
        for i in range(rows):
            text = input(f"Row #{i + 1}")
            self.tokens += "* " + text + "\n"
        print(self.tokens)

    def done(self):
        my_file = open("output.md", "w")
        my_file.write(self.tokens)
        my_file.close()
        exit()


if __name__ == '__main__':
    program = MarkdownEditor()
