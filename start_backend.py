#!/usr/bin/env python3
"""
سكريبت تشغيل الـ Backend لأكاديمية الإبداع
"""

import uvicorn
import os
from main import app

if __name__ == "__main__":
    # إعدادات التشغيل
    host = os.getenv("HOST", "0.0.0.0")  # السماح بالوصول من أي عنوان IP
    port = int(os.getenv("PORT", "8000"))
    reload_flag = os.getenv("RELOAD", "false").lower() == "true"
    log_level = os.getenv("LOG_LEVEL", "info")
    
    # طباعة مختصرة فقط عند البدء
    print(f"🚀 بدء تشغيل الخادم على: http://{host}:{port}")
    
    # تشغيل الخادم
    uvicorn.run(
        app,
        host=host,
        port=port,
        reload=reload_flag,
        log_level=log_level
    ) 