class StoryNode:
    """Represents a node in the decision tree."""
    def __init__(self, event_number, description, left=None, right=None):
        self.event_number = event_number
        self.description = description
        self.left = left
        self.right = right

class GameDecisionTree:
    """Binary decision tree for the RPG."""
    def __init__(self):
        self.nodes = {}  # Dictionary to store nodes
        self.root = None  # Root node of the tree

    def insert(self, event_number, description, left_event, right_event):
        """Insert a new story node into the tree."""
        if event_number not in self.nodes:
            self.nodes[event_number] = StoryNode(event_number, description)

        node = self.nodes[event_number]
        node.description = description

        if left_event != -1:
            if left_event not in self.nodes:
                self.nodes[left_event] = StoryNode(left_event, "")
            node.left = self.nodes[left_event]

        if right_event != -1:
            if right_event not in self.nodes:
                self.nodes[right_event] = StoryNode(right_event, "")
            node.right = self.nodes[right_event]

        if self.root is None:
            self.root = node  # Set the first inserted node as root

    def play_game(self):
        """Interactive function that plays the RPG."""
        current_node = self.root

        while current_node:
            print("\n" + current_node.description)

            if current_node.left is None and current_node.right is None:
                print("The game has ended. Thanks for playing!") #Empty tree ends game
                break

            choice = input("Enter your choice (1 or 2): ").strip()
            if choice == "1" and current_node.left:
                current_node = current_node.left
            elif choice == "2" and current_node.right:
                current_node = current_node.right
            else:
                print("Invalid choice. Please enter 1 or 2.")

def load_story(filename, game_tree):
    """Load story from a file and construct the decision tree."""
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) != 4:
                    print(f"Skipping invalid line: {line}")
                    continue

                event_number = int(parts[0])
                description = parts[1]
                left_event = int(parts[2])
                right_event = int(parts[3])

                game_tree.insert(event_number, description, left_event, right_event)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        exit(1)
    except ValueError:
        print("Error: Invalid data format in the story file.")
        exit(1)
        
# Main program
if __name__ == "__main__":
    game_tree = GameDecisionTree()
    load_story("story.txt", game_tree)
    game_tree.play_game()