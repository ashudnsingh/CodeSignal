import textwrap

def feedbackReview(feedback, size):
    return textwrap.TextWrapper(width=size).wrap(feedback)
