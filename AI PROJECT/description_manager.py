def generate_description(objects, texts):
    description_parts = []
    alerts = []

    # 1. تحليل الأشياء المكتشفة 
    for obj in objects:
        label = obj.get('type', 'شيء')
        distance = obj.get('distance', '')
        
        # صياغة وصف للشيء
        desc = f"{label} {distance}"
        description_parts.append(desc)
        
        # إضافة تحذير إذا كان الشيء قريباً جداً
        if distance == "قريب":
            alerts.append(f"تحذير: يوجد {label} قريب منك")

    # 2. إضافة النصوص المكتشفة
    if texts:
        # دمج قائمة النصوص في جملة واحدة
        text_info = "، نصوص مكتوبة تقول: " + " و ".join(texts)
        description_parts.append(text_info)

    # 3. صياغة الوصف النهائي
    if not description_parts:
        full_description = "المشهد هادئ ولا يوجد عوائق واضحة"
    else:
        full_description = "أمامك: " + "، و ".join(description_parts)

    return full_description, alerts