import os
from pathlib import Path

# 定义模板目录结构
template_structure = [
    "src/pages",
    "src/components",
    "src/content/members",
    "src/content/publications",
    "src/content/news",
    "public/images/logo",
    "public/images/members",
    "public/images/lab",
]

# 生成目录
for dir_path in template_structure:
    Path(dir_path).mkdir(parents=True, exist_ok=True)
print("✅ 目录结构创建完成！")

# 1. 生成 package.json（核心依赖和脚本，Vercel 识别关键）
package_json_content = '''{
  "name": "lab-website",
  "type": "module",
  "version": "0.1.0",
  "scripts": {
    "dev": "astro dev",
    "start": "astro dev",
    "build": "astro build",
    "preview": "astro preview",
    "astro": "astro"
  },
  "dependencies": {
    "astro": "^4.0.0",
    "@astrojs/tailwind": "^5.0.0",
    "tailwindcss": "^3.3.0"
  }
}
'''
with open("package.json", "w", encoding="utf-8") as f:
    f.write(package_json_content)

# 2. 生成 astro.config.mjs（Astro 配置，自动适配 Vercel）
astro_config_content = '''import { defineConfig } from 'astro/config';
import tailwind from "@astrojs/tailwind";

// https://astro.build/config
export default defineConfig({
  integrations: [tailwind()],
  site: "https://lab-website-xxx.vercel.app", // 后续替换为你的 Vercel 域名或自定义域名
});
'''
with open("astro.config.mjs", "w", encoding="utf-8") as f:
    f.write(astro_config_content)

# 3. 生成 tailwind.config.js（样式配置，无需改，按需调整颜色）
tailwind_config_content = '''/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        primary: '#165DFF', // 课题组主色调（可替换为学校/实验室颜色）
        secondary: '#6B7280', // 辅助色
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
'''
with open("tailwind.config.js", "w", encoding="utf-8") as f:
    f.write(tailwind_config_content)

# 4. 生成 src/components/Navbar.astro（导航栏组件）
navbar_content = '''---
---
<nav class="bg-white shadow-md fixed w-full z-10">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex justify-between h-16">
      <div class="flex items-center">
        <!-- Logo -->
        <a href="/" class="flex-shrink-0 flex items-center">
          <img class="h-8 w-auto" src="/images/logo/lab-logo.png" alt="课题组 Logo" />
          <span class="ml-2 text-xl font-bold text-primary">XX课题组</span>
        </a>
      </div>
      <!-- 导航链接 -->
      <div class="flex items-center space-x-4">
        <a href="/" class="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-primary">首页</a>
        <a href="/about" class="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-primary">关于我们</a>
        <a href="/members" class="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-primary">成员介绍</a>
        <a href="/publications" class="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-primary">研究成果</a>
        <a href="/news" class="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-primary">新闻动态</a>
        <a href="/contact" class="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-primary">联系方式</a>
      </div>
    </div>
  </div>
</nav>
'''
with open("src/components/Navbar.astro", "w", encoding="utf-8") as f:
    f.write(navbar_content)

# 5. 生成 src/components/Footer.astro（页脚组件）
footer_content = '''---
---
<footer class="bg-gray-50 border-t border-gray-200">
  <div class="max-w-7xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
    <div class="flex flex-col md:flex-row justify-between items-center">
      <div class="mb-4 md:mb-0">
        <p class="text-sm text-gray-500">© {new Date().getFullYear()} XX课题组 版权所有</p>
        <p class="text-sm text-gray-400">依托单位：XX大学 XX学院 XX实验室</p>
      </div>
      <div class="flex space-x-6">
        <a href="mailto:lab-email@xxx.edu.cn" class="text-gray-400 hover:text-primary">
          <span class="sr-only">邮箱</span>
          <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
          </svg>
        </a>
        <a href="https://github.com/你的课题组仓库" class="text-gray-400 hover:text-primary">
          <span class="sr-only">GitHub</span>
          <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
            <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd" />
          </svg>
        </a>
      </div>
    </div>
  </div>
</footer>
'''
with open("src/components/Footer.astro", "w", encoding="utf-8") as f:
    f.write(footer_content)

