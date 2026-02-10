# 如何在 Vercel 上部署《赤色纪元》

Vercel 是一个非常优秀的静态网站托管平台，速度快且全球访问流畅。
由于 Ren'Py 游戏需要编译成 Web 格式（HTML/WASM），不能直接把源代码（Python）放到 Vercel 上运行。

我们已经配置了 GitHub Actions 自动构建游戏。你可以通过以下两种方式部署到 Vercel：

## 方法一：全自动同步（推荐）

这个方法利用我们已经生成的 `gh-pages` 分支（里面是编译好的游戏）。

1. 登录 [Vercel](https://vercel.com/)。
2. 点击 **"Add New..."** -> **"Project"**。
3. 在 "Import Git Repository" 列表中找到 `Red-Era`，点击 **Import**。
4. **关键步骤**：
   - 在 **Framework Preset** 中选择 **Other**。
   - 展开 **Build and Output Settings**。
   - 此时你会发现无法选择分支。**先点击 Deploy**（它可能会失败，或者部署 Main 分支的源码，这没关系）。
5. 项目创建后，进入该项目的 **Settings** -> **Git**。
6. 在 **Production Branch** 选项中，将 `main` 修改为 `gh-pages`。
7. 点击 **Save**。
8. 回到 **Deployments** 标签页，点击右上角的三个点，选择 **Redeploy**。
9. 这次 Vercel 会直接抓取 `gh-pages` 分支里的游戏文件，部署成功！

## 方法二：手动上传

如果你不想绑定 GitHub，可以手动上传构建好的文件。

1. 在 GitHub 仓库的 **Actions** 页面，找到最新的 "Build and Deploy" 记录。
2. 在底部的 **Artifacts** 区域，下载 `red-era-web` 压缩包。
3. 解压这个文件。
4. 安装 [Vercel CLI](https://vercel.com/docs/cli) 或者直接在 Vercel 网页控制台拖拽上传这些文件（如果你使用 Vercel CLI，在解压后的目录运行 `vercel deploy` 即可）。

---

**注意**：每次你在 `main` 分支更新代码，GitHub Actions 会自动更新 `gh-pages` 分支，Vercel 也会随之自动更新（如果你用了方法一）。
