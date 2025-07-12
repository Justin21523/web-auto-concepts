Web Automation × Git 教學專案

> 📘 本專案採用繁體中文教學，並提供中英文對照重要術語
> 📂 以模組化方式拆分，每個模組對應獨立 Feature 分支
> 🧾 採用 Conventional Commits 格式：feat/fix/docs/chore/refactor

## 專案結構

- **docs/**：每個模組的教學文件
- **module-00/**：模組 0 的補充筆記與範例指令
- **requirements.txt & package.json**：環境相依檔

## Git 分支與提交約定

- 分支命名：`feature/module-00-initialization`
- 提交前綴（Commit message）：
  - `chore:` 初始化、設定檔
  - `docs:` 撰寫文件
  - `feat:` 新增範例程式

## 快速開始

1. clone 專案
   ```bash
   git clone <你的 repo URL>
   cd web-automation-git
