from django.core.management.base import BaseCommand, CommandError
from landing.models import Video
from . import _videoman as videoman

class Command(BaseCommand):
    help = 'Updates the videos db'

    def handle(self, *args, **options):
        videos = videoman.make_vieo_objects(
            videoman.get_latest_uploads()
        )
        for video in videos:
            # if video exists already
            if not Video.objects.filter(vid_id=video.vid_id):
                n_vid_entry = Video(
                    vid_id=video.vid_id,
                    title=video.title,
                    description=video.description,
                    thumb=video.thumb,
                    date_time=video.date_time,
                    url=video.url
                )
                n_vid_entry.save()
        return

"""
proj = Project(name = name, description = desc, author = puser)
		proj.save()

"""
