import random

assistant_name = "ChatGPT"


def chat():
    greetings = ["привіт", "вітаю", "добрий день"]
    interview_topics = {
        "освіта": ["Добре. Давайте розпочнемо з освіти. Розкажіть про вашу освіту та академічні досягнення.",
                   "Освіта - важливий аспект. Розкажіть, будь ласка, про свою освіту та як вона підготувала вас до даної ролі."],
        "досвід роботи": [
            "Добре. Тепер давайте обговоримо ваш досвід роботи. Розповідайте про свої попередні місця роботи та досягнення на них.",
            "Перейдемо до вашого досвіду роботи. Будь ласка, опишіть ваші попередні робочі місця та досягнення на них."],
        "навички": [
            "Давайте перейдемо до наступної теми. Наприклад, ваші навички. Які навички ви вважаєте своїми сильними?",
            "Поговоримо про ваші навички. Які з них ви вважаєте своїми сильними?"]
    }
    count_conversations = 0
    conversation_history = []
    name = ''
    date_birth = ''
    response = f"{assistant_name}: Привіт! як вас звати?"
    print(response)
    user_input = input("Ви: ").lower()
    name = user_input
    response = f"{assistant_name}: Добрий день {name.title()}"
    print(response)

    while True:
        user_input = input("Ви: ").lower()
        conversation_history.append({"user": user_input, "assistant": ""})
        count_conversations += 1

        if any(keyword in user_input for keyword in greetings):
            response = f'{assistant_name}: Привіт! Як я можу допомогти вам підготуватися до співбесіди?'
            conversation_history[-1]["assistant"] = response
            print(response)
            count_conversations += 1

        elif "підготовка" in user_input:
            response = f'{assistant_name}: Виберіть тему для обговорення: {", ".join(interview_topics.keys())}'
            conversation_history[-1]["assistant"] = response
            print(response)
            count_conversations += 1

        elif any(topic in user_input for topic in interview_topics):
            selected_topic = next((topic for topic in interview_topics if topic in user_input), None)
            response = random.choice(interview_topics[selected_topic])
            conversation_history[-1]["assistant"] = response
            print(response)
            count_conversations += 1

            user_input = input("Ви: ").lower()
            print(f"{assistant_name}: Добре зрозуміло.) Допомогти ще чимось?")
            conversation_history[-1]['user'] = user_input

        elif "дякую" in user_input or "дякую за допомогу" in user_input:
            response = f"{assistant_name}: Не за що! Я завжди тут, якщо вам знадобиться додаткова допомога."
            conversation_history[-1]["assistant"] = response
            print(response)

        elif "завершити" in user_input or "завершити роботу" in user_input:
            print(f"Лічильник питань-відповідей: {count_conversations}")
            response = f"{assistant_name}: Бажаю успіху на співбесіді! Я завжди тут, якщо вам знадобиться додаткова допомога."
            conversation_history[-1]["assistant"] = response
            break

        else:
            response = f"{assistant_name}: Вибачте, я не зрозумів ваш запит. Чи можете повторити або сформулювати по-іншому?"
            conversation_history[-1]["assistant"] = response
            print(response)
            count_conversations += 1

    print("\nІсторія розмови:")
    for conversation in conversation_history:
        print(f"Ви: {conversation['user']}")
        print(f"{assistant_name}: {conversation['assistant']}")


if __name__ == '__main__':
    chat()
