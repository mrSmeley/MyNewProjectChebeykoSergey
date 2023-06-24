import openai

api_key = "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"


def get_neiro_memes():
    openai.api_key = api_key
    img = openai.Image.create(
        prompt='dog and cat memes',
        n=10,
        size='512x512',
        response_format='url'
    )
    print(img)

get_neiro_memes()