# 6. 生成 src/pages/index.astro（首页）
index_content = '''---
import Navbar from '../components/Navbar.astro';
import Footer from '../components/Footer.astro';
---
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>XX课题组 - 首页</title>
  <meta name="description" content="XX课题组专注于XX领域研究，依托XX大学XX实验室，致力于XX方向的创新与突破">
</head>
<body class="font-sans text-gray-800 bg-gray-50">
  <Navbar />
  <!-- 英雄区 -->
  <section class="pt-28 pb-16 bg-gradient-to-r from-primary/5 to-primary/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col md:flex-row items-center">
        <div class="md:w-1/2 mb-8 md:mb-0">
          <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
            欢迎来到 <span class="text-primary">XX课题组</span>
          </h1>
          <p class="text-xl text-gray-600 mb-6">
            专注于 <span class="font-semibold">AI+医疗影像</span>、<span class="font-semibold">机器学习优化</span> 领域的研究与创新
          </p>
          <p class="text-gray-500 mb-8">
            依托XX大学XX学院，我们致力于通过技术突破解决实际问题，培养顶尖科研人才，产出高水平学术成果。
          </p>
          <div class="flex space-x-4">
            <a href="/about" class="px-6 py-3 bg-primary text-white rounded-md hover:bg-primary/90 transition-colors">
              了解更多
            </a>
            <a href="/contact" class="px-6 py-3 bg-white border border-primary text-primary rounded-md hover:bg-primary/5 transition-colors">
              联系我们
            </a>
          </div>
        </div>
        <div class="md:w-1/2">
          <img src="/images/lab/lab-photo.jpg" alt="实验室照片" class="rounded-lg shadow-lg w-full h-auto" />
        </div>
      </div>
    </div>
  </section>

  <!-- 核心研究方向 -->
  <section class="py-16 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h2 class="text-3xl font-bold text-center mb-12">核心研究方向</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-gray-50 p-6 rounded-lg shadow-sm hover:shadow-md transition-shadow">
          <div class="w-12 h-12 bg-primary/10 rounded-full flex items-center justify-center mb-4">
            <svg class="h-6 w-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
            </svg>
          </div>
          <h3 class="text-xl font-semibold mb-2">AI 医疗影像分析</h3>
          <p class="text-gray-600">基于深度学习的病灶检测、影像分割与诊断辅助系统，提升医疗诊断效率与准确性。</p>
        </div>
        <div class="bg-gray-50 p-6 rounded-lg shadow-sm hover:shadow-md transition-shadow">
          <div class="w-12 h-12 bg-primary/10 rounded-full flex items-center justify-center mb-4">
            <svg class="h-6 w-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 4a2 2 0 114 0 2 2 0 01-4 0zM15 20H9a2 2 0 01-2-2V6a2 2 0 012-2h6a2 2 0 012 2v12a2 2 0 01-2 2z" />
            </svg>
          </div>
          <h3 class="text-xl font-semibold mb-2">机器学习优化</h3>
          <p class="text-gray-600">研究神经网络结构搜索、模型压缩与加速技术，解决大规模模型部署的效率与成本问题。</p>
        </div>
        <div class="bg-gray-50 p-6 rounded-lg shadow-sm hover:shadow-md transition-shadow">
          <div class="w-12 h-12 bg-primary/10 rounded-full flex items-center justify-center mb-4">
            <svg class="h-6 w-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
          </div>
          <h3 class="text-xl font-semibold mb-2">多模态数据融合</h3>
          <p class="text-gray-600">融合文本、图像、传感器数据，构建跨模态智能分析模型，应用于精准医疗、智能监测等场景。</p>
        </div>
      </div>
    </div>
  </section>

  <!-- 最新成果预览 -->
  <section class="py-16 bg-gray-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center mb-8">
        <h2 class="text-3xl font-bold">最新研究成果</h2>
        <a href="/publications" class="text-primary hover:underline">查看全部 →</a>
      </div>
      <div class="bg-white rounded-lg shadow-sm p-6">
        <ul class="space-y-4">
          <li class="border-b border-gray-100 pb-4">
            <p class="font-semibold">《Deep Learning for Lung Nodule Detection in CT Images》</p>
            <p class="text-gray-600 text-sm">IEEE Transactions on Medical Imaging, 2024 (SCI 一区，IF=11.0)</p>
            <p class="text-gray-500 text-sm mt-1">作者：张三, 李四, 王五*（通讯作者）</p>
          </li>
          <li class="border-b border-gray-100 pb-4">
            <p class="font-semibold">《Efficient Neural Network Compression via Knowledge Distillation》</p>
            <p class="text-gray-600 text-sm">NeurIPS 2023 (CCF A类会议)</p>
            <p class="text-gray-500 text-sm mt-1">作者：赵六, 张三, 王五*</p>
          </li>
          <li>
            <p class="font-semibold">国家自然科学基金项目：基于多模态融合的早期癌症诊断关键技术研究（No. 62371000）</p>
            <p class="text-gray-600 text-sm">资助金额：50万元，2024-2027</p>
            <p class="text-gray-500 text-sm mt-1">负责人：王五 教授</p>
          </li>
        </ul>
      </div>
    </div>
  </section>

  <Footer />
</body>
</html>
'''
with open("src/pages/index.astro", "w", encoding="utf-8") as f:
    f.write(index_content)

