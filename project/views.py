import logging

import cv2
import imutils
from pyzbar import pyzbar

from django.http import JsonResponse
from rest_framework.decorators import api_view


logger = logging.getLogger(__name__)


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
    if not barcodes:
        for angle in [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]:
            rotated = imutils.rotate_bound(image, angle)
            barcodes = pyzbar.decode(rotated)
            if barcodes:
                break
    logger.debug('filename %s recognition results %s', str(file_obj), barcodes)
    return JsonResponse({'text': barcodes[0].data.decode() if barcodes else ''})
