from utils import html_getter, get_question_list, parse_question
import regex
from models.question import Question

class FormScrapper:
    def fetch_from_url(url):
        html = html_getter('https://docs.google.com/forms/viewform?bc=transparent&embedded=true&f=%2522Open%2BSans%2522%252C%2Bsans-serif&hl=en&htc=%2523eeeeee&id=10ABB4PujTmnYjdfZT1eg2sDw8vplaMpgc9VQkdQSXOg&lc=%2523298cca&pli=1&tc=%2523616161&ttl=0')

        questions = get_question_list(html)

        objs = []
        for question in questions:
            raw = parse_question(question)
            if raw:
                objs.append(Question(raw))

        dict = {}    
        for obj in objs:
            dict[obj.id] = obj.to_dict()

        return(dict)