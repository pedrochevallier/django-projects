from django.shortcuts import render
import qrcode
from io import BytesIO

def index(request):
    qr_image = None
    if request.method == 'POST':
        url = request.POST.get('url')
        if url:
            # Generate QR code image
            qr = qrcode.QRCode(version=1, box_size=10, border=1)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color='black', back_color='white')

            # Save QR code image to buffer
            buffer = BytesIO()
            img.save(buffer, format='PNG')
            qr_image = buffer.getvalue()

    context = {'qr_image': qr_image}
    return render(request, 'qrmaker/index.html', context=context)