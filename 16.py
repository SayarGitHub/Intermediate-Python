import asyncio


async def find_divisible(inrange, div_by):
    print(f"finding nums in range {inrange} divisible  by {div_by}")
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 50000 == 0:
            await asyncio.sleep(0.00001)
    print(f"Done with number {inrange} divisible by {div_by}")
    return located


async def main():
    divs1 = loop.create_task(find_divisible(508000, 34113))
    divs2 = loop.create_task(find_divisible(100052, 3210))
    divs3 = loop.create_task(find_divisible(500, 3))
    await asyncio.wait([divs1, divs2, divs3])
    return divs1, divs2, divs3


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        d1, d2, d3 = loop.run_until_complete(main())
        print(d1.result())
    except Exception as e:
        print(e)
    finally:
        loop.close()

