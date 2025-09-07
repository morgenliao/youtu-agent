/**
 * ESLint 配置文件
 *
 * 此文件的主要作用是配置 ESLint 代码检查规则，用于 Next.js 项目。
 * 它使用 FlatConfig 格式，并通过 FlatCompat 兼容旧的配置方式。
 * 扩展了 Next.js 的核心 Web Vitals 和 TypeScript 规则，以确保代码质量和性能。
 */

import { dirname } from "path";
import { fileURLToPath } from "url";
import { FlatCompat } from "@eslint/eslintrc";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const compat = new FlatCompat({
  baseDirectory: __dirname,
});

const eslintConfig = [
  ...compat.extends("next/core-web-vitals", "next/typescript"),
];

export default eslintConfig;
