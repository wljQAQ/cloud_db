/** @type {import('prettier').Config} */
module.exports = {
  semi: true,
  tabWidth: 2,
  arrowParens: "avoid",
  trailingComma: "none",
  bracketSpacing: true,
  singleQuote: true,
  printWidth: 140,
  importOrder: [
    "^vue",
    "",
    "^@cloud_db/(.*)$",
    "",
    "<THIRD_PARTY_MODULES>",
    "",
    "^types$",
    "",
    "^@/(.*)$",
    "",
    "^[./]",
    "",
  ],
  importOrderParserPlugins: ["typescript", "jsx", "decorators-legacy", "vue"],
  plugins: [
    "@ianvs/prettier-plugin-sort-imports",
    "prettier-plugin-tailwindcss",
  ],
};
