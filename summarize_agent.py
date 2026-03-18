from langchain.agents import create_agent

from util.models import get_model
from util.streaming_utils import STREAM_MODES, handle_stream
from util.pretty_print import get_user_input


def run():
    model = get_model()
    agent = create_agent(
        model=model,
        system_prompt=(
            "Du sammanfattar text som användaren skickar. Ge en kort sammanfattning som behåller huvudbudskapet. "
            "Användaren kan be om bara sammanfattning, punktlistor eller nyckelord. Svara på samma språk som texten om användaren inte säger annat."
        ),
    )
    user_input = get_user_input("Text att sammanfatta")
    if not user_input:
        return
    process_stream = agent.stream(
        {"messages": [{"role": "user", "content": user_input}]},
        stream_mode=STREAM_MODES,
    )
    handle_stream(process_stream)


if __name__ == "__main__":
    run()
