[English](README.md) | [简体中文](README.zh-CN.md)

# Offline UX Kit：离线体验测试工具包

给现有 HTML 或静态 Web 原型增加本地行为记录、主动反馈和一键可视化报告。它包含可供 AI 阅读的 Skill，也包含可复用代码，不是一份要求 AI 每次重新造轮子的提示词。

当前为 **beta 开发预览版**。自动代码测试已通过，真实浏览器 file://、页面视觉和 Windows 验收尚未完成。详见 [验收记录](docs/VALIDATION.md)。

## 快速安装

把下面这句话交给支持命令行的 Agent：

```text
帮我安装 offline-ux-kit：https://raw.githubusercontent.com/Fable-Forge/offline-ux-kit/main/docs/install.md
```

也可以使用 Agent Skills CLI：

```bash
npx skills add Fable-Forge/offline-ux-kit
```

更新和卸载分别见 [更新说明](docs/update.md) 与 [卸载说明](docs/uninstall.md)。

## 先看效果

1. 解压后，用普通浏览器窗口打开 `dist/form.html`。
2. 输入匿名代号、同意采集，再开始操作。
3. 选择选项，下一步，再返回改选；记录一次“这里有问题”。
4. 完成任务后点击“结束并下载 HTML 报告”。
5. 打开报告查看指标、流程、停留图、问题分布和事件明细。
6. 打开 `dist/review.html`，导入多人报告或 JSON。

`dist/dialogue.html` 是第二种场景：简短的分支客户沟通演练。它是原创示例，不是旧销售游戏的复刻，也不接大模型 API。

`dist/sample-report.html` 是合成数据示例，不能作为真实用户研究结论。

## 给 AI 使用

将整个目录交给编码助手，让它读取 `SKILL.md`，然后给出目标应用路径。例如：

> 使用这个目录中的 offline-ux-kit Skill，为我的离线表单增加体验测试。先检查代码并列出事件接入表，保留原业务逻辑，默认不采集输入原文，增加主动反馈和结束报告按钮。代码测试与真实浏览器测试分开报告。

压缩包没有安装程序，不会自动安装、启用或发布。需要自动发现时，再按所用助手的安装流程，将完整目录安装到你指定的技能位置。

## 开发命令

需要 Node.js 18 或更新版本；打包及其回归测试还需要 Python 3。无须安装 npm 依赖。

```sh
node scripts/build.cjs
node --test tests/core.test.cjs
python tests/package.test.py
python scripts/package.py ../offline-ux-kit.zip
```

运行时代码在 `assets/offline-ux.js`；两个示例共用 `examples/demo.html`。构建输出在 `dist/`，可直接分发。

## 数据与报告

默认记录任务、步骤、选项、返回改选、回答字数、反馈分类、活跃/后台时间，以及接入方明确调用的 AI 耗时和 fallback。数据优先存在 IndexedDB，失败时退回 localStorage；都不可用时仅在内存中保留并显示警告。

报告包含 KPI、会话有序漏斗、步骤活跃时间柱状图、反馈/疑似问题环形图、选择分布和可展开事件表。支持导出 JSON、Markdown 和浏览器打印。多人分析按应用、版本、批次、模式分组，不混算。

默认不记录输入原文、密码、密钥、请求正文、错误详情和导入文件业务内容。反馈只保留分类，暂不提供自由留言。报告仍是行为数据，不代表可以随意公开。

## 首版边界

- 支持浏览器 HTML/静态 Web，不支持原生桌面或移动应用。
- 路径是事件序列，不是录屏，也不是 DOM 回放。
- 没有大厅轨迹地图、自动课程分析或广告归因模型。
- 不能直接导入旧私有 The Closer v2 数据；需要另写转换器。
- 可切换不同批次查看，但没有并排对比图。
- UI 是中英混合标注，说明和文章提供完整中英文版本。
- 快照存储适合轻量试玩，不适合高频、超长会话。
- 不支持同一会话在多个标签页同时写入。
- 刷新后示例从第一步重启，旧任务记为 interrupted，不伪装成完整业务状态恢复。
- 关闭浏览器时的最后一段异步写入可能丢失，不能承诺零丢失。

MIT 开源许可，署名 FableForge。这里只包含独立重建的通用代码和原创示例，不含公司文件或旧游戏源码。