# 7. 生成 src/pages/about.astro（关于我们）
about_content = '''---
import Navbar from '../components/Navbar.astro';
import Footer from '../components/Footer.astro';
---
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>关于我们 - XX课题组</title>
</head>
<body class="font-sans text-gray-800 bg-gray-50">
  <Navbar />
  <section class="pt-28 pb-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h1 class="text-3xl font-bold mb-8">关于我们</h1>
      <div class="bg-white rounded-lg shadow-sm p-8">
        <h2 class="text-2xl font-semibold mb-4">课题组简介</h2>
        <p class="text-gray-600 mb-6">
          XX课题组成立于20XX年，依托XX大学XX学院XX实验室，是一支以中青年教师为核心、硕博研究生为骨干的创新型科研团队。
          课题组聚焦人工智能与医疗健康、机器学习优化等前沿交叉领域，致力于通过技术创新解决实际问题，推动学术进步与产业应用。
        </p>
        <p class="text-gray-600 mb-6">
          成立以来，课题组承担国家自然科学基金、省部级科研项目等XX项，在 IEEE TMI、NeurIPS、ICML 等顶级期刊和会议发表论文XX篇，
          申请发明专利XX项，部分成果已成功转化应用，获得行业广泛认可。
        </p>

        <h2 class="text-2xl font-semibold mb-4 mt-8">依托单位</h2>
        <p class="text-gray-600 mb-4">
          XX大学是国家“双一流”建设高校，XX学院拥有一级学科博士点、博士后流动站，
          实验室配备先进的计算设备和医疗影像数据平台，为课题组的科研工作提供坚实保障。
        </p>
        <img src="/images/lab/university-photo.jpg" alt="学校/学院照片" class="rounded-lg shadow-sm w-full h-auto my-6" />

        <h2 class="text-2xl font-semibold mb-4 mt-8">团队使命</h2>
        <ul class="list-disc list-inside text-gray-600 space-y-2">
          <li>深耕前沿领域，产出具有国际影响力的学术成果</li>
          <li>培养兼具科研能力与工程素养的复合型人才</li>
          <li>推动科研成果转化，服务国家战略与社会需求</li>
          <li>构建开放合作的科研生态，与国内外顶尖团队深度协作</li>
        </ul>
      </div>
    </div>
  </section>
  <Footer />
</body>
</html>
'''
with open("src/pages/about.astro", "w", encoding="utf-8") as f:
    f.write(about_content)

