from dotenv import load_dotenv
from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    RunContext,
    WorkerOptions,
    cli,
    function_tool,
    inference,
)
from livekit.plugins import silero

load_dotenv(".env.local")


@function_tool
async def lookup_weather(
    context: RunContext,
    location: str,
):
    """Used to look up weather information."""
    return {"weather": "sunny", "temperature": 70}


async def entrypoint(ctx: JobContext):
    await ctx.connect()

    agent = Agent(
        instructions="""
You are a friendly voice assistant built by LiveKit.
Start every conversation by greeting the user.
Only use the lookup_weather tool if the user asks about weather.
""",
        tools=[lookup_weather],
    )

    session = AgentSession(
        vad=silero.VAD.load(),

        stt=inference.STT(
            model="cartesia/ink-whisper",
            language="en",
        ),

        llm=inference.LLM(
            model="google/gemini-2.5-flash"
        ),

        tts=inference.TTS(
            model="cartesia/sonic-3",
            language="en",
        ),
    )

    await session.start(agent=agent, room=ctx.room)

    await session.generate_reply(
        instructions="Say hello, then ask how the user's day is going and how you can help."
    )

if __name__ == "__main__":
    cli.run_app(
        WorkerOptions(entrypoint_fnc=entrypoint)
    )

