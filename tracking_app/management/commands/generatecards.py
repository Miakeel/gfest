from django.core.management.base import BaseCommand, CommandError

from tracking_app.models import QrCodeId
from PIL import Image, ImageOps, ImageDraw, ImageFont
import qrcode
from uuid import uuid4

from pathlib import Path

class Command(BaseCommand):
    help = 'Generates a4 size images with unique uuid4 qrcodes'

    def add_arguments(self, parser):
        parser.add_argument('pages', type=int)

    def handle(self, *args, **options):
        nr_pages = options['pages']

        
        
        qr_border = 10
        qr_width = 360 - qr_border
        qr_height = 360 - qr_border

        template_border = 20
        template_width = 1138 - template_border
        template_height = 650 - template_border

        page_height = 2480
        page_width = 3508

        for k in range(nr_pages):
            page = Image.new('RGB', (page_width, page_height), (255, 255, 255))
            
            for i in range(int(page_height/(template_height+10))):
                for j in range(int(page_width/template_width)):
                    qrcodeid = QrCodeId.objects.create()
                    template = Image.open('tracking_app/management/commands/template.png')
                    template = template.resize((template_width, template_height))
                    template = ImageOps.expand(template, border=template_border)
                    temporary=template
                    qr = qrcode.QRCode(
                        version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10,
                        border=2
                    )
                    qr.add_data(qrcodeid.id)
                    qr.make()
                    code = ImageDraw.Draw(temporary)
                    
                    qr_img = qr.make_image()
                    qr_img = qr_img.resize((qr_width, qr_height))
                    qr_img = ImageOps.expand(qr_img, border=qr_border)
                    myFont=ImageFont.truetype("tracking_app/management/commands/FreeMono.ttf", 40)
                    code.text((75,160), str(qrcodeid.id), font=myFont)
                    temporary.paste(qr_img, (665, 210))
                    
                    page.paste(temporary, (j * (template_width+template_border), i * (template_height+20)))
            page.save('E:\cards\%s.png'%k)
