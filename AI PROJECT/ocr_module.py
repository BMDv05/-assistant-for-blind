import easyocr

# تحميل المحرك
reader = easyocr.Reader(['ar', 'en'], gpu=False)

def get_text_from_frame(frame):
    if frame is None: return []
    try:
        results = reader.readtext(frame)
        # استخراج النصوص فقط
        return [text for (bbox, text, prob) in results if prob > 0.30]
    except:
        return []