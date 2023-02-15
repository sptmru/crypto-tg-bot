import multiprocessing
import subprocess
import os

current_dir = os.getcwd()

api_process = multiprocessing.Process(
    target=subprocess.run,
    kwargs={
        'args': f'{current_dir}/healthcheck.py',
        'shell': True
    })


bot_process = multiprocessing.Process(
    target=subprocess.run,
    kwargs={
        'args': f'{current_dir}/app.py',
        'shell': True
    })


if __name__ == '__main__':
    api_process.start()
    bot_process.start()