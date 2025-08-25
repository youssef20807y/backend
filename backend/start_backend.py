#!/usr/bin/env python3
"""
سكريبت تشغيل الـ Backend لأكاديمية الإبداع
"""

import uvicorn
import os
from main import app

if __name__ == "__main__":
    # إعدادات التشغيل
    host = "0.0.0.0"  # السماح بالوصول من أي عنوان IP
    port = 8000       # المنفذ المطلوب للـ Angular
    
    print("🚀 بدء تشغيل خادم أكاديمية الإبداع...")
    print(f"📍 العنوان: http://{host}:{port}")
    print("🔗 يمكن الوصول من Angular على: http://localhost:4200")
    print("⏹️  اضغط Ctrl+C لإيقاف الخادم")
    print("-" * 50)
    
    # تشغيل الخادم
    uvicorn.run(
        app,
        host=host,
        port=port,
        reload=True,  # إعادة التحميل التلقائي عند التغيير
        log_level="info"
    ) 
"""
سكريبت تشغيل الـ Backend لأكاديمية الإبداع
"""

import uvicorn
import os
from main import app

if __name__ == "__main__":
    # إعدادات التشغيل
    host = "0.0.0.0"  # السماح بالوصول من أي عنوان IP
    port = 8000       # المنفذ المطلوب للـ Angular
    
    print("🚀 بدء تشغيل خادم أكاديمية الإبداع...")
    print(f"📍 العنوان: http://{host}:{port}")
    print("🔗 يمكن الوصول من Angular على: http://localhost:4200")
    print("⏹️  اضغط Ctrl+C لإيقاف الخادم")
    print("-" * 50)
    
    # تشغيل الخادم
    uvicorn.run(
        app,
        host=host,
        port=port,
        reload=True,  # إعادة التحميل التلقائي عند التغيير
        log_level="info"
    ) 
"""
سكريبت تشغيل الـ Backend لأكاديمية الإبداع
"""

import uvicorn
import os
from main import app

if __name__ == "__main__":
    # إعدادات التشغيل
    host = "0.0.0.0"  # السماح بالوصول من أي عنوان IP
    port = 8000       # المنفذ المطلوب للـ Angular
    
    print("🚀 بدء تشغيل خادم أكاديمية الإبداع...")
    print(f"📍 العنوان: http://{host}:{port}")
    print("🔗 يمكن الوصول من Angular على: http://localhost:4200")
    print("⏹️  اضغط Ctrl+C لإيقاف الخادم")
    print("-" * 50)
    
    # تشغيل الخادم
    uvicorn.run(
        app,
        host=host,
        port=port,
        reload=True,  # إعادة التحميل التلقائي عند التغيير
        log_level="info"
    ) 