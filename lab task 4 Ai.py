#!/usr/bin/env python
# coding: utf-8

# In[4]:


def luhn_check(card_number):
    card_number = ''.join(filter(str.isdigit, card_number))  # Remove non-digit characters
    digits = [int(digit) for digit in card_number]
    total_sum = 0
    # Iterate over the digits from right to left (reverse order)
    for i in range(len(digits) - 1, -1, -1):
        digit = digits[i]
        if (len(digits) - i) % 2 == 0:  # Even position when counting from the right (1-based index)
            doubled = digit * 2
            if doubled > 9:
                total_sum += (doubled - 9)  # Same as subtracting 9
            else:
                total_sum += doubled
        else:
            total_sum += digit
    return total_sum % 10 == 0

card_number = "4539 1488 0343 6467"
is_valid = luhn_check(card_number)
print(f"The card number {card_number} is {'valid' if is_valid else 'invalid'}.")


# In[5]:


def remove_special_characters(text):
    punctuation_marks = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
    return ''.join(char for char in text if char not in punctuation_marks)
user_input = input("Please provide a string: ")
print("Original input:", user_input)
modified_string = remove_special_characters(user_input)
print("Modified string (no special characters):", modified_string)


# In[6]:


def custom_sort(input_string):
    char_list = list(input_string)
    for i in range(len(char_list)):
        min_idx = i
        for j in range(i + 1, len(char_list)):
            if char_list[j] < char_list[min_idx]:
                min_idx = j
        char_list[i], char_list[min_idx] = char_list[min_idx], char_list[i]
    return ''.join(char_list)
input_string = input("Enter a word: ")
sorted_string = custom_sort(input_string)
print("Sorted word:", sorted_string)


# In[ ]:




