# do not run this code, copy and paste the commands

# install ollama for debian headless
curl -fsSL https://ollama.com/install.sh | sh

exec $SHELL

ollama --version

ollama pull deepseek-r1-distill-qwen-7b

ollama serve

docker compose down
docker compose up -d --build

docker logs benchai-llm

# for testing
curl -X POST "http://localhost:11434/api/generate" \
     -H "Content-Type: application/json" \
     -d '{"model": "deepseek-r1-distill-qwen-7b", "prompt": "Hello, how are you?"}'
