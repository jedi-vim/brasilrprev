from celery import Celery
from brprev_cli.settings import settings
from brprev_cli.database import get_search
from brprev_cli.external.brprev_bot import broadcast_search_result

app = Celery(__name__, broker=f'redis://guest@{settings.REDIS_HOST}/1')


@app.task(max_retries=10, default_retry_delay=5)
def send_search_result(search_id):
    search_data = get_search(search_id)
    if not search_data:
        return
    broadcast_search_result(search_data)
    print(f'Enviei a pesquisa {search_id}')