# 8. 生成 src/pages/members.astro（成员介绍，读取 Markdown 文件）
members_content = '''---
import Navbar from '../components/Navbar.astro';
import Footer from '../components/Footer.astro';
import { getCollection } from 'astro:content';

// 读取 members 目录下的所有 Markdown 文件
const members = await getCollection('members', ({ data }) => {
  // 按 role 排序（导师在前，学生在后）
  return data.role === 'teacher' || data.role === 'student';
});
const teachers = members.filter(m => m.data.role === 'teacher');
const students = members.filter(m => m.data.role === 'student');
---
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>成员介绍 - XX课题组</title>
</head>
<body class="font-sans text-gray-800 bg-gray-50">
  <Navbar />
  <section class="pt-28 pb-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h1 class="text-3xl font-bold mb-8">成员介绍</h1>

      <!-- 导师团队 -->
      <h2 class="text-2xl font-semibold mb-6">导师团队</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-12">
        {
          teachers.map(member => (
            <div class="bg-white rounded-lg shadow-sm overflow-hidden hover:shadow-md transition-shadow">
              <img src={member.data.avatar} alt={member.data.name} class="w-full h-64 object-cover" />
              <div class="p-6">
                <h3 class="text-xl font-semibold mb-1">{member.data.name}</h3>
                <p class="text-primary mb-3">{member.data.title}</p>
                <p class="text-gray-600 mb-4 text-sm">研究方向：{member.data.research}</p>
                <p class="text-gray-500 text-sm mb-4">{member.body}</p>
                <a href={`mailto:${member.data.email}`} class="text-sm text-primary hover:underline">
                  {member.data.email}
                </a>
              </div>
            </div>
          ))
        }
      </div>

      <!-- 学生团队 -->
      <h2 class="text-2xl font-semibold mb-6">学生团队</h2>
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
        {
          students.map(member => (
            <div class="bg-white rounded-lg shadow-sm p-6 hover:shadow-md transition-shadow">
              <img src={member.data.avatar} alt={member.data.name} class="w-full h-48 object-cover rounded-md mb-4" />
              <h3 class="text-lg font-semibold mb-1">{member.data.name}</h3>
              <p class="text-gray-500 mb-2 text-sm">{member.data.title}</p>
              <p class="text-gray-600 text-sm">研究方向：{member.data.research}</p>
            </div>
          ))
        }
      </div>
    </div>
  </section>
  <Footer />
</body>
</html>
'''
with open("src/pages/members.astro", "w", encoding="utf-8") as f:
    f.write(members_content)

