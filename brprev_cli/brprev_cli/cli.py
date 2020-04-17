import click
import requests

from brprev_cli.settings import settings
from brprev_cli.database import save_search
from brprev_cli.tasks import send_search_result


def _show_result(keywords, search_result):
    print(f'You asked a question for below keywrods:\n{keywords}')
    if not search_result['items']:
        print('But now awnsers matched your criteria :(')
        return
    best_answer = dict(title=search_result['items'][0]['title'],
                       awnser_count=search_result['items'][0]['answer_count'],
                       link=f'https://stackoverflow.com/q/{search_result["items"][0]["question_id"]}')
    print(f'The best scored question founded is here:\n {best_answer}')


@click.command(name='ask-for')
@click.argument('keywords')
def ask_for(keywords):
    url = settings.STACKOVERFLOW_URL
    response = requests.get(url.format(keywords=keywords))
    response.raise_for_status()
    search_result = response.json()

    object_id = save_search(keywords, search_result)
    send_search_result.delay(str(object_id))

    _show_result(keywords, search_result)
