import { defineConfig } from "drizzle-kit";

export default defineConfig({
  schema: "./src/infra/schema.ts",
  out: "./drizzle",
  dialect: "postgresql",
  dbCredentials: {
    host: "postgres",
    database: await Bun.file("/run/secret/pg_db").text(),
    user: await Bun.file("/run/secret/pg_user").text(),
    password: await Bun.file("/run/secret/pg_password").text(),
  },
});