# 9. 生成 src/pages/publications.astro（研究成果）
publications_content = '''---
import Navbar from '../components/Navbar.astro';
import Footer from '../components/Footer.astro';
import { getCollection } from 'astro:content';

const publications = await getCollection('publications', ({ data }) => {
  // 按年份倒序排序
  return true;
}).then(items => items.sort((a, b) => b.data.year - a.data.year));

// 分类：论文、项目、专利
const papers = publications.filter(p => p.data.type === 'paper');
const projects = publications.filter(p => p.data.type === 'project');
const patents = publications.filter(p => p.data.type === 'patent');
---
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>研究成果 - XX课题组</title>
</head>
<body class="font-sans text-gray-800 bg-gray-50">
  <Navbar />
  <section class="pt-28 pb-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h1 class="text-3xl font-bold mb-8">研究成果</h1>

      <!-- 学术论文 -->
      <div class="bg-white rounded-lg shadow-sm p-8 mb-10">
        <h2 class="text-2xl font-semibold mb-6 flex items-center">
          <svg class="h-6 w-6 text-primary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
          学术论文
        </h2>
        <div class="space-y-6">
          {
            papers.map(paper => (
              <div class="border-b border-gray-100 pb-6 last:border-0 last:pb-0">
                <h3 class="text-lg font-semibold mb-2">{paper.data.title}</h3>
                <p class="text-gray-600 mb-2">
                  {paper.data.journal} ({paper.data.year}) | {paper.data.level}
                </p>
                <p class="text-gray-500 mb-3">作者：{paper.data.authors}</p>
                {paper.data.doi && (
                  <a href={`https://doi.org/${paper.data.doi}`} target="_blank" rel="noopener noreferrer" class="text-primary hover:underline text-sm">
                    DOI: {paper.data.doi}
                  </a>
                )}
              </div>
            ))
          }
        </div>
      </div>

      <!-- 科研项目 -->
      <div class="bg-white rounded-lg shadow-sm p-8 mb-10">
        <h2 class="text-2xl font-semibold mb-6 flex items-center">
          <svg class="h-6 w-6 text-primary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
          </svg>
          科研项目
        </h2>
        <div class="space-y-6">
          {
            projects.map(project => (
              <div class="border-b border-gray-100 pb-6 last:border-0 last:pb-0">
                <h3 class="text-lg font-semibold mb-2">{project.data.title}</h3>
                <p class="text-gray-600 mb-2">
                  资助单位：{project.data.funder} | 资助金额：{project.data.funding} | 周期：{project.data.period}
                </p>
                <p class="text-gray-500">负责人：{project.data.leader}</p>
              </div>
            ))
          }
        </div>
      </div>

      <!-- 发明专利 -->
      <div class="bg-white rounded-lg shadow-sm p-8">
        <h2 class="text-2xl font-semibold mb-6 flex items-center">
          <svg class="h-6 w-6 text-primary mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z" />
          </svg>
          发明专利
        </h2>
        <div class="space-y-6">
          {
            patents.map(patent => (
              <div class="border-b border-gray-100 pb-6 last:border-0 last:pb-0">
                <h3 class="text-lg font-semibold mb-2">{patent.data.title}</h3>
                <p class="text-gray-600 mb-2">专利号：{patent.data.number} | 授权日期：{patent.data.date}</p>
                <p class="text-gray-500">发明人：{patent.data.inventors}</p>
              </div>
            ))
          }
        </div>
      </div>
    </div>
  </section>
  <Footer />
</body>
</html>
'''
with open("src/pages/publications.astro", "w", encoding="utf-8") as f:
    f.write(publications_content)

# 10. 生成 src/pages/news.astro（新闻动态）
news_content = '''---
import Navbar from '../components/Navbar.astro';
import Footer from '../components/Footer.astro';
import { getCollection } from 'astro:content';

const news = await getCollection('news', ({ data }) => {
  // 按日期倒序排序
  return true;
}).then(items => items.sort((a, b) => new Date(b.data.date) - new Date(a.data.date)));
---
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>新闻动态 - XX课题组</title>
</head>
<body class="font-sans text-gray-800 bg-gray-50">
  <Navbar />
  <section class="pt-28 pb-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h1 class="text-3xl font-bold mb-8">新闻动态</h1>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        {
          news.map(item => (
            <div class="bg-white rounded-lg shadow-sm overflow-hidden hover:shadow-md transition-shadow">
              <img src={item.data.image} alt={item.data.title} class="w-full h-48 object-cover" />
              <div class="p-6">
                <p class="text-gray-400 text-sm mb-2">{new Date(item.data.date).toLocaleDateString()}</p>
                <h3 class="text-xl font-semibold mb-3">{item.data.title}</h3>
                <p class="text-gray-600 mb-4">{item.body}</p>
                {item.data.link && (
                  <a href={item.data.link} target="_blank" rel="noopener noreferrer" class="text-primary hover:underline text-sm">
                    查看详情 →
                  </a>
                )}
              </div>
            </div>
          ))
        }
      </div>
    </div>
  </section>
  <Footer />
</body>
</html>
'''
with open("src/pages/news.astro", "w", encoding="utf-8") as f:
    f.write(news_content)

