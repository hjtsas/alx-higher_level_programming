#!/usr/bin/python3
# 5-text_indentation.py
"""Defines a text-indentation function."""

def text_indentation(text):
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Split the text into sentences
    sentences = text.split(".")
    
    # Add two new lines after each sentence
    new_text = "\n\n".join([sentence.strip() + "." for sentence in sentences])
    
    # Split the text into questions
    questions = new_text.split("?")
    
    # Add two new lines after each question
    new_text = "\n\n".join([question.strip() + "?" for question in questions])
    
    # Split the text into exclamations
    exclamations = new_text.split("!")
    
    # Add two new lines after each exclamation
    new_text = "\n\n".join([exclamation.strip() + "!" for exclamation in exclamations])
    
    # Print the formatted text
    print(new_text)
