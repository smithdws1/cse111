import random

def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        random_number = round(random.uniform(0, 100), 1)
        numbers_list.append(random_number)

def append_random_words(words_list, quantity=1):
    word_bank = ["dog", "cat", "apple", "keyboard", "phone", "baby", "laptop", "crazy", "torch", "sideways", "maybe"]
    for _ in range(quantity):
        random_word = random.choice(word_bank)
        words_list.append(random_word)

def main():
    numbers = [37.5, 234.4, 12.1, 49.9]
    print("Initial numbers list:", numbers)
    
    append_random_numbers(numbers)
    print("Numbers list after appending one number:", numbers)
    
    append_random_numbers(numbers, 3)
    print("Numbers list after appending three more numbers:", numbers)

    words = []
    print("\nInitial words list:", words)

    append_random_words(words)
    print("Words list after appending one word:", words)

    append_random_words(words, 3)
    print("Words list after appending three more words:", words)

if __name__ == "__main__":
    main()