from rake_nltk import Rake
import gensim
import itertools
import numpy as np


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
    

def word2vec(keywords, model):
    """
    Convert list of keywords to equivalent word2vec representation using pretrained model.
    """
    v = np.zeros(300)
    for w in keywords:
        if w in model.wv:
            v += model.wv[w]
    return v / len(keywords)



if __name__== "__main__":

    # Load Google's pre-trained Word2Vec model.
    model = gensim.models.KeyedVectors.load_word2vec_format('./model/GoogleNews-vectors-negative300.bin', binary=True)

    labels = ['Art', 'Design', 'Architecture', 'Film', 'Television', 'Scenography', 'Media', 
                'Management', 'Finance', 'Accounting', 'Marketing', 'Sales', 'Economics', 'Entrepreneurship',
                'Chemical', 'Bioproducts', 'Biosystems',
                'Communications', 'Electrical', 'Networking', 'Automation', 'Electronics', 'Signal', 'Acoustics',
                'Engineering', 'Mechanical', 'Physics','Mathematics','Industrial', 'Neuroscience', 'Computer']

    #text = "Advanced topics in cloud computing with emphasis on scalable distributed computing technologies employed in cloud computing. Key cloud technologies and their algorithmic background. Main topics are distributed file systems, distributed batch processing with the MapReduce and the Apache Spark computing frameworks, and distributed cloud based databases."
    text = "Content topics covered during the course: - Learning ability and various challenges in learning and studying - Effective learning and academic study skills - Identifying your own strengths and challenges in learning and reflecting on them - Designing your own studies and developing a Personal Study Plan"
    #text = "The goal of the course is to provide a practical deep-dive into effective communications. Students will learn to apply it in their own lives and careers through a series of exercises. The course emphasizes iterative cycles of research and practice, where personal storytelling skills are developed through feedback and discussion."
    keywords = extract_keywords(text)
    encoding = word2vec(keywords, model)

    max_sim = 0
    matching_label = ''
    for label in labels:
        cosine_similarity = np.sum(encoding*word2vec(label, model))/(np.linalg.norm(encoding)*np.linalg.norm(word2vec(label, model)))
        if cosine_similarity > max_sim:
            matching_label = label
            max_sim = cosine_similarity

    print(matching_label)