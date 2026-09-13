import re # this is used to 
from src.model import ModelInterface 
from src.tools import Tool

class Agent :
    def __init__(
            self,
            tools: list[Tool],
            instructions: str
            ):
        self.model = ModelInterface()

        #ttols available as functions to the agent
        self.tools = {tool.name: tool for tool in tools}

        #agent instructions to set behaviour
        self.instructions = instructions

    async def run(
            self,
            user_input : str
            ):
        history = [
            {
                "role":"system",
                "content":self.instructions
            },
            {   
                "role":"user",
                "content":user_input
            }
        ]
        #lloks for tool acllls in the forms: functions() where functin is replaced by the tool name
        tool_call_pattern = re.compile(r"^(\w+)\((.*)\)$",re.DOTALL)


        #call te model
        response = self.model.chat_completion(history)

        #check the output for a tool match
        match = tool_call_pattern.match(response.strip())


        if match:
            name, arg = match.groups()
            tool = self.tools.get(name)
            if tool:
                #check or arguments 
                result = tool.run(arg) if arg else tool.run("")
                history.append(
                    {   
                        "role":"assistant",
                        "content":response.strip()
                    }
                )
                history.append(
                    {   
                        "role":"tool",
                        "content":result
                    }
                )
                return result.strip()
        else:
            history.append(
                {   
                    "role":"assistant",
                    "content":response.strip()
                }
            )

            return response.strip()