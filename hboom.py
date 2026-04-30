import time
import requests

API_KEY = "sk-WBurshAaVIkkHv9pop41CXqXF7g5HkjW7UoHvaFYeWiCTCEt"
URL = "https://hboom.ai/v1/chat/completions"  # ⚠️ 改成真实接口

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "claude-opus-4-6",  # ⚠️ 用真实模型名
    "messages": [{"role": "user", "content": "ping"}],
    "max_tokens": 5
}

def test_latency(n=5):
    times = []
    success_count = 0

    for i in range(n):
        start = time.time()
        response = requests.post(URL, headers=headers, json=data)
        end = time.time()

        latency = end - start

        try:
            result = response.json()
        except:
            result = {}

        # ✅ 判断是否真正成功
        is_success = (
            response.status_code == 200 and
            "choices" in result
        )

        if is_success:
            success_count += 1
            times.append(latency)
            print(f"第{i+1}次: {latency:.2f} 秒 ✅")
        else:
            print(f"第{i+1}次: {latency:.2f} 秒 ❌ 失败")
            print("返回:", result)

    if times:
        print("\n平均延时: %.2f 秒" % (sum(times) / len(times)))
    else:
        print("\n没有成功请求")

    print(f"成功率: {success_count}/{n}")

test_latency(5)