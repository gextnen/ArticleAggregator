from __future__ import absolute_import, unicode_literals

from celery import shared_task

from articles.management.commands.parse_habr import celery_handle


@shared_task
def parse_habr_everyday():
    """Calls the script parse_habr"""
    celery_handle()
