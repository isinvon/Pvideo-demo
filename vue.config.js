import { defineConfig } from '@vue/cli-service';
export default defineConfig({
  publicPath: process.env.NODE_ENV === 'production' ? './.' : '/',
  transpileDependencies: true,
  outputDir: './dist', // 打包输出路径
  pages: {
    home: {
      entry: 'src/home/src/main.js',
      template: 'src/home/public/index.html',
      filename: 'index.html',
      title: 'Home Page',
      chunks: ['chunk-vendors', 'chunk-common', 'home']
    }
  }
});
