import streamlit as st


def calculate_score(answers):
    scores = {'Programmer': 0, 'Designer': 0, 'Data Scientist': 0}

    
    if answers['Q1'] == 'Saya suka coding':
        scores['Programmer'] += 1
    elif answers['Q1'] == 'Saya suka mendesain sesuatu':
        scores['Designer'] += 1
    else:
        scores['Data Scientist'] += 1

    if answers['Q2'] == 'Saya suka bekerja dengan data':
        scores['Data Scientist'] += 1
    elif answers['Q2'] == 'Saya suka bekerja dengan kode':
        scores['Programmer'] += 1
    else:
        scores['Designer'] += 1

    if answers['Q3'] == 'Saya suka bekerja di industri teknologi':
        scores['Programmer'] += 1
    elif answers['Q3'] == 'Saya suka bekerja di industri kreatif':
        scores['Designer'] += 1
    else:
        scores['Data Scientist'] += 1

    if answers['Q4'] == 'Saya lebih suka bekerja dengan logika':
        scores['Programmer'] += 1
    elif answers['Q4'] == 'Saya suka menggambar dan mendesain':
        scores['Designer'] += 1
    else:
        scores['Data Scientist'] += 1

    if answers['Q5'] == 'Saya suka analisis data':
        scores['Data Scientist'] += 1
    elif answers['Q5'] == 'Saya suka menulis kode komputer':
        scores['Programmer'] += 1
    else:
        scores['Designer'] += 1

    if answers['Q6'] == 'Saya suka menggunakan alat desain grafis':
        scores['Designer'] += 1
    elif answers['Q6'] == 'Saya suka memecahkan masalah dengan kode':
        scores['Programmer'] += 1
    else:
        scores['Data Scientist'] += 1

    if answers['Q7'] == 'Saya tertarik dengan kecerdasan buatan':
        scores['Data Scientist'] += 1
    elif answers['Q7'] == 'Saya tertarik dengan pengembangan aplikasi':
        scores['Programmer'] += 1
    else:
        scores['Designer'] += 1

    if answers['Q8'] == 'Saya suka bekerja dengan algoritma':
        scores['Programmer'] += 1
    elif answers['Q8'] == 'Saya suka bekerja dengan seni digital':
        scores['Designer'] += 1
    else:
        scores['Data Scientist'] += 1

    if answers['Q9'] == 'Saya suka menganalisis tren dan pola data':
        scores['Data Scientist'] += 1
    elif answers['Q9'] == 'Saya suka menulis kode komputer':
        scores['Programmer'] += 1
    else:
        scores['Designer'] += 1

    if answers['Q10'] == 'Saya tertarik untuk menciptakan antarmuka pengguna yang menarik':
        scores['Designer'] += 1
    elif answers['Q10'] == 'Saya ingin membuat aplikasi yang berjalan di berbagai platform':
        scores['Programmer'] += 1
    else:
        scores['Data Scientist'] += 1

    if answers['Q11'] == 'Saya suka eksperimen dengan data besar':
        scores['Data Scientist'] += 1
    elif answers['Q11'] == 'Saya suka menulis kode untuk aplikasi atau website':
        scores['Programmer'] += 1
    else:
        scores['Designer'] += 1

    if answers['Q12'] == 'Saya suka membuat website yang responsif':
        scores['Programmer'] += 1
    elif answers['Q12'] == 'Saya suka membuat desain grafis dan ilustrasi':
        scores['Designer'] += 1
    else:
        scores['Data Scientist'] += 1

    if answers['Q13'] == 'Saya ingin bekerja di industri teknologi':
        scores['Programmer'] += 1
    elif answers['Q13'] == 'Saya ingin bekerja di industri kreatif':
        scores['Designer'] += 1
    else:
        scores['Data Scientist'] += 1

    if answers['Q14'] == 'Saya tertarik dengan pengembangan perangkat lunak':
        scores['Programmer'] += 1
    elif answers['Q14'] == 'Saya ingin menciptakan seni digital yang inovatif':
        scores['Designer'] += 1
    else:
        scores['Data Scientist'] += 1

    if answers['Q15'] == 'Saya ingin bekerja dengan big data':
        scores['Data Scientist'] += 1
    elif answers['Q15'] == 'Saya tertarik membuat aplikasi dan sistem komputer':
        scores['Programmer'] += 1
    else:
        scores['Designer'] += 1

    if answers['Q16'] == 'Saya suka berfokus pada pengembangan aplikasi mobile':
        scores['Programmer'] += 1
    elif answers['Q16'] == 'Saya lebih suka desain grafis untuk branding dan iklan':
        scores['Designer'] += 1
    else:
        scores['Data Scientist'] += 1

    if answers['Q17'] == 'Saya lebih suka bekerja dengan database dan sistem informasi':
        scores['Data Scientist'] += 1
    elif answers['Q17'] == 'Saya ingin menjadi ahli dalam pengembangan perangkat lunak':
        scores['Programmer'] += 1
    else:
        scores['Designer'] += 1

    if answers['Q18'] == 'Saya ingin menjadi bagian dari tim pengembangan aplikasi web':
        scores['Programmer'] += 1
    elif answers['Q18'] == 'Saya ingin fokus pada penciptaan desain visual yang estetis':
        scores['Designer'] += 1
    else:
        scores['Data Scientist'] += 1

    if answers['Q19'] == 'Saya tertarik untuk bekerja dengan algoritma pembelajaran mesin':
        scores['Data Scientist'] += 1
    elif answers['Q19'] == 'Saya ingin mengembangkan aplikasi untuk meningkatkan produktivitas':
        scores['Programmer'] += 1
    else:
        scores['Designer'] += 1

    if answers['Q20'] == 'Saya suka bekerja dengan statistik dan analisis data':
        scores['Data Scientist'] += 1
    elif answers['Q20'] == 'Saya tertarik mengembangkan aplikasi desktop':
        scores['Programmer'] += 1
    else:
        scores['Designer'] += 1

    return scores


