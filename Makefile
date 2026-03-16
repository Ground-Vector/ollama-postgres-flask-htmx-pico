build:
	docker compose build
	docker compose up db --detach
	docker compose up ollama --detach
	docker compose exec ollama ollama pull gemma3:4b

up:
	docker compose up
