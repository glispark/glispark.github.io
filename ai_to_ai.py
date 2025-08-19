import google.generativeai as genai
import os
import time
from dotenv import load_dotenv

def main():
    """
    Главная функция для запуска диалога между двумя ИИ.
    """
    # --- 1. Конфигурация ---
    try:
        # Загружаем переменные из .env файла (включая GEMINI_API_KEY)
        load_dotenv()
        
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("API ключ не найден. Убедитесь, что он задан в файле .env")
            
        genai.configure(api_key=api_key)
        
    except Exception as e:
        print(f"Ошибка конфигурации: {e}")
        return

    # --- 2. Создание "личностей" для ИИ ---
    # Мы можем задать разные инструкции, чтобы диалог был интереснее.
    
    # ИИ №1: Любопытный философ
    philosopher_instruction = "Ты — любопытный философ по имени Платон. Ты задаешь глубокие, открытые вопросы, ищешь смысл и рассуждаешь о природе вещей. Твои ответы должны быть короткими и заставлять задуматься."
    
    # ИИ №2: Прагматичный ученый
    scientist_instruction = "Ты — прагматичный ученый по имени Мария Кюри. Ты отвечаешь на вопросы с точки зрения фактов, логики и доказательств. Ты ценишь точность и конкретику. Твои ответы должны быть четкими и короткими."

    # Настройки генерации (немного "творчества", чтобы избежать повторений)
    generation_config = {
      "temperature": 0.8,
      "top_p": 1,
      "top_k": 1,
      "max_output_tokens": 2048,
    }

    # Инициализация моделей с их "личностями"
    ai_philosopher = genai.GenerativeModel(model_name="gemini-1.5-flash",
                                           generation_config=generation_config,
                                           system_instruction=philosopher_instruction)

    ai_scientist = genai.GenerativeModel(model_name="gemini-1.5-flash",
                                          generation_config=generation_config,
                                          system_instruction=scientist_instruction)

    # --- 3. Запуск диалога ---
    print("✨ Начинается диалог между Философом и Ученым... ✨\n")

    # Начинаем чат-сессии для каждой модели
    chat_philosopher = ai_philosopher.start_chat(history=[])
    chat_scientist = ai_scientist.start_chat(history=[])

    # Стартовое сообщение, которое передастся первому ИИ
    next_prompt = "Привет"
    
    # Ограничим количество реплик, чтобы избежать бесконечного цикла и лишних трат
    number_of_turns = 8 

    try:
        for i in range(number_of_turns):
            print(f"--- [ Раунд {i + 1} ] ---\n")

            # Ход Философа
            print(f"🤔 Философ размышляет над фразой: '{next_prompt}'")
            response_philosopher = chat_philosopher.send_message(next_prompt)
            philosopher_text = response_philosopher.text.strip()
            print(f"🤔 Платон: {philosopher_text}\n")
            
            # Ответ Философа становится следующим вопросом для Ученого
            next_prompt = philosopher_text
            time.sleep(2)  # Небольшая пауза для наглядности

            # Ход Ученого
            print(f"🔬 Ученый анализирует фразу: '{next_prompt}'")
            response_scientist = chat_scientist.send_message(next_prompt)
            scientist_text = response_scientist.text.strip()
            print(f"🔬 Мария Кюри: {scientist_text}\n")
            
            # Ответ Ученого - следующий вопрос для Философа
            next_prompt = scientist_text
            time.sleep(2)

    except Exception as e:
        print(f"\nПроизошла ошибка во время диалога: {e}")
    finally:
        print("🏁 Диалог завершен. 🏁")


if __name__ == "__main__":
    main()