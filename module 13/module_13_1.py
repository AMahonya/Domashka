import asyncio


async def start_strongman(name, power):
    print(f"Cилач {name} начал соревнования.")
    for i in range(1, 6):
        await asyncio.sleep(5 / power)
        print(f"Силач {name} поднял {i} шар ")
    print(f"Силач {name} закончил соревнования.")


async def start_tournament():
    strongman1 = asyncio.create_task(start_strongman('Pasha', 3))
    strongman2 = asyncio.create_task(start_strongman('Denis', 4))
    strongman3 = asyncio.create_task(start_strongman('Apollon', 5))

    await asyncio.gather(strongman1, strongman2, strongman3)
    print("Турнир закончен.")


asyncio.run(start_tournament())
