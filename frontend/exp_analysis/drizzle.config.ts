/**
 * Drizzle ORM 配置文件
 *
 * 此文件的主要作用是配置 Drizzle Kit，用于数据库迁移和代码生成。
 * 它定义了数据库连接信息、schema 文件位置、输出目录和数据库方言。
 * 通过环境变量加载数据库 URL，并确保其存在以避免运行时错误。
 */

import { defineConfig } from "drizzle-kit";
import * as dotenv from "dotenv";
dotenv.config({ path: ".env" });

if (!process.env.DATABASE_URL) {
  throw new Error("DATABASE_URL is not set");
}

export default defineConfig({
  schema: "./src/lib/db/schema.ts",
  out: "./drizzle",
  dialect: "postgresql",
  dbCredentials: {
    url: process.env.DATABASE_URL,
  },
});
