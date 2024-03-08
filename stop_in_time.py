# # Create a function that sums 2 numbers and returns their result after a few 
# # seconds.
# # - It will receive as parameters the 2 numbers to add and the seconds that
# # it must take time in finish their execution.
# # - If the language the support it, it must return the result asynchronous, that
# # is, without stopping the execution of the main program.
# # It could be run multiple times at the same time.   

# Even loop => It's a component of an asyncio library that allows you to run tasks
# simultaneously in a single thread. 

import asyncio  # Allows asynchronous programming.

async def async_addition(number_1, number_2, wait_time):  # Asynchronous function.
    await asyncio.sleep(wait_time)  # Delay time.
    print(number_1 + number_2)

async def async_exec():
    task_1 = asyncio.create_task(async_addition(10, 10, 4))  # Create an asynchronous task.
    task_2 = asyncio.create_task(async_addition(20, 20, 2))
    task_3 = asyncio.create_task(async_addition(30, 30, 6))

    await task_1  # Execute the task 
    await task_2
    await task_3


asyncio.run(async_exec())  # Run the even loop.