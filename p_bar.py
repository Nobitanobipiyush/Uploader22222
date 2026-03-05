async def progress_bar(current, total):
    percentage = current * 100 / total
    return f"{percentage:.2f}% completed"
