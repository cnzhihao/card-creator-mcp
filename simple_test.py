#!/usr/bin/env python3
"""
简化测试脚本，直接测试DocGenius服务的功能
"""

import asyncio
import sys
from pathlib import Path

# 添加当前目录到Python路径
sys.path.insert(0, str(Path(__file__).parent))

from main_service import list_available_templates, get_template_details, create_image_from_html

def test_templates():
    """测试模板相关功能"""
    print("🧪 开始测试DocGenius服务...")
    
    # 调试: 检查模板目录
    from pathlib import Path
    template_dir = Path("templates")
    print(f"\n🔍 调试信息:")
    print(f"  - 模板目录存在: {template_dir.is_dir()}")
    if template_dir.is_dir():
        md_files = list(template_dir.glob("*.md"))
        print(f"  - 找到.md文件: {len(md_files)}")
        for md_file in md_files:
            print(f"    - {md_file.name}")
    
    # 测试1: 列出可用模板
    print("\n📋 测试1: 列出可用模板")
    templates = list_available_templates()
    print(f"找到 {len(templates)} 个模板:")
    for template in templates:
        print(f"  - {template['name']}: {template['description']}")
    
    if not templates:
        print("❌ 没有找到模板文件")
        return False
    
    # 测试2: 获取模板详情
    print("\n📝 测试2: 获取模板详情")
    for template in templates:
        template_name = template['name']
        details = get_template_details(template_name)
        
        if 'error' in details:
            print(f"❌ 获取模板 {template_name} 详情失败: {details['error']}")
        else:
            print(f"✅ 模板 {template_name}:")
            print(f"  - 描述: {details.get('description', 'N/A')}")
            print(f"  - 尺寸: {details.get('width', 'N/A')} x {details.get('height', 'N/A')}")
            print(f"  - 提示词长度: {len(details.get('prompt', ''))}")
    
    return True

async def test_image_generation():
    """测试图片生成功能"""
    print("\n🖼️ 测试3: 测试图片生成")
    
    # 测试HTML内容
    test_html = """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>测试卡片</title>
        <style>
            body {
                margin: 0;
                padding: 20px;
                background-color: #f4f4f5;
                font-family: '思源黑体', 'Microsoft YaHei', sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }
            .card {
                background: #ffffff;
                border-radius: 15px;
                padding: 40px;
                max-width: 600px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
                text-align: center;
            }
            h1 {
                color: #1e293b;
                margin-bottom: 20px;
            }
            p {
                color: #334155;
                font-size: 18px;
                line-height: 1.6;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>DocGenius 测试</h1>
            <p>这是一个测试卡片，用于验证HTML到图片的转换功能。</p>
            <p><strong>服务状态:</strong> 正常运行 ✅</p>
        </div>
    </body>
    </html>
    """
    
    try:
        result = await create_image_from_html(
            html_content=test_html,
            template_name="test",
            file_name="docgenius_test",
            width=800,
            height=600
        )
        print(f"✅ 图片生成结果: {result}")
        return True
    except Exception as e:
        print(f"❌ 图片生成失败: {e}")
        return False

async def main():
    """主测试函数"""
    print("=" * 50)
    print("DocGenius MCP服务测试")
    print("=" * 50)
    
    # 测试模板功能
    templates_ok = test_templates()
    
    if templates_ok:
        # 测试图片生成
        image_ok = await test_image_generation()
        
        if image_ok:
            print("\n🎉 所有测试通过！DocGenius服务工作正常。")
        else:
            print("\n⚠️ 图片生成测试失败，请检查Playwright配置。")
    else:
        print("\n❌ 模板测试失败，请检查templates目录。")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    asyncio.run(main()) 