import { defineCollection, z } from 'astro:content';

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
