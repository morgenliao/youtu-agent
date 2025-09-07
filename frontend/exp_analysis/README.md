# utu_agent_exp_analysis

utu-agent `exp_analysis` 的前端页面

## 安装

1. 设置日志 SQL 服务器的环境变量
```bash
cd frontend/exp_analysis
cp .env.example .env  # 配置必要的密钥...
source .env
```

2. 安装 npm 包
```bash
npm install --legacy-peer-deps
```

使用 `--legacy-peer-deps` 选项的原因是 `react-json-view` 安装包的最新版本是 `1.21.3`。当与 `react` 版本 `19.0.0` 一起安装时，会生成警告。实际测试可以正常安装和使用。

## 开始使用

1. 构建项目
```bash
npm run build
```

2. 启动服务器
```bash
npm run start
```

启动项目后，您可以通过浏览器使用服务器的 IP 地址和默认端口 `3000` 访问服务器。如果要更改默认端口，可以在 `package.json` 的 `script` 部分的 `start` 命令中修改端口。
```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start -p 3000",
    "lint": "next lint",
    "db:migrate": "tsx src/lib/db/migrate.ts",
    "test:db": "tsx scripts/test-db-connection.ts"
  }
}
```

3. 测试数据库连接
```bash
npm run test:db
```
您可以调用上述命令来测试数据库服务是否可以正常访问。假设数据库服务已配置，您可以通过以下命令获取数据库中的第一个数据查询。
