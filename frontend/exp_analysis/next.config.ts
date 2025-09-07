/**
 * Next.js 配置文件
 *
 * 此文件的主要作用是配置 Next.js 应用的构建和运行时行为。
 * 它定义了开发环境的允许源，以确保安全性和开发便利性。
 * 可以在这里添加其他配置选项，如环境变量、图片优化、重定向等。
 */

import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  allowedDevOrigins: ['127.0.0.1'],
};

export default nextConfig;
