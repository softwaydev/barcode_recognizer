from django.http import JsonResponse
from rest_framework.decorators import api_view
import cv2
from pyzbar import pyzbar


@api_view(['post'])
def upload(request):
    """
    ---
    parameters:
        - name: filename
          type: file
    """
    file_obj = request.FILES['filename']
    image = cv2.imread(file_obj.temporary_file_path())
    barcodes = pyzbar.decode(image)
    print(barcodes)
    return JsonResponse({'text': barcodes[0].data.decode() if barcodes else ''})
