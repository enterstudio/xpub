from prompter import Prompt

# prompt user for a particular mediatype
def get_mediatype(testing=False):
    config = {  
        "key": "mediatype",
        "text": "What type of file is this?",
        "info": "Specify the mediatype of the file being transferred.",
        "type": "list",
        "options": [
            "cat (CAT scan)",
            "emg (electromyography recording)",
            "xray (xray video, grid, or calibration object)",
            "video (standard video)",
            "other (none of the above)"
        ],
        "example": "video (standard video)",
        "require": True,
        "store": [],
        "regex": ""
    }
    prompt = Prompt(config)                     # create prompt based on config
    input = prompt(fixed=True, testing=testing) # prompt for input
    choice = input.split(' ')[0]                # get mediatype from input
    return choice


if __name__ == '__main__':

    # prompt user to select appropriate mediatype
    choice = get_mediatype(testing=True)
    assert choice == 'video'                    # given the example
