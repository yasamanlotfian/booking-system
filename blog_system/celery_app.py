from celery import Celery

celery_app = Celery(
    "blog_system",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=[
        "task.task_video",
    ],
)