# 塔罗抽卡小游戏

一个优雅的塔罗牌网页应用：支持随机抽卡、详细解读、动画效果和神秘主题设计。

**功能特性：**
- 完整 78 张塔罗牌库（大阿卡那 22 张 + 小阿卡那 56 张）
- 每张牌含详细的正位/逆位解读
- 随机抽卡与动画效果
- 神秘主题背景（星空、月亮、紫色渐变）
- 响应式设计，适配多终端
- 牌面支持中英文双语显示

**快速运行：**

```bash
# 1. 创建虚拟环境
python3 -m venv .venv
source .venv/bin/activate

# 2. 安装依赖
pip install -r requirements.txt

# 3. 启动服务器（开启自动重载）
uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

访问浏览器：http://127.0.0.1:8000/

**项目结构：**
- `app.py` - FastAPI 后端，提供 API 和静态文件服务
- `tarot_data.py` - 完整 78 张牌的数据库和解牌逻辑
- `generate_images.py` - 动态生成牌面 SVG 文件脚本
- `static/` - 前端资源（HTML、JS、CSS、SVG 图片）
  - `images/` - 78 张牌的 SVG 图片文件

**API 接口：**
- `GET /api/draw?n=3` - 随机抽取 n 张牌，返回牌 ID 与逆位标志
- `POST /api/interpret` - 解读牌面，接受 JSON `{"cards": [{"id": int, "reversed": bool}, ...]}`
- `GET /` - 返回主页面 HTML

**牌面设计：**
- 中文名称（40px）和英文名称（28px）分两行展示
- 按花色使用不同配色（权杖、圣杯、宝剑、钱币、大阿卡那）
- 包含装饰边框、角标、纹理和投影效果
- 隐藏 ID 信息，聚焦于名称展示

**前端特性：**
- 抽卡时卡片带阶梯飞入动画
- 解牌结果逐项淡入动画
- 逆位牌面自动旋转 180 度
- 悬停卡片时显示紫色发光效果
- 神秘主题：深紫色星空背景 + 闪烁星星 + 月亮装饰

**技术栈：**
- 后端：Python 3 + FastAPI + Uvicorn
- 前端：HTML + CSS3 + JavaScript（无框架）
- 图片格式：SVG（矢量，可缩放无损）

**如何重新生成牌面图片：**

如需修改牌面设计，编辑 `generate_images.py` 中的 `SVG_TEMPLATE`，然后运行：
```bash
source .venv/bin/activate
python generate_images.py
```

这会更新 `static/images/` 中的所有 78 张牌。

---

*项目创建于 2026 年 2 月。建议在 macOS Safari/Chrome 或其他现代浏览器中使用。*
