from models import Search

def get_search_stats():
    stats=Search.objects.filter()
    return stats
