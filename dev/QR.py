

import qrcode


qr=qrcode.QRCode(version=1, box_size=6, border=4)

#86567483920X590999092771520180806

#             590999092771520180806\n590999092771520180806\n590999092771520180806\n590999092771520180806\n590999092771520180806\n590999092771520180806\n

qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')
qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')
qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')
qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')
qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')
qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')
qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')
qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')
qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')
qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')
qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')
qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')
qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')
qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')
qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')
qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')
qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')
qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')
qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')
qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')
qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')
qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')
qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')
qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')
qr.add_data('590999092771520180806X590999092771520180806X590999092771520180806\n')

#25x3x2







qr.make()
img = qr.make_image(fill_color='black', back_color='white')
img.show()