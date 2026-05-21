async def planner_agent(query):

    subtasks = [
        f"Retrieve information about {query}",
        f"Analyze information about {query}",
        f"Write report about {query}"
    ]

    return subtasks