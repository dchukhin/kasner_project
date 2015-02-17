from models import SearchTerm, SearchBrowser

def get_search_stats():
    terms=SearchTerm.objects.filter()
    browsers=SearchBrowser.objects.filter()
    stats=[terms, browsers]
    return stats
