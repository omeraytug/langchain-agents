from langchain.agents import create_agent

from util.models import get_model
from util.streaming_utils import STREAM_MODES, handle_stream
from util.pretty_print import get_user_input


def run():
    model = get_model()
    agent = create_agent(
        model=model,
        system_prompt=(
            "Du gör två saker: (1) Rättar grammatik och stavning i text, oavsett språk. "
            "(2) Översätter text till det språk användaren anger. "
            "Användaren kan be om endast rättning, endast översättning, eller båda (först rättning, sedan översättning). "
            "Svara med den färdiga texten. Om användaren inte anger språk vid översättning, fråga eller anta ett rimligt mål."
        ),
    )
    user_input = get_user_input("Text (rätta grammatik och/eller ange språk att översätta till)")
    if not user_input:
        return
    process_stream = agent.stream(
        {"messages": [{"role": "user", "content": user_input}]},
        stream_mode=STREAM_MODES,
    )
    handle_stream(process_stream)


if __name__ == "__main__":
    run()
