# Please install OpenAI SDK first: `pip3 install openai`
#用法在代码注释


try:
    from openai import OpenAI
except:
    import pip
    print("There are not a Wheel named openai")
    
    pip.main(["install","openai"])


while True:
    #输入询问内容
    #输入exit退出
    usrmess=input(">>")
    usrmess=="exit" and exit()

    client = OpenAI(api_key="<Key>", base_url="https://api.deepseek.com")

    
    #发送推理请求
    response = client.chat.completions.create(
        model="deepseek-reasoner",
        messages=[
            #role system content后面内容是先行提示词会加在你发送的询问内容之前
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": usrmess},
        ],
        stream=False
    )
    print("wait ...")
    
    #推理完成保存推理内容,保存为markdown文档，用浏览器打开文件即可
    #存储当次输出结果
    with open("log-chat.md","w") as chat:
        chat.write(response.choices[0].message.content)
    
    #存储历次输出结果
    with open("log-chat.md.log","a") as chat:
        chat.write(response.choices[0].message.content)
    
    #存储当次思考内容
    with open("log-think.md","w") as think:
        think.write(response.choices[0].message.reasoning_content+"\n\n")
    
    #存储历次思考内容
    with open("log-think.md.log","a") as think:
        think.write(response.choices[0].message.reasoning_content+"\n\n")
    

