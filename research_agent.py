from langchain.agents import create_agent
from langchain_community.agent_toolkits.openapi.toolkit import RequestsToolkit
from langchain_community.utilities.requests import TextRequestsWrapper

from util.models import get_model
from util.streaming_utils import STREAM_MODES, handle_stream
from util.pretty_print import get_user_input


def run():
    model = get_model()
    tools = RequestsToolkit(
        requests_wrapper=TextRequestsWrapper(headers={}),
        allow_dangerous_requests=True,
    ).get_tools()

    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=(
            "Du är en forskningsassistent. Din uppgift är att hämta innehåll från webbadresser (URL:er) "
            "som användaren anger, sammanfatta sidan och svara på frågor om innehållet. "
            "Använd requests_get med en fullständig URL. "
            "Ge korta, tydliga sammanfattningar och svar på svenska."
        ),
    )
    user_input = get_user_input(
        "Ange en URL eller ställ en fråga (t.ex. 'Sammanfatta https://...')"
    )
    process_stream = agent.stream(
        {"messages": [{"role": "user", "content": user_input}]},
        stream_mode=STREAM_MODES,
    )
    handle_stream(process_stream)


if __name__ == "__main__":
    run()
