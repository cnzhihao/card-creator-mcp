import os
import asyncio
from pathlib import Path
from fastmcp import FastMCP
from playwright.async_api import async_playwright
import frontmatter
import aiofiles

# 初始化 FastMCP 服务
mcp = FastMCP("DocGeniusService")
TEMPLATE_DIR = Path("templates")
OUTPUT_DIR = Path("pic")

@mcp.tool()
def list_available_templates() -> list[dict]:
    """
    扫描 'templates' 文件夹，列出所有可用文档模板的名称和描述。
    """
    if not TEMPLATE_DIR.is_dir():
        return []
    
    templates_info = []
    for md_file in TEMPLATE_DIR.glob("*.md"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            post = frontmatter.loads(content)
            templates_info.append({
                "name": md_file.stem,
                "description": post.metadata.get("description", "无可用描述")
            })
        except Exception as e:
            print(f"解析模板文件 {md_file} 时发生错误: {e}")
            continue
    return templates_info

@mcp.tool()
def get_template_details(template_name: str) -> dict:
    """
    根据模板名称，获取其完整的配置信息，包括提示词和所有元数据。
    """
    try:
        template_path = TEMPLATE_DIR / f"{template_name}.md"
        with open(template_path, 'r', encoding='utf-8') as f:
            file_content = f.read()
        post = frontmatter.loads(file_content)
        result = dict(post.metadata)
        result['prompt'] = post.content
        return result
    except FileNotFoundError:
        return {"error": f"名为 '{template_name}' 的模板不存在。"}
    except Exception as e:
        return {"error": f"读取或解析模板时发生错误: {e}"}

@mcp.tool()
async def create_image_from_html(html_content: str, template_name: str, file_name: str, width: int, height: int) -> str:
    """
    接收HTML代码字符串和指定的尺寸，在后台浏览器中渲染它，并按模板分类截图保存为PNG图片。
    """
    output_dir = OUTPUT_DIR / template_name
    output_dir.mkdir(parents=True, exist_ok=True)
    
    image_path = output_dir / f"{file_name}.png"

    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.set_viewport_size({"width": width, "height": height})
            await page.set_content(html_content)
            await asyncio.sleep(2)  # 等待内容完全加载
            await page.screenshot(path=str(image_path), full_page=True)
            await browser.close()
        return f"任务成功：图片已保存到 {image_path}"
    except Exception as e:
        return f"任务失败：截图过程中发生错误 - {str(e)}"

if __name__ == "__main__":
    mcp.run() 