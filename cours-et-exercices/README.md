# 课程学习与练习 | Travaux dirigés (TD) & exercices

**中文**：这里整理 NF18《数据库》课程的随堂习题、课程示例代码与零散练习，按 TD（指导课）编号组织。课程设计主项目见仓库根目录 [README.md](../README.md)。

**Français** : Ce dossier regroupe les exercices des TD, les exemples de cours et quelques exercices isolés du cours NF18. Le projet principal se trouve à la racine du dépôt ([README.md](../README.md)).

## 学习内容总览 | Vue d'ensemble

这些练习按课程进度覆盖了以下主题 / Thèmes couverts au fil du cours :

1. **关系模型与关系代数** — SQL 建模、复合主键 / 外键，以及关系代数（RESTRICTION / JOINDRE / PROJECTION / JOINTURE EXTERNE）到 SQL 的翻译（TD3）；
2. **SQL 与应用编程** — 用 `psycopg2` 连接 PostgreSQL 做增删改查，用 `\copy` 导入 CSV 数据（TD4）；
3. **多表查询与聚合** — 多表 `JOIN`、`LEFT JOIN` 反连接、`GROUP BY` / `HAVING`、子查询（TD5 与补充练习）;
4. **半结构化数据** — JSON 解析与 JavaScript / HTML 简单演示。

## td/ — TD 习题 / Exercices des TD

### td3-ex1.sql · 公交经停与旅游景点（TD3）
**中文**：设计公交经停表 `Arret_Bus`（"线路号 + 时刻"复合主键）、旅游景点表 `Site_Touristique`，以及两者之间的关联表 `Dessert_Site`（复合外键）。重点练习复合主键 / 复合外键与 `TIME` 类型。

**Français** : Modélisation des arrêts de bus (`Arret_Bus`, clé primaire composée ligne + horaire), des sites touristiques (`Site_Touristique`) et de la table d'association `Dessert_Site` — mise en pratique des clés étrangères composées et du type `TIME`.

### td3-ex2.sql · 公交网络与关系代数（TD3）
**中文**：建模公交网络（`Ligne` / `Station` / `Arrêt` / `Conducteur` / `Bus` / `Trajet`），并把每条关系代数表达式翻译成 SQL，例如"从 Gare SNCF 站首发的巴士及其类型"、"不被波纹管（Soufflets）巴士服务的线路"（练习右外连接 + `IS NULL` 实现反连接）。

**Français** : Schéma d'un réseau de bus (`Ligne`, `Station`, `Arrêt`, `Conducteur`, `Bus`, `Trajet`) et traduction d'expressions d'algèbre relationnelle en SQL — par exemple « bus au départ de la station Gare SNCF » ou « lignes non desservies par les bus à soufflets » (anti-jointure via jointure externe droite et `IS NULL`).

### td4-ex1.sql / td4-ex1.py · CSV 导入与 Python 增删改查（TD4）
**中文**：先用 PostgreSQL 的 `\copy` 从 `dpt2.csv` 导入法国省份人口数据，再在 Python（psycopg2）中完成统计（人口最多 / 最少的省份）与增删改（`INSERT` / `DELETE` / `UPDATE`），练习游标遍历与参数化 SQL。

**Français** : Import d'un fichier CSV (`dpt2.csv`, population des départements français) via `\copy`, puis CRUD en Python/psycopg2 : requête statistique (département le plus / le moins peuplé), insertion, suppression et mise à jour — itération sur curseur et SQL paramétré.

### td4-ex2.sql / td4-ex2.py · 学生-作业-成绩模型（TD4）
**中文**：建立 `etudiant` / `devoir` / `note` 三表（复合主键、`CHECK` 成绩介于 0–20），并在 Python 中按学生姓名 `JOIN` 查询其各次作业的成绩。

**Français** : Création des tables `etudiant` / `devoir` / `note` (clé primaire composée, `CHECK` sur la note entre 0 et 20), puis interrogation par JOIN en Python pour afficher les notes d'un étudiant.

