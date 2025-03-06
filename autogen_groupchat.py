import autogen
import json

with open('autogen_config.json', 'r') as config_file:
    config_data = json.load(config_file)

config_list_gpt4 = [config_data]

llm_config = {
    "cache_seed": 42,
    "temperature": 0,
    "config_list": config_list_gpt4,
    "timeout": 120,
}

# Create the agents
user_proxy = autogen.UserProxyAgent(
    name="Admin",
    system_message="A human admin. Interact with the planner to discuss the plan. Plan execution needs to be approved by this admin.",
    code_execution_config=False,
)

assistant = autogen.AssistantAgent(
    name="Assistant",
    llm_config=llm_config,
    system_message="You are an AI assistant capable of solving tasks and writing code when necessary.",
)

critic = autogen.AssistantAgent(
    name="Critic",
    system_message="Critic. Double check plan, claims, code from other agents and provide feedback. Check whether the plan includes adding verifiable info such as source URL.",
    llm_config=llm_config,
)

# Create the group chat
groupchat = autogen.GroupChat(
    agents=[user_proxy, assistant, critic],
    messages=[],
    max_round=50
)

# Create the manager
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

# Initiate the chat
user_proxy.initiate_chat(
    manager,
    message="Compare Apple stocks with Microsft stocks in previous year"
)
