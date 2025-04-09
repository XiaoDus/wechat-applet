

## 项目结构

```
wechat-applet/
├── 前端（uniapp）/        # 基于 uni-app 的前端小程序代码
├── 后端（Django）/        # 基于 Django 的后端服务代码
└── 大屏（不属于小程序）/   # 独立的大屏展示模块（非小程序部分）
```

---

## 技术栈

- **前端**：uni-app（Vue.js）
- **后端**：Django（Python）
- **数据库**：根据 Django 配置，可能使用 SQLite、MySQL 等

---

## 核心功能

- **用户认证**：实现用户的注册、登录、权限管理等功能。
- **数据交互**：前端通过 API 与后端进行数据交互，展示和提交信息。
- **大屏展示**：独立于小程序的大屏展示模块，可能用于数据可视化或实时监控。

---

## 运行步骤

1. **后端启动**：
   - 进入 `后端（Django）` 目录。
   - 安装所需依赖：
     ```bash
     pip install -r requirements.txt
     ```
   - 运行数据库迁移：
     ```bash
     python manage.py migrate
     ```
   - 启动开发服务器：
     ```bash
     python manage.py runserver
     ```

2. **前端启动**：
   - 使用 HBuilderX 或其他支持 uni-app 的工具打开 `前端（uniapp）` 目录。
   - 根据需要配置后端 API 地址。
   - 运行并调试小程序。

