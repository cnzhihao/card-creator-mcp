#!/usr/bin/env python3
"""
DocGenius MCP服务演示脚本
展示如何使用AI驱动的动态文档生成服务
"""

import asyncio
import sys
from pathlib import Path

# 添加当前目录到Python路径
sys.path.insert(0, str(Path(__file__).parent))

from main_service import list_available_templates, get_template_details, create_image_from_html

async def demo_knowledge_card():
    """演示生成知识卡片"""
    print("\n📚 演示生成知识卡片")
    print("-" * 40)
    
    # 用户输入的文本内容
    user_text = """
    **Python编程语言**
    
    Python是一种高级、解释型、交互式和面向对象的脚本语言。
    
    **主要特点:**
    - **简洁易读**: 语法简单，代码可读性强
    - **跨平台**: 可在Windows、Mac、Linux等系统运行  
    - **丰富的库**: 拥有强大的标准库和第三方库生态
    - **多领域应用**: 适用于Web开发、数据科学、AI等
    
    **热门框架:**
    - Django/Flask (Web开发)
    - NumPy/Pandas (数据分析)  
    - TensorFlow/PyTorch (机器学习)
    - FastAPI (API开发)
    """
    
    # 获取知识卡片模板详情
    template_details = get_template_details("knowledge_card")
    if 'error' in template_details:
        print(f"❌ 获取模板失败: {template_details['error']}")
        return
    
    # 模拟AI生成的HTML内容 (在实际使用中，这里应该调用LLM API)
    generated_html = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Python编程语言知识卡片</title>
        <style>
            body {{
                margin: 0;
                padding: 20px;
                background-color: #f4f4f5;
                font-family: '思源黑体', 'Microsoft YaHei', sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }}
            .card {{
                background: #ffffff;
                border-radius: 15px;
                padding: 40px;
                max-width: 700px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            }}
            h2 {{
                font-size: 32px;
                font-weight: bold;
                color: #1e293b;
                margin-bottom: 20px;
                text-align: center;
            }}
            p {{
                font-size: 18px;
                line-height: 1.6;
                color: #334155;
                margin-bottom: 16px;
            }}
            strong {{
                color: #1e293b;
            }}
            ul {{
                font-size: 18px;
                line-height: 1.6;
                color: #334155;
                margin-bottom: 16px;
            }}
            li {{
                margin-bottom: 8px;
            }}
            .highlight {{
                background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
                padding: 20px;
                border-radius: 10px;
                margin: 20px 0;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>Python编程语言</h2>
            <p>Python是一种高级、解释型、交互式和面向对象的脚本语言。</p>
            
            <div class="highlight">
                <p><strong>主要特点:</strong></p>
                <ul>
                    <li><strong>简洁易读</strong>: 语法简单，代码可读性强</li>
                    <li><strong>跨平台</strong>: 可在Windows、Mac、Linux等系统运行</li>
                    <li><strong>丰富的库</strong>: 拥有强大的标准库和第三方库生态</li>
                    <li><strong>多领域应用</strong>: 适用于Web开发、数据科学、AI等</li>
                </ul>
            </div>
            
            <p><strong>热门框架:</strong></p>
            <ul>
                <li>Django/Flask (Web开发)</li>
                <li>NumPy/Pandas (数据分析)</li>
                <li>TensorFlow/PyTorch (机器学习)</li>
                <li>FastAPI (API开发)</li>
            </ul>
        </div>
    </body>
    </html>
    """
    
    # 生成图片
    result = await create_image_from_html(
        html_content=generated_html,
        template_name="knowledge_card",
        file_name="python_language_card",
        width=template_details['width'],
        height=template_details['height']
    )
    
    print(f"✅ {result}")

async def demo_resume():
    """演示生成简历"""
    print("\n📄 演示生成简历")
    print("-" * 40)
    
    # 模拟简历数据
    resume_html = """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>张伟 - 软件工程师简历</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Microsoft YaHei', sans-serif;
                background: white;
                width: 827px;
                height: 1169px;
                display: flex;
            }
            .left-column {
                background: #2d3748;
                color: white;
                width: 30%;
                padding: 40px 30px;
            }
            .right-column {
                background: white;
                color: #1a202c;
                width: 70%;
                padding: 40px 30px;
            }
            h1 {
                font-size: 28px;
                margin-bottom: 10px;
                color: white;
            }
            h2 {
                font-size: 20px;
                margin-bottom: 15px;
                color: white;
            }
            h3 {
                font-size: 18px;
                margin-bottom: 10px;
                border-bottom: 2px solid #4a5568;
                padding-bottom: 5px;
                color: #1a202c;
            }
            .right-column h3 {
                border-bottom-color: #e2e8f0;
            }
            p, li {
                font-size: 14px;
                line-height: 1.6;
                margin-bottom: 8px;
            }
            .contact {
                margin-bottom: 30px;
            }
            .section {
                margin-bottom: 25px;
            }
            ul {
                padding-left: 20px;
            }
        </style>
    </head>
    <body>
        <div class="left-column">
            <div class="contact">
                <h1>张伟</h1>
                <h2>软件工程师</h2>
                <p>📧 zhangwei@email.com</p>
                <p>📱 13800138000</p>
                <p>🏠 北京市朝阳区</p>
                <p>💼 github.com/zhangwei</p>
            </div>
            
            <div class="section">
                <h3>技能专长</h3>
                <ul>
                    <li>Python, Java, JavaScript</li>
                    <li>Django, Spring Boot, React</li>
                    <li>MySQL, PostgreSQL, Redis</li>
                    <li>Docker, Kubernetes</li>
                    <li>AWS, Azure云服务</li>
                </ul>
            </div>
            
            <div class="section">
                <h3>语言能力</h3>
                <ul>
                    <li>中文 (母语)</li>
                    <li>英语 (流利)</li>
                    <li>日语 (基础)</li>
                </ul>
            </div>
        </div>
        
        <div class="right-column">
            <div class="section">
                <h3>工作经历</h3>
                <p><strong>高级软件工程师</strong> | 某科技公司 | 2021-至今</p>
                <ul>
                    <li>负责核心业务系统的架构设计和开发</li>
                    <li>优化系统性能，提升响应速度30%</li>
                    <li>指导团队成员，推动代码质量提升</li>
                </ul>
                
                <p><strong>软件工程师</strong> | 某互联网公司 | 2019-2021</p>
                <ul>
                    <li>参与微服务架构改造项目</li>
                    <li>开发RESTful API和前端界面</li>
                    <li>协助运维团队部署和监控系统</li>
                </ul>
            </div>
            
            <div class="section">
                <h3>教育背景</h3>
                <p><strong>计算机科学与技术学士</strong> | 某大学 | 2015-2019</p>
                <p>主修课程：数据结构、算法设计、数据库系统、网络编程</p>
            </div>
            
            <div class="section">
                <h3>项目经验</h3>
                <p><strong>电商平台微服务重构</strong></p>
                <ul>
                    <li>将单体应用拆分为15个微服务</li>
                    <li>使用Spring Cloud和Docker部署</li>
                    <li>系统可用性提升至99.9%</li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    """
    
    # 获取简历模板详情
    template_details = get_template_details("resume")
    
    # 生成图片
    result = await create_image_from_html(
        html_content=resume_html,
        template_name="resume",
        file_name="zhang_wei_resume",
        width=template_details['width'],
        height=template_details['height']
    )
    
    print(f"✅ {result}")

async def main():
    """主演示函数"""
    print("🎯 DocGenius MCP服务演示")
    print("=" * 50)
    
    # 显示可用模板
    print("\n📋 可用模板:")
    templates = list_available_templates()
    for template in templates:
        print(f"  • {template['name']}: {template['description']}")
    
    # 演示生成知识卡片
    await demo_knowledge_card()
    
    # 演示生成简历
    await demo_resume()
    
    print("\n🎉 演示完成！")
    print("检查 pic/ 目录查看生成的图片文件。")
    print("=" * 50)

if __name__ == "__main__":
    asyncio.run(main()) 