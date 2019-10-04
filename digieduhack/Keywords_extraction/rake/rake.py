from rake_nltk import Rake
import gensim
import itertools
import numpy as np
import json

def extract_keywords(text):
    """
    Extract keywords from input text.
    """
    # Uses stopwords for english from NLTK, and all puntuation characters.
    r = Rake()

    # To get keyword phrases ranked highest to lowest.
    r.extract_keywords_from_text(text)
    r.get_ranked_phrases() 
    scores = r.get_ranked_phrases_with_scores()

    # Only keep best keywords
    good_keywords = [x[1] for x in scores if x[0] != 1]
    good_keywords = [x.split() for x in good_keywords]
    good_keywords = list(itertools.chain(*good_keywords))

    return good_keywords

def getContents(filename):

    json_file = open(filename, "r", encoding="utf-8")

    courses = json.load(json_file)
    dictionary = {}

    for i in courses:
        key = courses[i]['name']
        dictionary[key]=courses[i]['content']
        
    json_file.close()

    return dictionary

def word2vec(keywords, model):
    """
    Convert list of keywords to equivalent word2vec representation using pretrained model.
    """
    v = np.zeros(300)
    for w in keywords:
        if w in model.wv:
            v += model.wv[w]
    return v / len(keywords)

def finding_label(model,encoding, labels):

        max_sim = 0
        matching_label1 = ''
        matching_label2 = ''
        consine_similarities = []

        for label in labels:
            consine_similarities.append( np.sum(encoding*word2vec(label, model))/(np.linalg.norm(encoding)*np.linalg.norm(word2vec(label, model))) )
        
        index = np.argmax(consine_similarities)
        matching_label1 = labels[index]
        consine_similarities[index] = 0
        index = np.argmax(consine_similarities)
        matching_label2 = labels[index]

        return matching_label1, matching_label2

if __name__== "__main__":
    
    # CHANGE PATH HERE
    model = gensim.models.KeyedVectors.load_word2vec_format('C:\\Users\\simon\\Desktop\\GoogleNews-vectors-negative300.bin', binary=True)
    
    filename = "../../database/courses.json"

    """
    labels = ['Art', 'Design', 'Architecture', 'Film', 'Television', 'Scenography', 'Media', 
                'Management', 'Finance', 'Accounting', 'Marketing', 'Sales', 'Economics', 'Entrepreneurship',
                'Chemical', 'Bioproducts', 'Biosystems',
                'Communications', 'Electrical', 'Networking', 'Automation', 'Electronics', 'Signal', 'Acoustics',
                'Engineering', 'Mechanical', 'Physics','Mathematics','Industrial', 'Neuroscience', 'Computer']
    """

    labels = ['Art','Computer','Mathematics', 'Economics', "Physics"]

    contents_dictionary = getContents(filename)

    for k in contents_dictionary.keys():
        keywords = extract_keywords(contents_dictionary[k])
        encoding = word2vec(keywords, model)
        label = finding_label(model,encoding, labels)
        print(k, "\n", label, "\n")

    # #text = "Advanced topics in cloud computing with emphasis on scalable distributed computing technologies employed in cloud computing. Key cloud technologies and their algorithmic background. Main topics are distributed file systems, distributed batch processing with the MapReduce and the Apache Spark computing frameworks, and distributed cloud based databases."
    # text = "Content topics covered during the course: - Learning ability and various challenges in learning and studying - Effective learning and academic study skills - Identifying your own strengths and challenges in learning and reflecting on them - Designing your own studies and developing a Personal Study Plan"
    # #text = "The goal of the course is to provide a practical deep-dive into effective communications. Students will learn to apply it in their own lives and careers through a series of exercises. The course emphasizes iterative cycles of research and practice, where personal storytelling skills are developed through feedback and discussion."
    # keywords = extract_keywords(text)
    # encoding = word2vec(keywords, model)

    # # Compute similarities
    # cos_sim = np.zeros(len(interests))
    # for i in range(len(interests)):
    #     cos_sim[i] = np.sum(encoding*word2vec(interests[i], model))/(
    #         np.linalg.norm(encoding)*np.linalg.norm(word2vec(interests[i], model)))

    # # Take the max labels
    # sorted_idx = np.argsort(cos_sim)[-4:]
    # print(interests[sorted_idx[3]], interests[sorted_idx[2]], interests[sorted_idx[1]], interests[sorted_idx[0]])