# 11. 生成 src/pages/contact.astro（联系方式）
contact_content = '''---
import Navbar from '../components/Navbar.astro';
import Footer from '../components/Footer.astro';
---
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>联系方式 - XX课题组</title>
</head>
<body class="font-sans text-gray-800 bg-gray-50">
  <Navbar />
  <section class="pt-28 pb-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h1 class="text-3xl font-bold mb-8">联系方式</h1>
      <div class="bg-white rounded-lg shadow-sm p-8">
        <div class="flex flex-col md:flex-row gap-8">
          <div class="md:w-1/2">
            <h2 class="text-2xl font-semibold mb-6">联系我们</h2>
            <div class="space-y-6">
              <div class="flex items-start">
                <div class="w-10 h-10 bg-primary/10 rounded-full flex items-center justify-center mr-4 flex-shrink-0">
                  <svg class="h-5 w-5 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                  </svg>
                </div>
                <div>
                  <h3 class="text-lg font-semibold mb-1">课题组负责人</h3>
                  <p class="text-gray-600">王五 教授</p>
                  <p class="text-gray-500">邮箱：wangwu@xxx.edu.cn</p>
                  <p class="text-gray-500">电话：010-12345678（办公室）</p>
                </div>
              </div>
              <div class="flex items-start">
                <div class="w-10 h-10 bg-primary/10 rounded-full flex items-center justify-center mr-4 flex-shrink-0">
                  <svg class="h-5 w-5 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                  </svg>
                </div>
                <div>
                  <h3 class="text-lg font-semibold mb-1">实验室地址</h3>
                  <p class="text-gray-600">北京市海淀区XX大街5号 XX大学XX楼 302室</p>
                </div>
              </div>
              <div class="flex items-start">
                <div class="w-10 h-10 bg-primary/10 rounded-full flex items-center justify-center mr-4 flex-shrink-0">
                  <svg class="h-5 w-5 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                  </svg>
                </div>
                <div>
                  <h3 class="text-lg font-semibold mb-1">招新咨询</h3>
                  <p class="text-gray-600">欢迎有志于AI、医疗影像领域的本科生、研究生加入！</p>
                  <p class="text-gray-500">咨询邮箱：lab-recruit@xxx.edu.cn</p>
                </div>
              </div>
            </div>
          </div>
          <div class="md:w-1/2">
            <h2 class="text-2xl font-semibold mb-6">地理位置</h2>
            <!-- 替换为你的实验室地图嵌入代码（来自百度地图/高德地图） -->
            <div class="rounded-lg overflow-hidden shadow-sm h-80 bg-gray-100">
              <iframe 
                src="https://map.baidu.com/xxx"  <!-- 替换为实际地图链接 -->
                width="100%" 
                height="100%" 
                frameborder="0" 
                allowfullscreen="true"
                loading="lazy"
              ></iframe>
            </div>
            <div class="mt-6">
              <img src="/images/logo/wechat-qrcode.jpg" alt="微信公众号二维码" class="w-48 h-auto rounded-md" />
              <p class="text-gray-500 text-sm mt-2">关注课题组微信公众号，获取最新动态</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <Footer />
</body>
</html>
'''
with open("src/pages/contact.astro", "w", encoding="utf-8") as f:
    f.write(contact_content)

