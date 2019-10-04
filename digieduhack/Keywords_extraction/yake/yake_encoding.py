import yake
import gensim
import numpy as np
import itertools
import nltk
from nltk.corpus import stopwords


def extract_keywords(text):
    """
    Extract keywords from a text using yake model.
    """
    # extract keywords
    kw_extractor = yake.KeywordExtractor()
    keywords = kw_extractor.extract_keywords(text)

    # Sort them
    sorted_kw = sorted(keywords, key=lambda tup: tup[1])
    sorted_kw.reverse()
    sorted_kw = [x[0].replace(" ", "_") for x in sorted_kw]

    # # Make a list of strings
	# sorted_kw = [x.split() for x in sorted_kw]
	# sorted_kw = list(itertools.chain(*sorted_kw))

	# # Removing stopwords
	# stop_words = set(stopwords.words('english'))
	# filtered_kw = [w for w in sorted_kw if not w in stop_words] 

    return sorted_kw


def word2vec(keywords, model):
    """
    Convert list of keywords to equivalent word2vec representation using pretrained model.
    """
    v = np.zeros(300)
    for w in keywords:
        if w in model.wv:
            v += model.wv[w]
    return v / len(keywords)


if __name__ == "__main__":
        # Load Google's pre-trained Word2Vec model.
    model = gensim.models.KeyedVectors.load_word2vec_format(
        './word2vec/GoogleNews-vectors-negative300.bin', binary=True)

    # interests = ['Advertising', 'Media', 'Agriculture', 'Audio', 'Video', 'multimedia_production', 'Banking', 'Finance', 'Invest',
    #              'Construction', 'Urban_planning', 'Landscape_design', 'Consulting', 'Design', 'Graphic_arts', 'Education', 'Teaching', 'Training',
    #              'Engineering', 'Environment', 'Natural_resources', 'Insurance', 'Visual', 'Performing_arts',
    #                             'Government', 'Public_sector', 'Public_policy', 'Health_services', 'Healthcare', 'Medical', 'Hospitality', 'Tourism', 'Food', 'Human_resources'
    #                             'Labor_relations', 'InfoTech', 'Computer_science', 'Electronics', 'Artificial_Intelligence', 'Criminal_justice', 'Security', 'Management', 'Supply_Chain',
    #                             'Manufacturing', 'Marketing', 'Sales', 'Research', 'Quality_Assurance', 'Biotech', 'Social_Services', 'Social_Community', 'Writing',
    #                             'Publishing', 'Art', 'Design', 'Architecture', 'Film', 'Entrepreneurship', 'Mathematics']
    interests = ['Art','Computer','Mathematics', 'Economics', "Physics"]

    text = "Advanced topics in cloud computing with emphasis on scalable distributed computing technologies employed in cloud computing. Key cloud technologies and their algorithmic background. Main topics are distributed file systems, distributed batch processing with the MapReduce and the Apache Spark computing frameworks, and distributed cloud based databases."
    #text = "Content topics covered during the course: - Learning ability and various challenges in learning and studying - Effective learning and academic study skills - Identifying your own strengths and challenges in learning and reflecting on them - Designing your own studies and developing a Personal Study Plan"
    #text = "The goal of the course is to provide a practical deep-dive into effective communications. Students will learn to apply it in their own lives and careers through a series of exercises. The course emphasizes iterative cycles of research and practice, where personal storytelling skills are developed through feedback and discussion."
    keywords = extract_keywords(text)
    encoding = word2vec(keywords, model)

    # Compute similarities
    cos_sim = np.zeros(len(interests))
    for i in range(len(interests)):
        cos_sim[i] = np.sum(encoding*word2vec(interests[i], model))/(
            np.linalg.norm(encoding)*np.linalg.norm(word2vec(interests[i], model)))

    # Take the max labels
    sorted_idx = np.argsort(cos_sim)[-4:]
    print(interests[sorted_idx[3]], interests[sorted_idx[2]], interests[sorted_idx[1]], interests[sorted_idx[0]])
