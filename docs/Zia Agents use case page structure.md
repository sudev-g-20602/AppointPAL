Agents use case structure (Make a copy)   

  
**Agent name** *****   
**Agent tagline** ***** ** ** **(Eg: ** **Instantly triages and routes support tickets, so no request sits unanswered)**   
## Use case *   
* What problem is the agent trying to solve?/ What does the agent do?   
* One business scenario   
* Quick examples of inputs   
\<demo video of input and output\\\>  (optional)   
## Walkthrough *   
* First, it does A   
* Then, it does B   
* Finally, it does C   
\<overall use case video from where it is deployed\. Eg: inside CRM, Cliq, as a chatbot, etc\.\.\\\>  (optional)   
## Overview *   
|  
**Purpose** <br>|  
(Eg: Automatically sorts and prioritizes incoming support tickets and routes them to the right team, cutting first-response time.) <br>|
|----------|----------|
|  
**Products** <br>|  (Example: Zoho Desk, Zoho CRM, and Zoho Cliq) <br>|
|  
**Best suited for** <br>|  (Who all will find the agent useful?) <br>|
|  
**Complexity** <br>|  (Easy, Moderate, High) <br>|
|  
**Deployment mode** <br>|  (Using Connection, Digital Employee) <br>|
|  
**Trigger** <br>|  (Button, chat-based, etc.,) <br>|
|  
**Tools** <br>|  (Names of all the tools. System tool names in  **black** , custom tool names in  **blue** ) <br>|
|  
**Knowledge Base** <br>|  (Names/headers of the sources used) <br>|
|  
**Model Configuration** <br>|  (LLM and its model) <br>|
|  
**Constraints** <br>|  (What the agent is restricted to do or limited to) <br>|
  

  
## Configuration *   
**Pre-requisites**   
* Upload the relevant files listed under the Knowledge Base section    
* Create a connection with the following scopes: a, b, c   
* Create a tool group and import the following custom tools: x, y, z   
* Test each tool and mark as ready.   

**Agent Instructions** *****   

\<full instructions text\>   

**Knowledge Base**   

(for file formats .md, .pdf, .txt, .docx, add full text from the file)   

(for Workdrive or Learn, add full text from the page)   

(for web scraping, just mention the website url)   
(for private documents or the ones with real-customer data), just mention what kind of document it is)   
\<file 1 content \>   

\<file 2 content\>   

.   

.   
**Custom tools**   
\<Custom tool YAML in a code snippet\>   
(if Python functions are added as tools, add the function here in a code snippet)   

**Custom Guardrails**   
**Do's**   
* A   
* B   
* C   
  
**Don'ts**   
* A   
* B   
* C   
  
## Invocation *   
* **Deployment:**   How the deployment is consumed   
* **Integration Details: ** Platforms or services connected to your agent. Example: Zoho Flow, third-party APIs.   
* **External Tools Used: ** Tools used to build or host it. Example: Zoho Catalyst, serverless functions.   
* **How Users Interact With It:**   How a user engages with the agent. Example: a button in CRM, a chat widget.   
* **How It's Triggered: ** What starts the agent. Example: a button click, a record update, a scheduled time.   
* **Where It's Deployed: ** Where the agent lives. Example: Zoho CRM, Zoho Desk, a standalone web app.   
## Observability   
* Logs and execution history   
* Error handling   
* Monitoring and metrics   
* Debugging   
  
### Supporting Code s   
\<use code snippets\>   
* Backend functions   
* Catalyst/serverless code   
* Middleware   
* Helper scripts   
* Other code used outside Zia Agents   
---  
  
**_For multi-agent setups, list each agent here, with all configuration sub-headers retained under the agent's name as the header._**   
  
  