st.title('Potention Quiz - :red[Profesi yang Cocok untuk Anda]')


questions = {
    'Q1': 'Apa yang paling Anda sukai?',
    'Q2': 'Apa yang lebih menarik bagi Anda?',
    'Q3': 'Di industri apa Anda ingin bekerja?',
    'Q4': 'Apa yang lebih Anda sukai?',
    'Q5': 'Apa yang lebih menarik bagi Anda?',
    'Q6': 'Apa yang lebih Anda suka?',
    'Q7': 'Apa yang lebih menarik bagi Anda?',
    'Q8': 'Apa yang lebih menarik bagi Anda?',
    'Q9': 'Apa yang lebih menarik bagi Anda?',
    'Q10': 'Apa yang lebih Anda sukai?',
    'Q11': 'Apa yang lebih Anda sukai?',
    'Q12': 'Apa yang lebih Anda sukai?',
    'Q13': 'Di bidang apa Anda ingin bekerja?',
    'Q14': 'Apa yang lebih Anda tertarik?',
    'Q15': 'Apa yang lebih Anda tertarik?',
    'Q16': 'Apa yang lebih Anda suka?',
    'Q17': 'Apa yang lebih Anda suka?',
    'Q18': 'Apa yang lebih Anda suka?',
    'Q19': 'Apa yang lebih Anda sukai?',
    'Q20': 'Apa yang lebih Anda tertarik?',
}

