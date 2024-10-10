import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = {
    'description': [
        "At Ouran High School, Haruhi encounters the Host Club and joins to repay her debt, forging deep connections.",
        "Park Hyung Seok wakes up with a handsome body, observing changes in how people treat him based on appearance.",
        "Tomboyish Tomo struggles to show her softer side to her childhood friend, whom she has romantic feelings for.",
        "Futaba reconnects with her first love while hiding her true identity in high school to avoid attention.",
        "Anzu is thrown into a romance simulation, resisting her feelings despite the amusing situations she faces.",
        "Misaki juggles two lives—strict school leader by day, secret maid cafe worker by night.",
        "Kyoko immerses herself in the entertainment business after her love interest betrays her, discovering her self-worth.",
        "Kyouko and Miyamura unveil their hidden sides and build a connection based on their true selves.",
        "Kaguya and Miyuki engage in a battle of wits, each trying to force the other to confess their love first.",
        "Takehiro, an intimidating yet kind student, develops a love story with a girl who admires him for his true self.",
        "Kang Mi Rae undergoes surgery to overcome bullying and deals with self-esteem issues at university.",
        "Im Sol time travels to save her idol from death, with lighthearted and heartfelt moments in the series.",
        "Han Se-hye transforms into different people for seven days, causing complications in her romantic life.",
        "Hong Dae Young relives high school life in his 18-year-old body, reconnecting with his family.",
        "Ahn Soo Young believes romantic relationships are destined to fail, exploring love and life with friends."
    ],
    'category': [
        'Slice of Life, Comedy', 
        'Fantasy, Comedy', 
        'Romance, Coming-of-Age', 
        'Romance, Drama', 
        'Romantic Comedy', 
        'Slice of Life, Drama', 
        'Drama, Self-Discovery', 
        'Romance, Drama', 
        'Romantic Comedy', 
        'Romance, Slice of Life', 
        'Drama, Coming-of-Age', 
        'Fantasy, Romance', 
        'Fantasy, Romance', 
        'Drama, Fantasy', 
        'Drama, Romance'
    ]
}




df = pd.DataFrame(data)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['description'])

X_train, X_test, y_train, y_test = train_test_split(X, df['category'], test_size=0.2, random_state=42)

# usign logistic regression
clf = LogisticRegression(max_iter=200)
clf.fit(X_train, y_train)




def classify_description(description):
    description_vector = vectorizer.transform([description])
    prediction = clf.predict(description_vector)
    return prediction[0]

#test your own description to see in which category it fits
new_description = input("Enter your description: ")
category = classify_description(new_description)
print(f"The description is classified as: {category}")
