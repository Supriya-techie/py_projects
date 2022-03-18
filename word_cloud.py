# Here are all the installs and imports you will need for your word cloud script and uploader widget

!pip install wordcloud
!pip install fileupload
!pip install ipywidgets
!jupyter nbextension install --py --user fileupload
!jupyter nbextension enable --py fileupload

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

# This is the uploader widget
def _upload():
    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()
    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)
_upload()

Hint: Try storing the results of your iteration in a dictionary before passing them into wordcloud via the generate_from_frequencies function.
def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    #ignoring case
    file_contents = file_contents.lower()
    file_contents_list = file_contents.split()
    new_file_contents_list = []
    new_contents_file = ""
    # LEARNER CODE START HERE
    #removing punctuions
    for text in file_contents:
        if text in punctuations:
            file_contents = file_contents.replace(text,""        
    #removing words with numbers
    for text in file_contents_list:
        if text.isalpha():
            new_file_contents_list.append(text)        
    #removing uninteresting words         
    for file_list in new_file_contents_list:
         if file_list not in uninteresting_words:
                new_contents_file = new_contents_file+" "+file_list           
    #count frequencies
    word_list = new_contents_file.split()
    word_frequencies = {}
    for word in word_list:
        word_frequencies[word]=word_list.count(word)    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_frequencies)
    return cloud.to_array()
     # Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()                                             