### td5-ex2.sql · 版本管理系统（TD5）
**中文**：用 `Users` / `Documents` / `Versions` 模拟一个简易版本管理系统，练习：JOIN 查文档作者；`LEFT JOIN` + `IS NULL` 找出"既未创建文档、也未贡献版本"的用户；`GROUP BY` + `HAVING` 统计每人贡献次数并按次数降序；用 `MAX` 取每份文档的最新版本号。

**Français** : Mini-système de gestion de versions (`Users`, `Documents`, `Versions`) : auteur d'un document via JOIN ; utilisateurs n'ayant ni créé ni contribué via `LEFT JOIN` / `IS NULL` ; nombre de contributions par utilisateur avec `GROUP BY` / `HAVING` et tri décroissant ; dernière version de chaque document avec `MAX` et `GROUP BY`.

### sqlbook.sql · 菜谱数据库（补充练习 / exercice supplémentaire）
**中文**：`Plats` / `Ingredients` / `Contient` 三表，包含自引用外键（一道菜可以以另一道菜为"基底"）、跨两列的复合外键、`CHECK` 枚举计量单位；查询练习如"使用某食材的菜"、"从未被任何菜谱使用的食材"（`LEFT OUTER JOIN` + `IS NULL`）、自连接查询。

**Français** : Tables `Plats` / `Ingredients` / `Contient` : clé étrangère autoréférente (une recette peut servir de base à une autre), clé étrangère composée sur deux colonnes, `CHECK` sur les unités de mesure ; requêtes d'entraînement (recettes contenant un ingrédient donné, ingrédients jamais utilisés via `LEFT OUTER JOIN` / `IS NULL`, auto-jointure).

## demos/ — 课程示例 / Exemples de cours

### demo-json/ · JSON 与 JavaScript
**中文**：`index.html` + `query.js` + `exemple.json`。在页面上选择一个 JSON 文件，`FileReader` 读取内容、`JSON.parse` 解析后把字段渲染到页面——对应课程"半结构化数据 / JSON"主题的入门演示。直接用浏览器打开 `index.html`，再选择 `exemple.json` 即可体验。

**Français** : `index.html` + `query.js` + `exemple.json`. On choisit un fichier JSON dans la page ; `FileReader` lit son contenu, `JSON.parse` le transforme en objet et les champs sont affichés dans le DOM — une petite démonstration sur les données semi-structurées (JSON). Ouvrez `index.html` dans un navigateur puis sélectionnez `exemple.json`.

## 运行环境 | Environnement

- PostgreSQL（脚本编写时使用学校教学服务器 `tuxa.sme.utc`）+ Python 3 与 `psycopg2`；
- `td4-ex1.sql` 中 `\copy` 的路径已用占位符 `/chemin/vers/dpt2.csv` 代替，本地使用时请改为你自己的 CSV 路径；
- ⚠️ **注意 / Attention**：Python 脚本中的数据库连接参数（`HOST` / `USER` / `PASSWORD` / `DATABASE`）已替换为占位符（`your_user` 等）；使用前请填入你自己的配置，或改用环境变量，切勿提交真实凭据。

## 归档说明 | Archive

部分早期草稿与零散笔记（例如把 TD4 练习和项目函数初稿合在一起的旧脚本 `projet.py`、笔记片段 `bigbrother.sql` 与 `c4.sql`）已移至仓库根目录的 [archive](../archive) 文件夹，仅作为学习过程记录保留。

Quelques brouillons et notes anciens (par exemple l'ancien script `projet.py` mêlant les exercices de TD4 et les premières fonctions du projet, ainsi que les fragments de notes `bigbrother.sql` et `c4.sql`) ont été déplacés dans le dossier [archive](../archive) à la racine du dépôt, conservés uniquement comme trace du parcours d'apprentissage.
