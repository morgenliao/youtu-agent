/*
 * Copyright 2025 morgenliao. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { ThemeProvider } from "@/components/theme-provider";

/**
 * Inter 字体配置，用于应用的主要字体。
 * 从 Google Fonts 加载 Inter 字体，仅包含拉丁字符集。
 */
const inter = Inter({ subsets: ["latin"] });

/**
 * 应用的元数据配置。
 * 定义页面的标题和描述，用于 SEO 和浏览器标签。
 */
export const metadata: Metadata = {
    title: "LLM Agent Evaluations",
    description: "Evaluate your LLM Agent performance",
};

/**
 * 根布局组件。
 * 这是 Next.js 应用的根布局，包装所有页面内容。
 * 提供主题提供者、字体类和基本的 HTML 结构。
 *
 * @param children - 要渲染的子组件，通常是页面内容。
 * @returns 完整的 HTML 文档结构。
 */
export default function RootLayout({
                                       children,
                                   }: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <html lang="en" suppressHydrationWarning>
        <body className={inter.className}>
        <ThemeProvider attribute="class" defaultTheme="system" enableSystem>
            {children}
        </ThemeProvider>
        </body>
        </html>
    );
}