options = {
    'Q1': ['Saya suka coding', 'Saya suka mendesain sesuatu', 'Saya suka menganalisis data'],
    'Q2': ['Saya suka bekerja dengan data', 'Saya suka bekerja dengan kode', 'Saya suka mendesain grafis'],
    'Q3': ['Saya suka bekerja di industri teknologi', 'Saya suka bekerja di industri kreatif', 'Saya suka bekerja di bidang riset dan data'],
    'Q4': ['Saya lebih suka bekerja dengan logika', 'Saya suka menggambar dan mendesain', 'Saya suka menganalisis data'],
    'Q5': ['Saya suka analisis data', 'Saya suka menulis kode komputer', 'Saya suka mendesain grafis'],
    'Q6': ['Saya suka menggunakan alat desain grafis', 'Saya suka memecahkan masalah dengan kode', 'Saya suka bekerja dengan data'],
    'Q7': ['Saya tertarik dengan kecerdasan buatan', 'Saya tertarik dengan pengembangan aplikasi', 'Saya tertarik dengan desain'],
    'Q8': ['Saya suka bekerja dengan algoritma', 'Saya suka bekerja dengan seni digital', 'Saya suka bekerja dengan data'],
    'Q9': ['Saya suka menganalisis tren dan pola data', 'Saya suka menulis kode komputer', 'Saya suka mendesain grafis'],
    'Q10': ['Saya tertarik untuk menciptakan antarmuka pengguna yang menarik', 'Saya ingin membuat aplikasi yang berjalan di berbagai platform', 'Saya ingin bekerja dengan data'],
    'Q11': ['Saya suka eksperimen dengan data besar', 'Saya suka menulis kode untuk aplikasi atau website', 'Saya suka mendesain'],
    'Q12': ['Saya suka membuat website yang responsif', 'Saya suka membuat desain grafis dan ilustrasi', 'Saya suka menganalisis data'],
    'Q13': ['Saya ingin bekerja di industri teknologi', 'Saya ingin bekerja di industri kreatif', 'Saya ingin bekerja di bidang riset dan data'],
    'Q14': ['Saya tertarik dengan pengembangan perangkat lunak', 'Saya ingin menciptakan seni digital yang inovatif', 'Saya tertarik dengan analisis data'],
    'Q15': ['Saya ingin bekerja dengan big data', 'Saya tertarik membuat aplikasi dan sistem komputer', 'Saya suka mendesain grafis'],
    'Q16': ['Saya suka berfokus pada pengembangan aplikasi mobile', 'Saya lebih suka desain grafis untuk branding dan iklan', 'Saya suka bekerja dengan data besar'],
    'Q17': ['Saya lebih suka bekerja dengan database dan sistem informasi', 'Saya ingin menjadi ahli dalam pengembangan perangkat lunak', 'Saya suka mendesain'],
    'Q18': ['Saya ingin menjadi bagian dari tim pengembangan aplikasi web', 'Saya ingin fokus pada penciptaan desain visual yang estetis', 'Saya suka bekerja dengan data besar'],
    'Q19': ['Saya tertarik untuk bekerja dengan algoritma pembelajaran mesin', 'Saya ingin mengembangkan aplikasi untuk meningkatkan produktivitas', 'Saya suka mendesain grafis'],
    'Q20': ['Saya suka bekerja dengan statistik dan analisis data', 'Saya tertarik mengembangkan aplikasi desktop', 'Saya lebih suka desain grafis'],
}


answers = {}
for key, question in questions.items():
    answers[key] = st.radio(question, options[key])


if st.button('Lihat Hasil'):
    scores = calculate_score(answers)
    result = max(scores, key=scores.get)

    print(scores["Programmer"])  

    
    if result == 'Programmer':
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnJ3YTVmdHU2dTJ4bzRybWo0dzA1eXJvYWZ6ZXAwMHZvdHZsODQwZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3oKIPnAiaMCws8nOsE/giphy.gif", caption="Programmer")
    elif result == 'Designer':
        st.image("https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dGJtOHczcmE3YmluYW1uYWczOW1sYTMwdGNtMXNjNXF5ODliYTBkZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/absVClYNxIyrN1lOJr/giphy.gif", caption="Designer")
    else:
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHVqNXZyd21xOHc1aXloNWgxZXBkbnh5dmU3bGt3eGQ1cTFpcWl1aCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/7c8QeB0VMddFOuu4iR/giphy.gif", caption="Data Scientist")

    
    st.subheader(f'Anda cocok menjadi: {result}')
    st.write(f'**Skor Anda**')
    
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    for profession, score in sorted_scores:
        st.write(f'**{profession} {score}**')
