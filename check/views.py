from .models import Tag
from django.http import JsonResponse



def TagList(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        q = request.GET.get('q', None)
        if q is not None:
            if Tag.objects.filter(TagNo=q).exists():                
                return JsonResponse({"response":"Card Supported"}, safe=False)            
            else:
                return JsonResponse({"response":"Card Not Supported"}, safe=False)

        return JsonResponse({"response":"Invalid Query, try '/tag?q=queryparam"}, safe=False)

    
