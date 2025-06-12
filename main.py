from process import DataHandler, Analyzer
from visual import Visualizer
from tui import Menu

def show_title():
    title = "Disneyland Review Analyser"
    print("-" * len(title))
    print(title)
    print("-" * len(title))

def main():
    show_title()
    data_handler = DataHandler()
    analyzer = Analyzer(data_handler)
    visualizer = Visualizer()
    print(f"Dataset loaded successfully with {len(data_handler.data)} rows.")
    menu = Menu(data_handler, analyzer, visualizer)
    menu.run()

if __name__ == "__main__":
    main()
