# Course Helper Chatbot
This was a test of how an integration of a chatbot focused on privacy could be integrated into an LMS like Canvas.

## Purpose
The initial purpose of this was to test how a privacy-focused chatbot could ingest course materials to help students with basic questions on course content.

## Requirements and Set Up
> [!WARNING]  
> This relies on a specific branch of privateGPT, released in May 2023, known now as the "primordial" version. That project has since moved on and includes its own web interface. I built this around the same time to see what was possible to integrate into the Canvas Learning Management System. See the [Further Reading](#further-reading) section for the write-up on this project. 

> [!IMPORTANT] 
> To get this running (for whatever reason), you will need to install the primordial version of privateGPT, and then all of the requirements from the `requirements.txt` file. **This will not work without those prerequisites!**

1. Add an appropriate AI model to the `models` directory.
2. Add source documents to the `source_documents` directory and run `ingest.py` to give privateGPT access to your documents.
3. Watch for any errors - at this stage it is likely missing or conflicting requirements.

Once privateGPT is installed, the `app.py` file and `template` directory can be dropped into the same folder. Running the `app.py` file should launch privateGPT and the web server.


## How it works
The Course Helper uses a custom made "bridging app" that launches privateGPT and a webserver, then connects the two.
![Diagram showing the bridge app connecting the web interface to privateGPT](https://github.com/drphilchambers/course_helper/blob/main/%E2%80%8Ediagram_1_chatbot_system-1024x274.png)

Once created, the web interface portion, running locally, allows us to plug it into a Canvas page, like so:
![A screenshot showing regular Canvas text on the left, and the chat box interface on the right, connected to the LLM.](https://github.com/drphilchambers/course_helper/blob/main/canvas_integration-1024x627.png)

### Demo Video
This video is a sped up version of how the bot works.

https://github.com/drphilchambers/course_helper/assets/99165681/c3bd0ee5-0e7e-4c85-b476-57323948b49b


## Further Reading
Main article and write-up at the OSU Inspire Blog: [You won’t believe where AI could replace you next! (But you’re probably going to like it)](https://blogs.oregonstate.edu/inspire/2023/07/31/you-wont-believe-where-ai-could-replace-you-next-but-youre-probably-going-to-like-it/)
