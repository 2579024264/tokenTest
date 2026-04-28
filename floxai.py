import anthropic
import time
 
client = anthropic.Anthropic(
    api_key="sk-Ec1lDRKSn5DoZ1PJpa9WaI_4KP3IzSYMHJnT_XerhNo",
    base_url="https://api.floxai.io"
)

# Call the API 5 times and measure latency
total_latency = 0
num_calls = 5

for i in range(num_calls):
    start_time = time.time()
    
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1000,
        temperature=1,
        messages=[
            {
                "role": "user",
                "content":"ping"
            }
        ]
    )
    
    end_time = time.time()
    latency = end_time - start_time
    total_latency += latency
    
    # print(f"Call {i+1}: {message.content[0].text}")
    print(f"Latency: {latency:.3f} seconds\n")

avg_latency = total_latency / num_calls
print(f"Average Latency: {avg_latency:.3f} seconds")
print(f"Total Time: {total_latency:.3f} seconds")