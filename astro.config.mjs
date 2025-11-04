import { defineConfig } from 'astro/config';
import tailwind from "@astrojs/tailwind";

// https://astro.build/config
export default defineConfig({
  integrations: [tailwind()],
  site: "https://lab-website-xxx.vercel.app", // 后续替换为你的 Vercel 域名或自定义域名
});