# 12. 生成 src/content/config.ts（Astro 内容集合配置，必须！）
content_config = '''import { defineCollection, z } from 'astro:content';

// 成员集合配置
const membersCollection = defineCollection({
  schema: z.object({
    name: z.string(), // 姓名
    title: z.string(), // 职称/年级
    avatar: z.string(), // 头像路径（如 /images/members/xxx.jpg）
    research: z.string(), // 研究方向
    role: z.enum(['teacher', 'student']), // 角色（导师/学生）
    email: z.string().optional(), // 邮箱（学生可选）
  }),
});

// 成果集合配置
const publicationsCollection = defineCollection({
  schema: z.object({
    title: z.string(), // 标题（论文名/项目名/专利名）
    type: z.enum(['paper', 'project', 'patent']), // 类型
    year: z.number(), // 发表/立项年份
    authors: z.string().optional(), // 作者/发明人（论文/专利）
    journal: z.string().optional(), // 期刊/会议（论文）
    level: z.string().optional(), // 级别（如 SCI 一区、CCF A类）
    doi: z.string().optional(), // DOI（论文）
    funder: z.string().optional(), // 资助单位（项目）
    funding: z.string().optional(), // 资助金额（项目）
    period: z.string().optional(), // 周期（项目）
    leader: z.string().optional(), // 负责人（项目）
    number: z.string().optional(), // 专利号（专利）
    date: z.string().optional(), // 授权日期（专利）
  }),
});

// 新闻集合配置
const newsCollection = defineCollection({
  schema: z.object({
    title: z.string(), // 新闻标题
    date: z.string(), // 日期（格式：YYYY-MM-DD）
    image: z.string(), // 新闻配图路径
    link: z.string().optional(), // 详情链接（可选）
  }),
});

export const collections = {
  members: membersCollection,
  publications: publicationsCollection,
  news: newsCollection,
};
'''
with open("src/content/config.ts", "w", encoding="utf-8") as f:
    f.write(content_config)

# 13. 生成 Markdown 示例文件（成员、成果、新闻）
# 成员示例（导师）
member_teacher = '''---
name: 王五
title: 博士生导师、课题组负责人
avatar: /images/members/wangwu.jpg
research: AI 医疗影像分析、机器学习优化
role: teacher
email: wangwu@xxx.edu.cn
---
个人简介：20XX年毕业于XX大学计算机科学与技术专业，获博士学位；20XX-20XX年在XX大学从事博士后研究；20XX年加入XX大学XX学院。主要研究方向为人工智能在医疗健康领域的应用，发表 IEEE TMI、NeurIPS 等顶级期刊/会议论文30余篇，主持国家自然科学基金、省部级项目5项，申请发明专利10余项。
'''
with open("src/content/members/teacher-wang.md", "w", encoding="utf-8") as f:
    f.write(member_teacher)

# 成员示例（学生）
member_student = '''---
name: 张三
title: 2022级博士生
avatar: /images/members/zhangsan.jpg
research: 肺结节检测与良恶性诊断
role: student
---
'''
with open("src/content/members/student-zhang.md", "w", encoding="utf-8") as f:
    f.write(member_student)

# 成果示例（论文）
publication_paper = '''---
title: Deep Learning for Lung Nodule Detection in CT Images
type: paper
year: 2024
authors: 张三, 李四, 王五*
journal: IEEE Transactions on Medical Imaging
level: SCI 一区，IF=11.0
doi: 10.1109/TMI.2024.338XXX
---
'''
with open("src/content/publications/paper-2024.md", "w", encoding="utf-8") as f:
    f.write(publication_paper)

# 新闻示例
news_item = '''---
title: 课题组在 NeurIPS 2023 发表最新研究成果
date: 2023-12-10
image: /images/news/neurips-2023.jpg
link: https://neurips.cc/Conferences/2023
---
课题组博士生赵六的论文《Efficient Neural Network Compression via Knowledge Distillation》被 NeurIPS 2023 接收。该论文提出了一种新型知识蒸馏框架，有效解决了大规模神经网络部署的效率问题，相关技术已申请发明专利。
'''
with open("src/content/news/2023-12-10-neurips.md", "w", encoding="utf-8") as f:
    f.write(news_item)

print("✅ 模板文件生成完成！")
print("\n📋 下一步操作指引：")
print("1. 将课题组 Logo、成员头像、实验室照片等图片，分别放入 public/images/ 对应文件夹；")
print("2. 编辑 src/content/ 下的 Markdown 文件，替换为课题组真实内容；")
print("3. 运行 `npm install` 安装依赖，`npm run dev` 本地预览；")
print("4. 推送代码到 GitHub，关联 Vercel 自动部署！")